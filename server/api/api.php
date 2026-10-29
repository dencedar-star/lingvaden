<?php
/**
 * JSON API платформы: /api/api.php?a=<действие>.
 *
 * Общие:   login (единый вход по 6-значному коду: по коду понятно, учитель это или ученик), me (GET), consent, logout,
 *          log (пакет событий, sendBeacon), profile (ФИО, e-mail, Telegram), avatar_set|avatar_del, avatar (GET)
 * Ученик:  s_code (вход по коду или ссылке), forget (удаляет свои данные), s_hw_list|s_hw (GET), s_hw_submit
 * Учитель: t_data, t_student_add|update|delete|relink|mail, t_space_add|update|delete, t_member, t_student, t_review,
 *          t_hw_add|t_hw_archive, t_hw_list|t_hw_result (GET)
 */

declare(strict_types=1);
require __DIR__ . '/_lib.php';

header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: same-origin');

$a = (string)($_GET['a'] ?? '');
$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';

// POST только со своего сайта (cookie и так SameSite=Lax; это второй замок)
if ($method === 'POST') {
    $origin = (string)($_SERVER['HTTP_ORIGIN'] ?? '');
    if ($origin !== '' && parse_url($origin, PHP_URL_HOST) !== preg_replace('/:\d+$/', '', (string)($_SERVER['HTTP_HOST'] ?? ''))) {
        fail('origin', 403);
    }
} elseif (!in_array($a, ['me', 't_data', 't_student', 't_review', 'avatar', 's_hw_list', 's_hw', 't_hw_list', 't_hw_result'], true)) {
    fail('method', 405);
}

try {
    $pdo = en_db();
} catch (Throwable $e) {
    error_log('en api db: ' . $e->getMessage());
    fail('db', 503);
}

$ID = '/^[a-z0-9_-]{1,40}$/';

function ctx(array $b): array
{
    global $ID;
    $c = [];
    foreach (['course', 'unit', 'page'] as $k) {
        $v = (string)($b[$k] ?? '');
        $c[$k] = preg_match($ID, $v) ? $v : '';
    }
    $c['path'] = mb_substr((string)($b['path'] ?? ''), 0, 160);
    return $c;
}

function need_teacher(PDO $pdo): array
{
    $t = current_user($pdo, 'teacher');
    if (!$t) {
        fail('auth', 401);
    }
    // без принятых документов кабинет не работает (их собирает окно согласия при входе)
    if (consent_missing($pdo, 'teacher', (int)$t['id'])) {
        fail('consent', 403);
    }
    return $t;
}

/** Ученик этого учителя или 404. */
function own_student(PDO $pdo, array $t, $id): array
{
    $st = $pdo->prepare('SELECT * FROM en_student WHERE id = ? AND teacher_id = ?');
    $st->execute([(int)$id, (int)$t['id']]);
    $s = $st->fetch();
    if (!$s) {
        fail('notfound', 404);
    }
    return $s;
}

function own_space(PDO $pdo, array $t, $id): array
{
    $st = $pdo->prepare('SELECT * FROM en_space WHERE id = ? AND teacher_id = ?');
    $st->execute([(int)$id, (int)$t['id']]);
    $s = $st->fetch();
    if (!$s) {
        fail('notfound', 404);
    }
    return $s;
}

function need_student(PDO $pdo): array
{
    $s = current_user($pdo, 'student');
    if (!$s) {
        fail('auth', 401);
    }
    if (consent_missing($pdo, 'student', (int)$s['id'])) {
        fail('consent', 403);
    }
    return $s;
}

/** Вошедший пользователь (на устройстве — один: учитель или ученик). */
function who(PDO $pdo): array
{
    $t = current_user($pdo, 'teacher');
    if ($t) {
        return ['teacher', $t];
    }
    $s = current_user($pdo, 'student');
    if ($s) {
        return ['student', $s];
    }
    fail('auth', 401);
    return [];
}

function avatar_url(string $role, array $u): ?string
{
    return !empty($u['avatar_at']) ? '/api/api.php?a=avatar&r=' . ($role === 'teacher' ? 't' : 's') . '&id=' . (int)$u['id']
        . '&v=' . strtotime((string)$u['avatar_at']) : null;
}

function clean_tg($s): ?string
{
    $s = trim((string)$s);
    if ($s === '') {
        return null;
    }
    if (preg_match('~(?:t\.me/|telegram\.me/|^@?)([A-Za-z0-9_]{4,32})/?$~', $s, $m)) {
        return '@' . $m[1];
    }
    if (preg_match('/^\+?[0-9 ()-]{7,20}$/', $s)) {
        return preg_replace('/[^0-9+]/', '', $s);
    }
    return '';
}

/** Новый вход: на устройстве остаётся только один пользователь. */
function login_as(PDO $pdo, string $role, array $u, string $via): void
{
    $other = $role === 'teacher' ? 'student' : 'teacher';
    if (!empty($_COOKIE[cookie_name($other)])) {
        session_end($pdo, $other);
    }
    $cur = current_user($pdo, $role);
    if (!$cur || (int)$cur['id'] !== (int)$u['id']) {
        session_start_for($pdo, $role, (int)$u['id']);
    }
    if ($role === 'teacher') {
        $pdo->prepare('UPDATE en_teacher SET last_login_at = ? WHERE id = ?')->execute([now(), $u['id']]);
        log_event($pdo, 'teacher', (int)$u['id'], (int)$u['id'], 'login', ['data' => ['via' => $via, 'device' => device()]]);
    } else {
        $pdo->prepare('UPDATE en_student SET first_login_at = COALESCE(first_login_at, ?) WHERE id = ?')->execute([now(), $u['id']]);
        log_event($pdo, 'student', (int)$u['id'], (int)$u['teacher_id'], 'login', ['data' => ['via' => $via, 'device' => device()]]);
    }
}

/** Задания домашней работы: [{ex, n, unit, page}]. */
function hw_items(array $hw): array
{
    $it = json_decode((string)$hw['items'], true);
    return is_array($it) ? $it : [];
}

function student_link(array $s): string
{
    return site_url() . '/s/' . $s['token'];
}

function tlog(PDO $pdo, array $t, string $type, array $data = []): void
{
    log_event($pdo, 'teacher', (int)$t['id'], (int)$t['id'], $type, ['data' => $data]);
}

