<?php
/**
 * Вход ученика по личной ссылке: lingvaden.ru/s/<код> (правило в .htaccess) → сюда.
 * Преподавателя — по lingvaden.ru/t/<код> (r=t): кабинет преподавателя, вход ученика заканчивается.
 * Ставит cookie входа (вход учителя на этом устройстве заканчивается) и ведёт в кабинет ученика,
 * где сайт приветствует его по имени (при первом входе — сначала согласия).
 */

declare(strict_types=1);
require __DIR__ . '/_lib.php';

header('Cache-Control: no-store');
header('Referrer-Policy: no-referrer');
header('X-Robots-Tag: noindex, nofollow');

$token = strtolower((string)($_GET['t'] ?? ''));
try {
    $pdo = en_db();
} catch (Throwable $e) {
    header('Location: /?err=db', true, 303);
    exit;
}
if (throttle_wait($pdo, 'student')) {
    header('Location: /?err=wait', true, 303);
    exit;
}
if (($_GET['r'] ?? '') === 't') {
    $t = null;
    if (preg_match('/^[a-z0-9]{6,16}$/', $token)) {
        $st = $pdo->prepare("SELECT * FROM en_teacher WHERE token = ? AND status = 'active'");
        $st->execute([$token]);
        $t = $st->fetch() ?: null;
    }
    if (!$t) {
        throttle_note($pdo, 'student');
        header('Location: /?err=bad', true, 303);
        exit;
    }
    if (!empty($_COOKIE[cookie_name('student')])) {
        session_end($pdo, 'student');
    }
    $cur = current_user($pdo, 'teacher');
    if (!$cur || (int)$cur['id'] !== (int)$t['id']) {
        session_start_for($pdo, 'teacher', (int)$t['id']);
    }
    $pdo->prepare('UPDATE en_teacher SET last_login_at = ? WHERE id = ?')->execute([now(), $t['id']]);
    log_event($pdo, 'teacher', (int)$t['id'], (int)$t['id'], 'login', ['data' => ['via' => 'link', 'device' => device()]]);
    header('Location: /teacher/', true, 303);
    exit;
}
$st = $pdo->prepare("SELECT s.* FROM en_student s JOIN en_teacher t ON t.id = s.teacher_id AND t.status = 'active' WHERE s.token = ?");
$st->execute([$token]);
$s = preg_match('/^[a-z0-9]{6,16}$/', $token) ? $st->fetch() : null;
if (!$s) {
    throttle_note($pdo, 'student');
    header('Location: /?err=bad', true, 303);
    exit;
}
// тот же ученик уже вошёл на этом устройстве — новую сессию не плодим
if (!empty($_COOKIE[cookie_name('teacher')])) {
    session_end($pdo, 'teacher');
}
$cur = current_user($pdo, 'student');
if (!$cur || (int)$cur['id'] !== (int)$s['id']) {
    session_start_for($pdo, 'student', (int)$s['id']);
}
$pdo->prepare('UPDATE en_student SET first_login_at = COALESCE(first_login_at, ?) WHERE id = ?')->execute([now(), $s['id']]);
log_event($pdo, 'student', (int)$s['id'], (int)$s['teacher_id'], 'login', ['data' => ['via' => 'link', 'device' => device()]]);
header('Location: /me/?hello=1', true, 303);