switch ($a) {

// ---- кто я ----------------------------------------------------------------
case 'me':
    $out = ['ok' => true, 'student' => null, 'teacher' => null];
    $t = current_user($pdo, 'teacher');
    $s = $t ? null : current_user($pdo, 'student');
    if ($s) {
        $hw = $pdo->prepare('SELECT COUNT(*) FROM en_hw_student hs JOIN en_hw h ON h.id = hs.hw_id AND h.archived_at IS NULL
                             WHERE hs.student_id = ? AND hs.submitted_at IS NULL');
        $hw->execute([(int)$s['id']]);
        $out['student'] = ['id' => (int)$s['id'], 'name' => $s['name'], 'teacher' => $s['teacher_name'],
            'consent' => consent_missing($pdo, 'student', (int)$s['id']), 'email' => $s['email'], 'telegram' => $s['telegram'],
            'code' => $s['code'], 'avatar' => avatar_url('student', $s), 'hw_open' => (int)$hw->fetchColumn()];
        if (!empty($_GET['state'])) {
            // state=all — все курсы (id заданий уникальны), иначе — один курс
            $course = preg_match($ID, (string)$_GET['state']) ? (string)$_GET['state'] : '';
            $cw = $course === 'all' ? '' : ' AND course = ?';
            $cp = $course === 'all' ? [(int)$s['id']] : [(int)$s['id'], $course];
            $st = $pdo->prepare('SELECT ex, best, last, total, shown, state FROM en_progress WHERE student_id = ?' . $cw);
            $st->execute($cp);
            $p = [];
            foreach ($st as $r) {
                $p[$r['ex']] = ['s' => (int)$r['last'], 't' => (int)$r['total'], 'best' => (int)$r['best'],
                    'st' => $r['state'] !== null ? json_decode($r['state'], true) : null];
            }
            $st = $pdo->prepare('SELECT wid, text FROM en_writing WHERE student_id = ?' . $cw);
            $st->execute($cp);
            $w = [];
            foreach ($st as $r) {
                $w[$r['wid']] = $r['text'];
            }
            $out['state'] = ['p' => $p, 'w' => $w];
        }
    }
    if ($t) {
        $hw = $pdo->prepare('SELECT COUNT(*) FROM en_hw_student hs JOIN en_hw h ON h.id = hs.hw_id
                             WHERE h.teacher_id = ? AND hs.submitted_at IS NOT NULL AND hs.seen_at IS NULL');
        $hw->execute([(int)$t['id']]);
        $out['teacher'] = ['id' => (int)$t['id'], 'name' => $t['name'], 'consent' => consent_missing($pdo, 'teacher', (int)$t['id']),
            'email' => $t['email'], 'telegram' => $t['telegram'], 'avatar' => avatar_url('teacher', $t), 'hw_new' => (int)$hw->fetchColumn()];
    }
    json_out($out);

// ---- единый вход по коду ------------------------------------------------------
case 'login':
case 't_login':
    $code = preg_replace('/\D/', '', (string)(body()['code'] ?? ''));
    $w = throttle_wait($pdo, 'teacher');
    if ($w) {
        fail('wait:' . $w, 429);
    }
    $u = null;
    $role = '';
    if (strlen($code) === 6) {
        $st = $pdo->prepare("SELECT * FROM en_teacher WHERE code = ? AND status = 'active'");
        $st->execute([$code]);
        $u = $st->fetch();
        $role = 'teacher';
        if (!$u) {
            $st = $pdo->prepare("SELECT s.* FROM en_student s JOIN en_teacher t ON t.id = s.teacher_id AND t.status = 'active' WHERE s.code = ?");
            $st->execute([$code]);
            $u = $st->fetch();
            $role = 'student';
        }
    }
    if (!$u) {
        throttle_note($pdo, 'teacher');
        fail('badcode', 404);
    }
    login_as($pdo, $role, $u, 'code');
    json_out(['ok' => true, 'role' => $role]);

// ---- профиль: ФИО, e-mail, Telegram, фото -------------------------------------
case 'profile':
    list($role, $u) = who($pdo);
    $b = body();
    $name = clean_text($b['name'] ?? $u['name'], 200);
    if ($name === '') {
        fail('name');
    }
    $email = clean_email($b['email'] ?? '');
    if (trim((string)($b['email'] ?? '')) !== '' && $email === null) {
        fail('email');
    }
    $tg = clean_tg($b['telegram'] ?? '');
    if ($tg === '') {
        fail('telegram');
    }
    $table = $role === 'teacher' ? 'en_teacher' : 'en_student';
    $pdo->prepare("UPDATE $table SET name = ?, email = ?, telegram = ? WHERE id = ?")->execute([$name, $email, $tg, (int)$u['id']]);
    log_event($pdo, $role, (int)$u['id'], $role === 'teacher' ? (int)$u['id'] : (int)$u['teacher_id'], 'profile',
        ['data' => ['name' => $name !== $u['name'], 'email' => $email !== $u['email'], 'telegram' => $tg !== $u['telegram']]]);
    json_out(['ok' => true]);

case 'avatar_set':
    list($role, $u) = who($pdo);
    $data = (string)(body()['data'] ?? '');
    if (!preg_match('~^data:image/(jpeg|png|webp);base64,([A-Za-z0-9+/=]+)$~', $data, $m)) {
        fail('image');
    }
    $bin = base64_decode($m[2], true);
    $info = $bin !== false && strlen($bin) <= 300000 ? @getimagesizefromstring($bin) : false;
    if (!$info || !in_array($info['mime'], ['image/jpeg', 'image/png', 'image/webp'], true) || $info[0] > 1024 || $info[1] > 1024) {
        fail('image');
    }
    $pdo->prepare('REPLACE INTO en_avatar (role, user_id, mime, data, updated_at) VALUES (?, ?, ?, ?, ?)')
        ->execute([$role, (int)$u['id'], $info['mime'], $bin, now()]);
    $pdo->prepare('UPDATE ' . ($role === 'teacher' ? 'en_teacher' : 'en_student') . ' SET avatar_at = ? WHERE id = ?')->execute([now(), (int)$u['id']]);
    $u['avatar_at'] = now();
    json_out(['ok' => true, 'avatar' => avatar_url($role, $u)]);

case 'avatar_del':
    list($role, $u) = who($pdo);
    $pdo->prepare('UPDATE en_avatar SET data = \'\', mime = \'none\', updated_at = ? WHERE role = ? AND user_id = ?')->execute([now(), $role, (int)$u['id']]);
    $pdo->prepare('UPDATE ' . ($role === 'teacher' ? 'en_teacher' : 'en_student') . ' SET avatar_at = NULL WHERE id = ?')->execute([(int)$u['id']]);
    json_out(['ok' => true]);

case 'avatar':   // фото видят: сам человек, учитель — своих учеников, ученик — своего учителя
    $r = ($_GET['r'] ?? '') === 't' ? 'teacher' : 'student';
    $id = (int)($_GET['id'] ?? 0);
    $t = current_user($pdo, 'teacher');
    $s = $t ? null : current_user($pdo, 'student');
    $ok = false;
    if ($t) {
        if ($r === 'teacher') {
            $ok = $id === (int)$t['id'];
        } else {
            $st = $pdo->prepare('SELECT 1 FROM en_student WHERE id = ? AND teacher_id = ?');
            $st->execute([$id, (int)$t['id']]);
            $ok = (bool)$st->fetch();
        }
    } elseif ($s) {
        $ok = $r === 'student' ? $id === (int)$s['id'] : $id === (int)$s['teacher_id'];
    }
    $st = $pdo->prepare('SELECT mime, data FROM en_avatar WHERE role = ? AND user_id = ?');
    $st->execute([$r, $id]);
    $img = $ok ? $st->fetch() : null;
    if (!$img || $img['mime'] === 'none') {
        http_response_code(404);
        exit;
    }
    header('Content-Type: ' . $img['mime']);
    header('Cache-Control: private, max-age=2592000');
    echo $img['data'];
    exit;

// ---- согласия при первом входе --------------------------------------------
case 'consent':
    $b = body();
    $role = ($b['role'] ?? '') === 'teacher' ? 'teacher' : 'student';
    $u = current_user($pdo, $role);
    if (!$u) {
        fail('auth', 401);
    }
    $docs = is_array($b['docs'] ?? null) ? $b['docs'] : [];
    $missing = consent_missing($pdo, $role, (int)$u['id']);
    foreach ($missing as $d) {
        if (!in_array($d, $docs, true)) {
            fail('need:' . $d);
        }
    }
    $extra = null;
    if ($role === 'student') {
        $age = (string)($b['age'] ?? '');
        if (!in_array($age, ['14plus', 'parent'], true)) {
            fail('need:age');
        }
        $extra = $age === '14plus' ? 'Ученику 14 лет или больше — согласие даёт сам' : 'Ученику меньше 14 — согласие подтвердил родитель (законный представитель)';
        if ($age === 'parent') {
            $pn = clean_text($b['parent'] ?? '', 120);
            if ($pn !== '') {
                $extra .= ': ' . $pn;
            }
        }
    }
    $tid = $role === 'teacher' ? (int)$u['id'] : (int)$u['teacher_id'];
    $ins = $pdo->prepare('INSERT INTO en_consent (role, user_id, teacher_id, person, doc, version, extra, accepted_at, ip_hash, user_agent)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)');
    foreach ($missing as $d) {
        $ins->execute([$role, (int)$u['id'], $tid, $u['name'], $d, EN_DOCS[$d], $extra, now(), ip_hash(), ua()]);
    }
    $table = $role === 'teacher' ? 'en_teacher' : 'en_student';
    $pdo->prepare("UPDATE $table SET consent_at = COALESCE(consent_at, ?) WHERE id = ?")->execute([now(), (int)$u['id']]);
    log_event($pdo, $role, (int)$u['id'], $tid, 'consent', ['data' => ['docs' => $missing]]);
    json_out(['ok' => true]);

case 'logout':
    foreach (['teacher', 'student'] as $role) {
        $u = current_user($pdo, $role);
        if ($u) {
            log_event($pdo, $role, (int)$u['id'], $role === 'teacher' ? (int)$u['id'] : (int)$u['teacher_id'], 'logout');
        }
        if (!empty($_COOKIE[cookie_name($role)])) {
            session_end($pdo, $role);
        }
    }
    json_out(['ok' => true]);

// ---- ученик: удалить свои данные (отзыв согласия) --------------------------
case 'forget':
    $s = current_user($pdo, 'student');
    if (!$s) {
        fail('auth', 401);
    }
    log_event($pdo, 'system', 0, (int)$s['teacher_id'], 'student_forget', ['data' => ['name' => $s['name']]]);
    delete_student_data($pdo, (int)$s['id']);
    session_end($pdo, 'student');
    json_out(['ok' => true]);

// ---- ученик: вход по коду ссылки --------------------------------------------
case 's_code':
    $code = strtolower(preg_replace('/[^a-z0-9]/i', '', (string)(body()['code'] ?? '')));
    if (preg_match('~/s/([a-z0-9]+)~i', (string)(body()['code'] ?? ''), $m)) {
        $code = strtolower($m[1]);
    }
    $w = throttle_wait($pdo, 'student');
    if ($w) {
        fail('wait:' . $w, 429);
    }
    $st = $pdo->prepare('SELECT s.* FROM en_student s JOIN en_teacher t ON t.id = s.teacher_id AND t.status = \'active\' WHERE s.token = ?');
    $st->execute([$code]);
    $s = $st->fetch();
    if (!$s) {
        throttle_note($pdo, 'student');
        fail('badcode', 404);
    }
    login_as($pdo, 'student', $s, 'link');
    json_out(['ok' => true, 'role' => 'student']);

// ---- журнал действий (пакетом) ----------------------------------------------
case 'log':
    $b = body();
    $role = ($b['role'] ?? '') === 'teacher' ? 'teacher' : 'student';
    $u = current_user($pdo, $role);
    if (!$u) {
        json_out(['ok' => false, 'error' => 'auth']);
    }
    $uid = (int)$u['id'];
    $tid = $role === 'teacher' ? $uid : (int)$u['teacher_id'];
    if (consent_missing($pdo, $role, $uid)) {
        json_out(['ok' => false, 'error' => 'consent']);
    }
    $c0 = ctx($b);
    $c = $c0;
    $evs = is_array($b['ev'] ?? null) ? array_slice($b['ev'], 0, 60) : [];
    $liveEx = null;
    $sec = 0;
    $pages = 0;
    foreach ($evs as $e) {
        if (!is_array($e)) {
            continue;
        }
        $type = (string)($e['t'] ?? '');
        $ex = preg_match('/^[A-Za-z0-9_.:-]{1,60}$/', (string)($e['ex'] ?? '')) ? (string)$e['ex'] : null;
        // в домашней работе задания собраны с разных страниц: модуль и страница — у самого события
        $c = $c0;
        foreach (['c' => 'course', 'u' => 'unit', 'p' => 'page'] as $k => $f) {
            if (isset($e[$k]) && preg_match($ID, (string)$e[$k])) {
                $c[$f] = (string)$e[$k];
            }
        }
        $hw = null;
        if ($role === 'student' && !empty($e['hw'])) {
            $hs = $pdo->prepare('SELECT hw_id FROM en_hw_student WHERE hw_id = ? AND student_id = ? AND submitted_at IS NULL');
            $hs->execute([(int)$e['hw'], $uid]);
            $hw = $hs->fetchColumn() ? (int)$e['hw'] : null;
        }
        switch ($type) {
        case 'tick':
            $sec += max(0, min(60, (int)($e['sec'] ?? 0)));
            break;
        case 'view':
            $pages++;
            log_event($pdo, $role, $uid, $tid, 'view', ['course' => $c['course'] ?: null, 'page' => $c['path'],
                'data' => ['title' => mb_substr((string)($e['title'] ?? ''), 0, 160)]]);
            break;
        case 'check':
        case 'show':
            if ($role !== 'student' || !$ex || $c['course'] === '') {
                break;
            }
            $total = max(0, min(500, (int)($e['n'] ?? 0)));
            $score = $type === 'check' ? max(0, min($total, (int)($e['s'] ?? 0))) : 0;
            $items = [];
            foreach (array_slice(is_array($e['items'] ?? null) ? $e['items'] : [], 0, 500) as $it) {
                $items[] = ['v' => mb_substr((string)($it['v'] ?? ''), 0, 500), 'ok' => !empty($it['ok']),
                    'e' => mb_substr((string)($it['e'] ?? ''), 0, 500)];
            }
            $state = isset($e['st']) ? mb_substr(json_encode($e['st'], JSON_UNESCAPED_UNICODE), 0, 20000) : null;
            $pdo->prepare('INSERT INTO en_attempt (student_id, teacher_id, course, unit, page, ex, kind, score, total, answers, created_at, hw_id)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
                ->execute([$uid, $tid, $c['course'], $c['unit'], $c['page'], $ex, $type, $score, $total,
                    json_encode(['i' => $items, 'st' => isset($e['st']) ? $e['st'] : null, 'auto' => !empty($e['auto'])], JSON_UNESCAPED_UNICODE), now(), $hw]);
            $liveEx = $ex;
            if ($type === 'check') {
                $pdo->prepare('INSERT INTO en_progress (student_id, course, ex, unit, page, best, last, total, attempts, shown, state, first_at, updated_at)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1, 0, ?, ?, ?)
                               ON DUPLICATE KEY UPDATE best = GREATEST(best, VALUES(best)), last = VALUES(last), total = VALUES(total),
                               attempts = attempts + 1, state = VALUES(state), updated_at = VALUES(updated_at)')
                    ->execute([$uid, $c['course'], $ex, $c['unit'], $c['page'], $score, $score, $total, $state, now(), now()]);
            } else {
                $pdo->prepare('INSERT INTO en_progress (student_id, course, ex, unit, page, best, last, total, attempts, shown, state, first_at, updated_at)
                               VALUES (?, ?, ?, ?, ?, 0, 0, ?, 0, 1, ?, ?, ?)
                               ON DUPLICATE KEY UPDATE shown = 1, state = VALUES(state), updated_at = VALUES(updated_at)')
                    ->execute([$uid, $c['course'], $ex, $c['unit'], $c['page'], $total, $state, now(), now()]);
            }
            log_event($pdo, $role, $uid, $tid, $type, ['course' => $c['course'], 'page' => $c['path'], 'ex' => $ex,
                'data' => ($type === 'check' ? ['s' => $score, 'n' => $total] : ['n' => $total, 'auto' => !empty($e['auto'])]) + ($hw ? ['hw' => $hw] : [])]);
            break;
        case 'draft':   // ответы, которые ученик вводит, ещё не проверив: преподаватель видит их при разборе онлайн
            if ($role !== 'student' || !$ex || $c['course'] === '') {
                break;
            }
            $state = mb_substr(json_encode($e['st'] ?? null, JSON_UNESCAPED_UNICODE), 0, 20000);
            $pdo->prepare('INSERT INTO en_progress (student_id, course, ex, unit, page, best, last, total, attempts, shown, state, first_at, updated_at)
                           VALUES (?, ?, ?, ?, ?, 0, 0, ?, 0, 0, ?, ?, ?)
                           ON DUPLICATE KEY UPDATE state = VALUES(state), updated_at = VALUES(updated_at)')
                ->execute([$uid, $c['course'], $ex, $c['unit'], $c['page'], max(0, min(500, (int)($e['n'] ?? 0))), $state, now(), now()]);
            $liveEx = $ex;
            break;
        case 'focus':
            if ($ex) {
                $liveEx = $ex;
            }
            break;
        case 'reset':
            if ($role === 'student' && $ex) {
                $pdo->prepare('UPDATE en_progress SET state = NULL, updated_at = ? WHERE student_id = ? AND course = ? AND ex = ?')
                    ->execute([now(), $uid, $c['course'], $ex]);
                log_event($pdo, $role, $uid, $tid, 'reset', ['course' => $c['course'], 'page' => $c['path'], 'ex' => $ex]);
            }
            break;
        case 'write':
            $wid = preg_match('/^[A-Za-z0-9_.-]{1,60}$/', (string)($e['wid'] ?? '')) ? (string)$e['wid'] : '';
            if ($role !== 'student' || $wid === '' || $c['course'] === '') {
                break;
            }
            $text = mb_substr((string)($e['text'] ?? ''), 0, 20000);
            $words = preg_match_all("/[A-Za-z0-9’']+/u", $text);
            $prev = $pdo->prepare('SELECT words, updated_at FROM en_writing WHERE student_id = ? AND course = ? AND wid = ?');
            $prev->execute([$uid, $c['course'], $wid]);
            $pr = $prev->fetch();
            $pdo->prepare('REPLACE INTO en_writing (student_id, course, wid, page, text, words, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)')
                ->execute([$uid, $c['course'], $wid, $c['path'], $text, $words, now()]);
            // в журнал — не чаще раза в 10 минут на текст (сам текст — в en_writing)
            if (!$pr || strtotime($pr['updated_at']) < time() - 600) {
                log_event($pdo, $role, $uid, $tid, 'write', ['course' => $c['course'], 'page' => $c['path'], 'ex' => $wid,
                    'data' => ['words' => $words]]);
            }
            break;
        case 'audio':
        case 'reveal':
        case 'open':
            log_event($pdo, $role, $uid, $tid, $type, ['course' => $c['course'] ?: null, 'page' => $c['path'], 'ex' => $ex,
                'data' => ['what' => mb_substr((string)($e['what'] ?? ''), 0, 160)]]);
            break;
        }
    }
    if ($sec > 0 || $pages > 0) {
        visit_touch($pdo, $role, $uid, $tid, $sec, $pages);
    }
    $c = $c0;
    if ($role === 'student' && $c['path'] !== '' && empty($b['bg'])) {
        // «где ученик сейчас»: страница и задание (для режима разбора «Следовать за учеником»)
        // MySQL присваивает слева направо: live_ex считаем до смены live_path
        $pdo->prepare('UPDATE en_student SET live_ex = COALESCE(?, IF(live_path = ?, live_ex, NULL)), live_path = ?, live_at = ? WHERE id = ?')
            ->execute([$liveEx, $c['path'], $c['path'], now(), $uid]);
    }
    if (random_int(1, 500) === 1) {
        $pdo->exec('DELETE FROM en_event WHERE created_at < NOW() - INTERVAL ' . EN_EVENT_KEEP_DAYS . ' DAY');
    }
    json_out(['ok' => true]);

// ---- учитель: всё для кабинета ------------------------------------------------
case 't_data':
    $t = need_teacher($pdo);
    $tid = (int)$t['id'];
    $st = $pdo->prepare('SELECT id, name, email, token, code, telegram, avatar_at, created_at, first_login_at, last_seen_at, consent_at,
                                total_seconds, invited_at, live_path, live_ex, live_at, (live_at > NOW() - INTERVAL 150 SECOND) AS online
                         FROM en_student WHERE teacher_id = ? ORDER BY name');
    $st->execute([$tid]);
    $students = [];
    foreach ($st as $r) {
        $r['id'] = (int)$r['id'];
        $r['total_seconds'] = (int)$r['total_seconds'];
        $r['online'] = (bool)$r['online'];
        $r['link'] = student_link($r);
        $r['avatar'] = avatar_url('student', $r);
        unset($r['token'], $r['avatar_at']);
        $r['spaces'] = [];
        $students[$r['id']] = $r;
    }
    $st = $pdo->prepare('SELECT id, name, kind, course, sort, created_at FROM en_space WHERE teacher_id = ? ORDER BY sort, id');
    $st->execute([$tid]);
    $spaces = [];
    foreach ($st as $r) {
        $r['id'] = (int)$r['id'];
        $r['members'] = [];
        $spaces[$r['id']] = $r;
    }
    if ($spaces) {
        $in = implode(',', array_keys($spaces));
        foreach ($pdo->query("SELECT space_id, student_id FROM en_space_member WHERE space_id IN ($in) ORDER BY added_at") as $r) {
            $sid = (int)$r['student_id'];
            if (isset($students[$sid])) {
                $spaces[(int)$r['space_id']]['members'][] = $sid;
                $students[$sid]['spaces'][] = (int)$r['space_id'];
            }
        }
    }
    // прогресс: по ученику, курсу и модулю
    $st = $pdo->prepare('SELECT p.student_id, p.course, p.unit, COUNT(*) AS done, SUM(p.best) AS best, SUM(p.total) AS total,
                                SUM(p.attempts) AS attempts, MAX(p.updated_at) AS last_at
                         FROM en_progress p JOIN en_student s ON s.id = p.student_id
                         WHERE s.teacher_id = ? GROUP BY p.student_id, p.course, p.unit');
    $st->execute([$tid]);
    $prog = [];
    foreach ($st as $r) {
        $prog[] = ['sid' => (int)$r['student_id'], 'course' => $r['course'], 'unit' => $r['unit'], 'done' => (int)$r['done'],
            'best' => (int)$r['best'], 'total' => (int)$r['total'], 'attempts' => (int)$r['attempts'], 'last' => $r['last_at']];
    }
    json_out(['ok' => true, 'teacher' => ['id' => $tid, 'name' => $t['name'], 'email' => $t['email'], 'telegram' => $t['telegram']],
        'students' => array_values($students), 'spaces' => array_values($spaces), 'progress' => $prog, 'site' => site_url()]);

// ---- учитель: ученики ---------------------------------------------------------
case 't_student_add':
    $t = need_teacher($pdo);
    $b = body();
    $name = clean_text($b['name'] ?? '', 200);
    if ($name === '') {
        fail('name');
    }
    $email = clean_email($b['email'] ?? '');
    if (trim((string)($b['email'] ?? '')) !== '' && $email === null) {
        fail('email');
    }
    $cnt = $pdo->prepare('SELECT COUNT(*) FROM en_student WHERE teacher_id = ?');
    $cnt->execute([(int)$t['id']]);
    if ((int)$cnt->fetchColumn() >= 2000) {
        fail('limit');
    }
    $token = new_student_token($pdo);
    $code = new_code($pdo);
    $pdo->prepare('INSERT INTO en_student (teacher_id, name, email, token, code, created_at) VALUES (?, ?, ?, ?, ?, ?)')
        ->execute([(int)$t['id'], $name, $email, $token, $code, now()]);
    $sid = (int)$pdo->lastInsertId();
    if (!empty($b['space'])) {
        $sp = own_space($pdo, $t, $b['space']);
        $pdo->prepare('INSERT IGNORE INTO en_space_member (space_id, student_id, added_at) VALUES (?, ?, ?)')
            ->execute([(int)$sp['id'], $sid, now()]);
    }
    tlog($pdo, $t, 'student_add', ['student' => $sid, 'email' => $email !== null]);
    json_out(['ok' => true, 'id' => $sid, 'code' => $code, 'link' => student_link(['token' => $token])]);

case 't_student_update':
    $t = need_teacher($pdo);
    $b = body();
    $s = own_student($pdo, $t, $b['id'] ?? 0);
    $name = clean_text($b['name'] ?? $s['name'], 200);
    $email = clean_email($b['email'] ?? '');
    if (trim((string)($b['email'] ?? '')) !== '' && $email === null) {
        fail('email');
    }
    if ($name === '') {
        fail('name');
    }
    $pdo->prepare('UPDATE en_student SET name = ?, email = ? WHERE id = ?')->execute([$name, $email, $s['id']]);
    tlog($pdo, $t, 'student_edit', ['student' => (int)$s['id']]);
    json_out(['ok' => true]);

case 't_student_delete':
    $t = need_teacher($pdo);
    $s = own_student($pdo, $t, body()['id'] ?? 0);
    delete_student_data($pdo, (int)$s['id']);
    tlog($pdo, $t, 'student_delete', ['student' => (int)$s['id']]);
    json_out(['ok' => true]);

case 't_student_relink':
    $t = need_teacher($pdo);
    $s = own_student($pdo, $t, body()['id'] ?? 0);
    $token = new_student_token($pdo);
    $pdo->prepare('UPDATE en_student SET token = ?, code = ? WHERE id = ?')->execute([$token, new_code($pdo), $s['id']]);
    $pdo->prepare("DELETE FROM en_session WHERE role = 'student' AND user_id = ?")->execute([$s['id']]);
    tlog($pdo, $t, 'student_relink', ['student' => (int)$s['id']]);
    json_out(['ok' => true]);

case 't_student_mail':
    $t = need_teacher($pdo);
    $s = own_student($pdo, $t, body()['id'] ?? 0);
    if (empty($s['email'])) {
        fail('noemail');
    }
    $st = $pdo->prepare('SELECT COUNT(*) FROM en_mail WHERE teacher_id = ? AND created_at > NOW() - INTERVAL 1 DAY');
    $st->execute([(int)$t['id']]);
    if ((int)$st->fetchColumn() >= 200) {
        fail('maillimit', 429);
    }
    $link = student_link($s);
    $text = "Здравствуйте, {$s['name']}!\n\n"
        . "Ваш преподаватель {$t['name']} приглашает вас заниматься английским на платформе Lingvaden English (lingvaden.ru).\n\n"
        . "Ваша личная ссылка для входа:\n$link\n\n"
        . "Или откройте " . site_url() . " и введите ваш код: {$s['code']}\n\n"
        . "Сайт поприветствует вас по имени; в вашем кабинете — курсы и домашние работы, а преподаватель будет видеть ваши результаты.\n"
        . "Ссылка и код личные: не пересылайте их другим. Если вы их потеряли, попросите преподавателя прислать новые.\n\n"
        . "Как пользоваться и установить на телефон как приложение: " . site_url() . "/how/\n"
        . "Правовая информация и обработка данных: " . site_url() . "/legal/\n\n"
        . "Если вы не знаете, о чём речь, просто проигнорируйте это письмо.\n\n— Lingvaden English";
    $ok = send_mail((string)$s['email'], "{$t['name']} приглашает вас заниматься английским", $text);
    $pdo->prepare('INSERT INTO en_mail (teacher_id, student_id, kind, to_email, ok, created_at) VALUES (?, ?, ?, ?, ?, ?)')
        ->execute([(int)$t['id'], (int)$s['id'], 'invite', $s['email'], $ok ? 1 : 0, now()]);
    if ($ok) {
        $pdo->prepare('UPDATE en_student SET invited_at = ? WHERE id = ?')->execute([now(), $s['id']]);
    }
    tlog($pdo, $t, 'student_mail', ['student' => (int)$s['id'], 'ok' => $ok]);
    json_out(['ok' => $ok, 'error' => $ok ? null : 'mail']);

case 't_invited':  // отметка «ссылка отправлена» (Telegram, копирование, QR)
    $t = need_teacher($pdo);
    $b = body();
    $s = own_student($pdo, $t, $b['id'] ?? 0);
    $pdo->prepare('UPDATE en_student SET invited_at = ? WHERE id = ?')->execute([now(), $s['id']]);
    tlog($pdo, $t, 'student_share', ['student' => (int)$s['id'], 'via' => clean_text($b['via'] ?? '', 20)]);
    json_out(['ok' => true]);

// ---- учитель: пространства ----------------------------------------------------
case 't_space_add':
    $t = need_teacher($pdo);
    $b = body();
    $name = clean_text($b['name'] ?? '', 120);
    $kind = in_array($b['kind'] ?? '', ['class', 'group', 'marathon', 'other'], true) ? $b['kind'] : 'group';
    if ($name === '') {
        fail('name');
    }
    $course = preg_match($ID, (string)($b['course'] ?? '')) ? (string)$b['course'] : null;
    $mx = $pdo->prepare('SELECT IFNULL(MAX(sort), 0) + 1 FROM en_space WHERE teacher_id = ?');
    $mx->execute([(int)$t['id']]);
    $pdo->prepare('INSERT INTO en_space (teacher_id, name, kind, course, sort, created_at) VALUES (?, ?, ?, ?, ?, ?)')
        ->execute([(int)$t['id'], $name, $kind, $course, (int)$mx->fetchColumn(), now()]);
    $id = (int)$pdo->lastInsertId();
    tlog($pdo, $t, 'space_add', ['space' => $id, 'kind' => $kind]);
    json_out(['ok' => true, 'id' => $id]);

case 't_space_update':
    $t = need_teacher($pdo);
    $b = body();
    $sp = own_space($pdo, $t, $b['id'] ?? 0);
    $name = clean_text($b['name'] ?? $sp['name'], 120);
    $kind = in_array($b['kind'] ?? '', ['class', 'group', 'marathon', 'other'], true) ? $b['kind'] : $sp['kind'];
    $course = array_key_exists('course', $b) ? (preg_match($ID, (string)$b['course']) ? (string)$b['course'] : null) : $sp['course'];
    if ($name === '') {
        fail('name');
    }
    $pdo->prepare('UPDATE en_space SET name = ?, kind = ?, course = ? WHERE id = ?')->execute([$name, $kind, $course, $sp['id']]);
    tlog($pdo, $t, 'space_edit', ['space' => (int)$sp['id']]);
    json_out(['ok' => true]);

case 't_space_delete':
    $t = need_teacher($pdo);
    $sp = own_space($pdo, $t, body()['id'] ?? 0);
    $pdo->prepare('DELETE FROM en_space_member WHERE space_id = ?')->execute([$sp['id']]);
    $pdo->prepare('DELETE FROM en_space WHERE id = ?')->execute([$sp['id']]);
    tlog($pdo, $t, 'space_delete', ['space' => (int)$sp['id']]);
    json_out(['ok' => true]);

case 't_member':
    $t = need_teacher($pdo);
    $b = body();
    $sp = own_space($pdo, $t, $b['space'] ?? 0);
    $s = own_student($pdo, $t, $b['student'] ?? 0);
    if (!empty($b['on'])) {
        $pdo->prepare('INSERT IGNORE INTO en_space_member (space_id, student_id, added_at) VALUES (?, ?, ?)')
            ->execute([(int)$sp['id'], (int)$s['id'], now()]);
    } else {
        $pdo->prepare('DELETE FROM en_space_member WHERE space_id = ? AND student_id = ?')->execute([(int)$sp['id'], (int)$s['id']]);
    }
    tlog($pdo, $t, !empty($b['on']) ? 'member_add' : 'member_remove', ['space' => (int)$sp['id'], 'student' => (int)$s['id']]);
    json_out(['ok' => true]);

// ---- учитель: всё по одному ученику -------------------------------------------
case 't_student':
    $t = need_teacher($pdo);
    $s = own_student($pdo, $t, $_GET['id'] ?? 0);
    $sid = (int)$s['id'];
    $q = function (string $sql, array $p) use ($pdo) {
        $st = $pdo->prepare($sql);
        $st->execute($p);
        return $st->fetchAll();
    };
    $progress = $q('SELECT course, unit, page, ex, best, last, total, attempts, shown, first_at, updated_at
                    FROM en_progress WHERE student_id = ? ORDER BY updated_at DESC', [$sid]);
    $attempts = $q('SELECT id, course, unit, page, ex, kind, score, total, answers, created_at
                    FROM en_attempt WHERE student_id = ? ORDER BY id DESC LIMIT 3000', [$sid]);
    foreach ($attempts as &$r) {
        $a = json_decode((string)$r['answers'], true);
        $r['answers'] = isset($a['i']) ? $a['i'] : (is_array($a) ? $a : []);
    }
    unset($r);
    $visits = $q("SELECT started_at, last_at, seconds, pages, device FROM en_visit WHERE role = 'student' AND user_id = ?
                  ORDER BY id DESC LIMIT 300", [$sid]);
    $events = $q("SELECT type, course, page, ex, data, created_at FROM en_event WHERE role = 'student' AND user_id = ?
                  ORDER BY id DESC LIMIT 1500", [$sid]);
    foreach ($events as &$r) {
        $r['data'] = $r['data'] !== null ? json_decode($r['data'], true) : null;
    }
    unset($r);
    $writings = $q('SELECT course, wid, page, text, words, updated_at FROM en_writing WHERE student_id = ? ORDER BY updated_at DESC', [$sid]);
    tlog($pdo, $t, 'student_view', ['student' => $sid]);
    unset($s['token']);
    json_out(['ok' => true, 'student' => $s, 'progress' => $progress, 'attempts' => $attempts, 'visits' => $visits,
        'events' => $events, 'writings' => $writings]);

// ---- учитель: рабочее место разбора — всё по одной странице курса -----------------
case 't_review':
    $t = need_teacher($pdo);
    $s = own_student($pdo, $t, $_GET['id'] ?? 0);
    $sid = (int)$s['id'];
    $unit = preg_match($ID, (string)($_GET['unit'] ?? '')) ? (string)$_GET['unit'] : '';
    $page = preg_match($ID, (string)($_GET['page'] ?? '')) ? (string)$_GET['page'] : '';
    $course = preg_match($ID, (string)($_GET['course'] ?? '')) ? (string)$_GET['course'] : '';
    $st = $pdo->prepare('SELECT ex, best, last, total, attempts, shown, state, updated_at FROM en_progress
                         WHERE student_id = ? AND course = ? AND unit = ? AND page = ?');
    $st->execute([$sid, $course, $unit, $page]);
    $prog = [];
    foreach ($st as $r) {
        $r['state'] = $r['state'] !== null ? json_decode($r['state'], true) : null;
        $prog[$r['ex']] = $r;
    }
    $st = $pdo->prepare('SELECT id, ex, kind, score, total, answers, created_at FROM en_attempt
                         WHERE student_id = ? AND course = ? AND unit = ? AND page = ? ORDER BY id');
    $st->execute([$sid, $course, $unit, $page]);
    $att = [];
    foreach ($st as $r) {
        $a = json_decode((string)$r['answers'], true);
        $r['items'] = isset($a['i']) ? $a['i'] : (is_array($a) ? $a : []);
        $r['st'] = isset($a['st']) ? $a['st'] : null;
        unset($r['answers']);
        $att[$r['ex']][] = $r;
    }
    $st = $pdo->prepare('SELECT wid, text, words, updated_at FROM en_writing WHERE student_id = ? AND course = ? AND page LIKE ?');
    $st->execute([$sid, $course, '%/' . $unit . '/%']);
    $w = [];
    foreach ($st as $r) {
        $w[$r['wid']] = $r;
    }
    if (empty($_GET['poll'])) {
        tlog($pdo, $t, 'student_review', ['student' => $sid, 'unit' => $unit, 'page' => $page]);
    }
    json_out(['ok' => true, 'student' => ['id' => $sid, 'name' => $s['name']], 'progress' => $prog, 'attempts' => $att, 'writings' => $w,
        'live' => ['path' => $s['live_path'], 'ex' => $s['live_ex'], 'at' => $s['live_at'],
            'online' => $s['live_at'] !== null && strtotime($s['live_at']) > time() - 150], 'now' => now()]);

// ---- учитель: домашние работы ---------------------------------------------------
case 't_hw_add':
    $t = need_teacher($pdo);
    $b = body();
    $title = clean_text($b['title'] ?? '', 200);
    if ($title === '') {
        fail('title');
    }
    $course = preg_match($ID, (string)($b['course'] ?? '')) ? (string)$b['course'] : '';
    $items = [];
    foreach (array_slice(is_array($b['items'] ?? null) ? $b['items'] : [], 0, 200) as $it) {
        if (!is_array($it) || !preg_match('/^[A-Za-z0-9_.:-]{1,60}$/', (string)($it['ex'] ?? ''))
            || !preg_match($ID, (string)($it['unit'] ?? '')) || !preg_match($ID, (string)($it['page'] ?? ''))) {
            continue;
        }
        $items[] = ['ex' => (string)$it['ex'], 'n' => max(1, min(500, (int)($it['n'] ?? 1))), 'unit' => (string)$it['unit'], 'page' => (string)$it['page']];
    }
    if (!$items || $course === '') {
        fail('items');
    }
    // кому: ученики и все ученики выбранных пространств
    $sids = [];
    $spaces = [];
    foreach (array_slice(is_array($b['spaces'] ?? null) ? $b['spaces'] : [], 0, 100) as $x) {
        $sp = own_space($pdo, $t, $x);
        $spaces[] = (int)$sp['id'];
        $st = $pdo->prepare('SELECT student_id FROM en_space_member WHERE space_id = ?');
        $st->execute([(int)$sp['id']]);
        foreach ($st->fetchAll(PDO::FETCH_COLUMN) as $sid) {
            $sids[(int)$sid] = true;
        }
    }
    $direct = [];
    foreach (array_slice(is_array($b['students'] ?? null) ? $b['students'] : [], 0, 2000) as $x) {
        $s = own_student($pdo, $t, $x);
        $direct[] = (int)$s['id'];
        $sids[(int)$s['id']] = true;
    }
    if (!$sids) {
        fail('nobody');
    }
    $due = preg_match('/^\d{4}-\d{2}-\d{2}$/', (string)($b['due'] ?? '')) ? $b['due'] . ' 23:59:59' : null;
    $pdo->prepare('INSERT INTO en_hw (teacher_id, title, note, course, items, due_at, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)')
        ->execute([(int)$t['id'], $title, mb_substr(trim((string)($b['note'] ?? '')), 0, 4000) ?: null, $course,
            json_encode($items, JSON_UNESCAPED_UNICODE), $due, now()]);
    $hid = (int)$pdo->lastInsertId();
    $tg = $pdo->prepare('INSERT IGNORE INTO en_hw_target (hw_id, kind, ref_id) VALUES (?, ?, ?)');
    foreach ($spaces as $x) {
        $tg->execute([$hid, 'space', $x]);
    }
    foreach ($direct as $x) {
        $tg->execute([$hid, 'student', $x]);
    }
    $hs = $pdo->prepare('INSERT IGNORE INTO en_hw_student (hw_id, student_id, assigned_at) VALUES (?, ?, ?)');
    foreach (array_keys($sids) as $sid) {
        $hs->execute([$hid, $sid, now()]);
    }
    tlog($pdo, $t, 'hw_add', ['hw' => $hid, 'students' => count($sids), 'items' => count($items)]);
    json_out(['ok' => true, 'id' => $hid, 'students' => count($sids)]);

case 't_hw_archive':
    $t = need_teacher($pdo);
    $b = body();
    $st = $pdo->prepare('SELECT id FROM en_hw WHERE id = ? AND teacher_id = ?');
    $st->execute([(int)($b['id'] ?? 0), (int)$t['id']]);
    $hid = (int)$st->fetchColumn();
    if (!$hid) {
        fail('notfound', 404);
    }
    $pdo->prepare('UPDATE en_hw SET archived_at = ? WHERE id = ?')->execute([!empty($b['on']) ? now() : null, $hid]);
    tlog($pdo, $t, 'hw_archive', ['hw' => $hid, 'on' => !empty($b['on'])]);
    json_out(['ok' => true]);

case 't_hw_list':
    $t = need_teacher($pdo);
    $st = $pdo->prepare('SELECT id, title, note, course, items, due_at, created_at, archived_at FROM en_hw WHERE teacher_id = ? ORDER BY id DESC LIMIT 500');
    $st->execute([(int)$t['id']]);
    $hws = [];
    foreach ($st as $r) {
        $r['id'] = (int)$r['id'];
        $r['items'] = hw_items($r);
        $r['targets'] = [];
        $r['students'] = [];
        $hws[$r['id']] = $r;
    }
    if ($hws) {
        $in = implode(',', array_keys($hws));
        foreach ($pdo->query("SELECT hw_id, kind, ref_id FROM en_hw_target WHERE hw_id IN ($in)") as $r) {
            $hws[(int)$r['hw_id']]['targets'][] = [$r['kind'], (int)$r['ref_id']];
        }
        // попытки по домашней работе: число проверок у каждого ученика
        $cnt = [];
        foreach ($pdo->query("SELECT hw_id, student_id, COUNT(*) AS n FROM en_attempt WHERE hw_id IN ($in) AND kind = 'check' GROUP BY hw_id, student_id") as $r) {
            $cnt[$r['hw_id'] . ':' . $r['student_id']] = (int)$r['n'];
        }
        foreach ($pdo->query("SELECT hw_id, student_id, assigned_at, opened_at, submitted_at, seen_at, score, total FROM en_hw_student WHERE hw_id IN ($in)") as $r) {
            $r['sid'] = (int)$r['student_id'];
            unset($r['student_id']);
            $r['checks'] = $cnt[$r['hw_id'] . ':' . $r['sid']] ?? 0;
            $hws[(int)$r['hw_id']]['students'][] = $r;
        }
    }
    json_out(['ok' => true, 'hw' => array_values($hws)]);

case 't_hw_result':   // что ученик сделал в домашней работе: по заданиям — все попытки
    $t = need_teacher($pdo);
    $st = $pdo->prepare('SELECT * FROM en_hw WHERE id = ? AND teacher_id = ?');
    $st->execute([(int)($_GET['hw'] ?? 0), (int)$t['id']]);
    $hw = $st->fetch();
    if (!$hw) {
        fail('notfound', 404);
    }
    $s = own_student($pdo, $t, $_GET['sid'] ?? 0);
    $st = $pdo->prepare('SELECT * FROM en_hw_student WHERE hw_id = ? AND student_id = ?');
    $st->execute([(int)$hw['id'], (int)$s['id']]);
    $hs = $st->fetch();
    if (!$hs) {
        fail('notfound', 404);
    }
    $st = $pdo->prepare('SELECT id, ex, kind, score, total, answers, created_at FROM en_attempt WHERE hw_id = ? AND student_id = ? ORDER BY id');
    $st->execute([(int)$hw['id'], (int)$s['id']]);
    $att = [];
    foreach ($st as $r) {
        $a = json_decode((string)$r['answers'], true);
        $r['items'] = isset($a['i']) ? $a['i'] : [];
        $r['st'] = isset($a['st']) ? $a['st'] : null;   // состояние полей — чтобы показать попытку прямо в задании
        $r['auto'] = !empty($a['auto']);
        unset($r['answers']);
        $att[$r['ex']][] = $r;
    }
    if ($hs['submitted_at'] && !$hs['seen_at']) {
        $pdo->prepare('UPDATE en_hw_student SET seen_at = ? WHERE hw_id = ? AND student_id = ?')->execute([now(), (int)$hw['id'], (int)$s['id']]);
    }
    tlog($pdo, $t, 'hw_view', ['hw' => (int)$hw['id'], 'student' => (int)$s['id']]);
    $hw['items'] = hw_items($hw);
    json_out(['ok' => true, 'hw' => $hw, 'student' => ['id' => (int)$s['id'], 'name' => $s['name']], 'status' => $hs, 'attempts' => $att]);

// ---- ученик: домашние работы ------------------------------------------------------
case 's_hw_list':
    $s = need_student($pdo);
    $st = $pdo->prepare('SELECT h.id, h.title, h.note, h.course, h.items, h.due_at, h.created_at, hs.opened_at, hs.submitted_at, hs.score, hs.total
                         FROM en_hw_student hs JOIN en_hw h ON h.id = hs.hw_id AND h.archived_at IS NULL
                         WHERE hs.student_id = ? ORDER BY (hs.submitted_at IS NULL) DESC, h.id DESC');
    $st->execute([(int)$s['id']]);
    $out = [];
    foreach ($st as $r) {
        $r['id'] = (int)$r['id'];
        $r['n'] = count(hw_items($r));
        unset($r['items']);
        $out[] = $r;
    }
    json_out(['ok' => true, 'hw' => $out]);

case 's_hw':
    $s = need_student($pdo);
    $st = $pdo->prepare('SELECT h.*, hs.opened_at, hs.submitted_at, hs.score, hs.total FROM en_hw_student hs
                         JOIN en_hw h ON h.id = hs.hw_id WHERE hs.hw_id = ? AND hs.student_id = ?');
    $st->execute([(int)($_GET['id'] ?? 0), (int)$s['id']]);
    $hw = $st->fetch();
    if (!$hw) {
        fail('notfound', 404);
    }
    if (!$hw['opened_at']) {
        $pdo->prepare('UPDATE en_hw_student SET opened_at = ? WHERE hw_id = ? AND student_id = ?')->execute([now(), (int)$hw['id'], (int)$s['id']]);
        log_event($pdo, 'student', (int)$s['id'], (int)$s['teacher_id'], 'hw_open', ['data' => ['hw' => (int)$hw['id']]]);
    }
    // последнее состояние каждого задания и число неверных проверок — для другого устройства
    $st = $pdo->prepare('SELECT ex, kind, score, total, answers FROM en_attempt WHERE hw_id = ? AND student_id = ? ORDER BY id');
    $st->execute([(int)$hw['id'], (int)$s['id']]);
    $last = [];
    foreach ($st as $r) {
        $a = json_decode((string)$r['answers'], true);
        $x = $last[$r['ex']] ?? ['fails' => 0, 'checks' => 0];
        if ($r['kind'] === 'check') {
            $x['checks']++;
            if ((int)$r['score'] < (int)$r['total']) {
                $x['fails']++;
            }
            $x['s'] = (int)$r['score'];
            $x['t'] = (int)$r['total'];
        }
        if (isset($a['st'])) {
            $x['st'] = $a['st'];
        }
        $last[$r['ex']] = $x;
    }
    $hw['items'] = hw_items($hw);
    unset($hw['teacher_id']);
    json_out(['ok' => true, 'hw' => $hw, 'last' => (object)$last]);

case 's_hw_submit':
    $s = need_student($pdo);
    $hid = (int)(body()['id'] ?? 0);
    $st = $pdo->prepare('SELECT h.items, hs.submitted_at FROM en_hw_student hs JOIN en_hw h ON h.id = hs.hw_id WHERE hs.hw_id = ? AND hs.student_id = ?');
    $st->execute([$hid, (int)$s['id']]);
    $r = $st->fetch();
    if (!$r) {
        fail('notfound', 404);
    }
    if ($r['submitted_at']) {
        fail('submitted');
    }
    // итог: последняя проверка каждого задания
    $score = 0;
    $total = 0;
    $q = $pdo->prepare("SELECT score FROM en_attempt WHERE hw_id = ? AND student_id = ? AND ex = ? AND kind = 'check' ORDER BY id DESC LIMIT 1");
    foreach (hw_items($r) as $it) {
        $total += (int)$it['n'];
        $q->execute([$hid, (int)$s['id'], $it['ex']]);
        $score += min((int)$it['n'], (int)$q->fetchColumn());
    }
    $pdo->prepare('UPDATE en_hw_student SET submitted_at = ?, score = ?, total = ? WHERE hw_id = ? AND student_id = ?')
        ->execute([now(), $score, $total, $hid, (int)$s['id']]);
    log_event($pdo, 'student', (int)$s['id'], (int)$s['teacher_id'], 'hw_submit', ['data' => ['hw' => $hid, 's' => $score, 'n' => $total]]);
    json_out(['ok' => true, 'score' => $score, 'total' => $total]);

default:
    fail('action', 404);
}
