<?php
/**
 * Общая часть платформы lingvaden.ru: конфиг, БД, схема, сессии, утилиты.
 *
 * Совместимость: PHP 7.2+ (сайт — 7.3, CLI хостинга — 7.2): без fn(), ??=, match, str_contains.
 * Конфиг с паролем БД лежит ВНЕ www: ~/lingvaden.ru/english_config.php
 * (локально — путь в переменной окружения EN_CONFIG).
 */

declare(strict_types=1);

ini_set('display_errors', '0');
ini_set('log_errors', '1');
date_default_timezone_set('Europe/Moscow');

const EN_SCHEMA_VERSION = 5;
const EN_DOCS = [
    // документ => версия; при изменении текста документа поднять версию — согласие спросят заново
    'terms' => '1.2',
    'privacy' => '1.2',
    'cookies' => '1.2',
    'teacher_terms' => '1.2',
    'student_consent' => '1.2',
];
const EN_STUDENT_DAYS = 180;   // срок жизни входа ученика (cookie)
const EN_TEACHER_DAYS = 30;    // срок жизни входа учителя
const EN_EVENT_KEEP_DAYS = 730; // журнал событий — 2 года

function en_config(): array
{
    static $c = null;
    if ($c !== null) {
        return $c;
    }
    $p = getenv('EN_CONFIG');
    if (!$p) {
        $p = dirname(__DIR__, 3) . '/english_config.php';
        if (!is_readable($p)) {
            $p = dirname(__DIR__, 2) . '/english_config.php';
        }
    }
    $c = is_readable($p) ? require $p : [];
    if (!is_array($c)) {
        $c = [];
    }
    return $c;
}

function en_db(): PDO
{
    static $pdo = null;
    if ($pdo) {
        return $pdo;
    }
    $c = en_config();
    if (empty($c['db_name'])) {
        throw new RuntimeException('noconfig');
    }
    $pdo = new PDO(
        sprintf('mysql:host=%s;dbname=%s;charset=utf8mb4', $c['db_host'], $c['db_name']),
        (string)$c['db_user'], (string)$c['db_pass'],
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
         PDO::ATTR_EMULATE_PREPARES => false, PDO::ATTR_TIMEOUT => 5]
    );
    $pdo->exec("SET NAMES utf8mb4, time_zone = '+03:00'");
    en_schema($pdo);
    return $pdo;
}

/** Таблицы создаются сами при первом запросе; версия схемы — в en_meta. */
function en_schema(PDO $pdo): void
{
    try {
        $v = (int)$pdo->query("SELECT v FROM en_meta WHERE k = 'schema'")->fetchColumn();
        if ($v >= EN_SCHEMA_VERSION) {
            return;
        }
    } catch (Throwable $e) {
    }
    $T = ' ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci';
    $sql = [
        "CREATE TABLE IF NOT EXISTS en_meta (k VARCHAR(40) PRIMARY KEY, v TEXT NOT NULL)$T",
        // учителя заводит владелец в админке lingvaden.ru (раздел English → Учителя)
        "CREATE TABLE IF NOT EXISTS en_teacher (
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(200) NOT NULL,
            email VARCHAR(190) NULL,
            code CHAR(6) NOT NULL,
            status ENUM('active','blocked') NOT NULL DEFAULT 'active',
            note VARCHAR(255) NULL,
            created_at DATETIME NOT NULL,
            last_login_at DATETIME NULL,
            last_seen_at DATETIME NULL,
            consent_at DATETIME NULL,
            total_seconds INT UNSIGNED NOT NULL DEFAULT 0,
            UNIQUE KEY uq_code (code)
        )$T",
        "CREATE TABLE IF NOT EXISTS en_student (
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            teacher_id INT UNSIGNED NOT NULL,
            name VARCHAR(200) NOT NULL,
            email VARCHAR(190) NULL,
            token VARCHAR(16) NOT NULL,
            created_at DATETIME NOT NULL,
            first_login_at DATETIME NULL,
            last_seen_at DATETIME NULL,
            consent_at DATETIME NULL,
            total_seconds INT UNSIGNED NOT NULL DEFAULT 0,
            invited_at DATETIME NULL,
            UNIQUE KEY uq_token (token),
            KEY idx_teacher (teacher_id, id)
        )$T",
        // пространства учителя: класс, группа, марафон
        "CREATE TABLE IF NOT EXISTS en_space (
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            teacher_id INT UNSIGNED NOT NULL,
            name VARCHAR(120) NOT NULL,
            kind ENUM('class','group','marathon','other') NOT NULL DEFAULT 'group',
            course VARCHAR(40) NULL,
            sort INT NOT NULL DEFAULT 0,
            created_at DATETIME NOT NULL,
            KEY idx_teacher (teacher_id, sort)
        )$T",
        "CREATE TABLE IF NOT EXISTS en_space_member (
            space_id INT UNSIGNED NOT NULL,
            student_id INT UNSIGNED NOT NULL,
            added_at DATETIME NOT NULL,
            PRIMARY KEY (space_id, student_id),
            KEY idx_student (student_id)
        )$T",
        "CREATE TABLE IF NOT EXISTS en_session (
            id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            token_hash CHAR(64) NOT NULL,
            role ENUM('teacher','student') NOT NULL,
            user_id INT UNSIGNED NOT NULL,
            created_at DATETIME NOT NULL,
            last_seen_at DATETIME NOT NULL,
            expires_at DATETIME NOT NULL,
            user_agent VARCHAR(255) NULL,
            UNIQUE KEY uq_token (token_hash),
            KEY idx_user (role, user_id)
        )$T",
        // «визит» — непрерывная работа; разрыв больше 30 минут начинает новый
        "CREATE TABLE IF NOT EXISTS en_visit (
            id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            role ENUM('teacher','student') NOT NULL,
            user_id INT UNSIGNED NOT NULL,
            teacher_id INT UNSIGNED NOT NULL,
            started_at DATETIME NOT NULL,
            last_at DATETIME NOT NULL,
            seconds INT UNSIGNED NOT NULL DEFAULT 0,
            pages INT UNSIGNED NOT NULL DEFAULT 0,
            device VARCHAR(16) NULL,
            KEY idx_user (role, user_id, last_at),
            KEY idx_teacher (teacher_id, started_at),
            KEY idx_started (started_at)
        )$T",
        // журнал всех действий (входы, страницы, проверки, письмо, аудио, действия учителя)
        "CREATE TABLE IF NOT EXISTS en_event (
            id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            role ENUM('teacher','student','admin','system') NOT NULL,
            user_id INT UNSIGNED NOT NULL,
            teacher_id INT UNSIGNED NOT NULL,
            type VARCHAR(32) NOT NULL,
            course VARCHAR(40) NULL,
            page VARCHAR(160) NULL,
            ex VARCHAR(60) NULL,
            data TEXT NULL,
            created_at DATETIME NOT NULL,
            KEY idx_user (role, user_id, id),
            KEY idx_teacher (teacher_id, id),
            KEY idx_created (created_at),
            KEY idx_type (type, created_at)
        )$T",
        // каждая проверка задания — отдельная запись: история всех вариантов ответа
        "CREATE TABLE IF NOT EXISTS en_attempt (
            id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            student_id INT UNSIGNED NOT NULL,
            teacher_id INT UNSIGNED NOT NULL,
            course VARCHAR(40) NOT NULL,
            unit VARCHAR(40) NOT NULL,
            page VARCHAR(40) NOT NULL,
            ex VARCHAR(60) NOT NULL,
            kind ENUM('check','show') NOT NULL,
            score SMALLINT UNSIGNED NOT NULL DEFAULT 0,
            total SMALLINT UNSIGNED NOT NULL DEFAULT 0,
            answers MEDIUMTEXT NULL,
            created_at DATETIME NOT NULL,
            KEY idx_student_ex (student_id, course, ex, id),
            KEY idx_teacher (teacher_id, id)
        )$T",
        // сводка по заданию: лучший и последний результат (для прогресса и для другого устройства)
        "CREATE TABLE IF NOT EXISTS en_progress (
            student_id INT UNSIGNED NOT NULL,
            course VARCHAR(40) NOT NULL,
            ex VARCHAR(60) NOT NULL,
            unit VARCHAR(40) NOT NULL,
            page VARCHAR(40) NOT NULL,
            best SMALLINT UNSIGNED NOT NULL DEFAULT 0,
            last SMALLINT UNSIGNED NOT NULL DEFAULT 0,
            total SMALLINT UNSIGNED NOT NULL DEFAULT 0,
            attempts INT UNSIGNED NOT NULL DEFAULT 0,
            shown TINYINT UNSIGNED NOT NULL DEFAULT 0,
            state TEXT NULL,
            first_at DATETIME NOT NULL,
            updated_at DATETIME NOT NULL,
            PRIMARY KEY (student_id, course, ex),
            KEY idx_unit (student_id, course, unit)
        )$T",
        "CREATE TABLE IF NOT EXISTS en_writing (
            student_id INT UNSIGNED NOT NULL,
            course VARCHAR(40) NOT NULL,
            wid VARCHAR(60) NOT NULL,
            page VARCHAR(160) NULL,
            text MEDIUMTEXT NOT NULL,
            words INT UNSIGNED NOT NULL DEFAULT 0,
            updated_at DATETIME NOT NULL,
            PRIMARY KEY (student_id, course, wid)
        )$T",
        // согласия: кто, какой документ и версия, когда; отзыв — withdrawn_at
        "CREATE TABLE IF NOT EXISTS en_consent (
            id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            role ENUM('teacher','student') NOT NULL,
            user_id INT UNSIGNED NOT NULL,
            teacher_id INT UNSIGNED NOT NULL,
            person VARCHAR(200) NOT NULL,
            doc VARCHAR(40) NOT NULL,
            version VARCHAR(16) NOT NULL,
            extra VARCHAR(255) NULL,
            accepted_at DATETIME NOT NULL,
            withdrawn_at DATETIME NULL,
            ip_hash CHAR(64) NULL,
            user_agent VARCHAR(255) NULL,
            KEY idx_user (role, user_id),
            KEY idx_accepted (accepted_at)
        )$T",
        "CREATE TABLE IF NOT EXISTS en_login_fail (
            id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            kind ENUM('teacher','student') NOT NULL,
            ip_hash CHAR(64) NOT NULL,
            created_at DATETIME NOT NULL,
            KEY idx_ip (ip_hash, created_at),
            KEY idx_created (created_at)
        )$T",
        "CREATE TABLE IF NOT EXISTS en_mail (
            id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            teacher_id INT UNSIGNED NOT NULL,
            student_id INT UNSIGNED NULL,
            kind VARCHAR(20) NOT NULL,
            to_email VARCHAR(190) NOT NULL,
            ok TINYINT UNSIGNED NOT NULL,
            created_at DATETIME NOT NULL,
            KEY idx_teacher (teacher_id, id)
        )$T",
    ];
    foreach ($sql as $q) {
        $pdo->exec($q);
    }
    // миграции: v2 — где ученик сейчас (для разбора с преподавателем в реальном времени)
    $cols = [];
    foreach ($pdo->query('SHOW COLUMNS FROM en_student') as $r) {
        $cols[$r['Field']] = true;
    }
    if (empty($cols['live_at'])) {
        $pdo->exec('ALTER TABLE en_student ADD COLUMN live_path VARCHAR(160) NULL, ADD COLUMN live_ex VARCHAR(60) NULL,
                    ADD COLUMN live_at DATETIME NULL');
    }
    // v3 — единый вход по коду (у ученика тоже 6 цифр), профиль (Telegram, фото), домашние работы
    $T3 = [
        "CREATE TABLE IF NOT EXISTS en_avatar (
            role ENUM('teacher','student') NOT NULL,
            user_id INT UNSIGNED NOT NULL,
            mime VARCHAR(20) NOT NULL,
            data MEDIUMBLOB NOT NULL,
            updated_at DATETIME NOT NULL,
            PRIMARY KEY (role, user_id)
        )$T",
        // домашняя работа: набор заданий из базы тестов курса
        "CREATE TABLE IF NOT EXISTS en_hw (
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            teacher_id INT UNSIGNED NOT NULL,
            title VARCHAR(200) NOT NULL,
            note TEXT NULL,
            course VARCHAR(40) NOT NULL,
            items TEXT NOT NULL,
            due_at DATETIME NULL,
            created_at DATETIME NOT NULL,
            archived_at DATETIME NULL,
            KEY idx_teacher (teacher_id, id)
        )$T",
        // кому назначена: пространства и отдельные ученики (для подписи); сами ученики — в en_hw_student
        "CREATE TABLE IF NOT EXISTS en_hw_target (
            hw_id INT UNSIGNED NOT NULL,
            kind ENUM('space','student') NOT NULL,
            ref_id INT UNSIGNED NOT NULL,
            PRIMARY KEY (hw_id, kind, ref_id)
        )$T",
        "CREATE TABLE IF NOT EXISTS en_hw_student (
            hw_id INT UNSIGNED NOT NULL,
            student_id INT UNSIGNED NOT NULL,
            assigned_at DATETIME NOT NULL,
            opened_at DATETIME NULL,
            submitted_at DATETIME NULL,
            seen_at DATETIME NULL,
            score SMALLINT UNSIGNED NULL,
            total SMALLINT UNSIGNED NULL,
            PRIMARY KEY (hw_id, student_id),
            KEY idx_student (student_id, hw_id)
        )$T",
    ];
    foreach ($T3 as $q) {
        $pdo->exec($q);
    }
    $add = function (string $table, string $col, string $ddl) use ($pdo) {
        // SHOW … LIKE не подготавливается: имя столбца — своя константа, не ввод пользователя
        if (!$pdo->query("SHOW COLUMNS FROM $table LIKE '$col'")->fetch()) {
            $pdo->exec("ALTER TABLE $table ADD COLUMN $ddl");
        }
    };
    $add('en_student', 'code', 'code CHAR(6) NULL, ADD UNIQUE KEY uq_code (code)');
    $add('en_student', 'telegram', 'telegram VARCHAR(64) NULL');
    $add('en_student', 'avatar_at', 'avatar_at DATETIME NULL');
    $add('en_teacher', 'telegram', 'telegram VARCHAR(64) NULL');
    $add('en_teacher', 'avatar_at', 'avatar_at DATETIME NULL');
    $add('en_attempt', 'hw_id', 'hw_id INT UNSIGNED NULL, ADD KEY idx_hw (hw_id, student_id, id)');
    // ученикам, добавленным до v3, — свой 6-значный код
    foreach ($pdo->query('SELECT id FROM en_student WHERE code IS NULL')->fetchAll(PDO::FETCH_COLUMN) as $sid) {
        $pdo->prepare('UPDATE en_student SET code = ? WHERE id = ?')->execute([new_code($pdo), (int)$sid]);
    }
    // v4 — личная ссылка преподавателя: lingvaden.ru/t/<token> (выдаёт админка lingvaden.ru)
    $add('en_teacher', 'token', 'token VARCHAR(16) NULL, ADD UNIQUE KEY uq_token (token)');
    foreach ($pdo->query('SELECT id FROM en_teacher WHERE token IS NULL')->fetchAll(PDO::FETCH_COLUMN) as $tid) {
        $pdo->prepare('UPDATE en_teacher SET token = ? WHERE id = ?')->execute([new_teacher_token($pdo), (int)$tid]);
    }
    // v5 — доступ к курсам: ученик видит только курсы, которые открыл ему преподаватель (закрытие — отметка revoked_at)
    $pdo->exec("CREATE TABLE IF NOT EXISTS en_student_course (
        student_id INT UNSIGNED NOT NULL,
        course VARCHAR(40) NOT NULL,
        granted_at DATETIME NOT NULL,
        revoked_at DATETIME NULL,
        PRIMARY KEY (student_id, course)
    )$T");
    $pdo->prepare("REPLACE INTO en_meta (k, v) VALUES ('schema', ?)")->execute([(string)EN_SCHEMA_VERSION]);
}

// ---- утилиты --------------------------------------------------------------

function now(): string
{
    return date('Y-m-d H:i:s');
}

function is_https(): bool
{
    return (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off')
        || (($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '') === 'https');
}

function site_url(): string
{
    $c = en_config();
    if (!empty($c['site'])) {
        return rtrim((string)$c['site'], '/');
    }
    return (is_https() ? 'https://' : 'http://') . ($_SERVER['HTTP_HOST'] ?? 'lingvaden.ru');
}

function secret(): string
{
    $s = (string)(en_config()['secret'] ?? '');
    return $s !== '' ? $s : 'en-dev-secret';
}

/** IP не храним: только HMAC с секретом (для защиты от перебора и как след согласия). */
function ip_hash(): string
{
    return hash_hmac('sha256', (string)($_SERVER['REMOTE_ADDR'] ?? ''), secret());
}

function ua(): string
{
    return mb_substr((string)($_SERVER['HTTP_USER_AGENT'] ?? ''), 0, 255);
}

function device(): string
{
    $u = strtolower(ua());
    if (strpos($u, 'ipad') !== false || strpos($u, 'tablet') !== false) {
        return 'tablet';
    }
    if (strpos($u, 'mobi') !== false || strpos($u, 'iphone') !== false || strpos($u, 'android') !== false) {
        return 'phone';
    }
    return 'desktop';
}

function rand_str(int $len, string $alphabet): string
{
    $out = '';
    $n = strlen($alphabet);
    for ($i = 0; $i < $len; $i++) {
        $out .= $alphabet[random_int(0, $n - 1)];
    }
    return $out;
}

const TOKEN_ALPHABET = '23456789abcdefghjkmnpqrstuvwxyz'; // без 0/o, 1/l/i

/** Токен личной ссылки преподавателя (/t/<token>): длиннее ученического — ссылка открывает кабинет. */
function new_teacher_token(PDO $pdo): string
{
    for ($i = 0; $i < 20; $i++) {
        $t = rand_str(12, TOKEN_ALPHABET);
        $st = $pdo->prepare('SELECT 1 FROM en_teacher WHERE token = ?');
        $st->execute([$t]);
        if (!$st->fetch()) {
            return $t;
        }
    }
    throw new RuntimeException('token');
}

function new_student_token(PDO $pdo): string
{
    for ($i = 0; $i < 20; $i++) {
        $t = rand_str(8, TOKEN_ALPHABET);
        $st = $pdo->prepare('SELECT 1 FROM en_student WHERE token = ?');
        $st->execute([$t]);
        if (!$st->fetch()) {
            return $t;
        }
    }
    throw new RuntimeException('token');
}

/** 6-значный код входа: общий для учителей и учеников, по нему понятно, кто вошёл. */
function new_code(PDO $pdo): string
{
    for ($i = 0; $i < 50; $i++) {
        $c = (string)random_int(100000, 999999);
        $st = $pdo->prepare('SELECT 1 FROM en_teacher WHERE code = ? UNION SELECT 1 FROM en_student WHERE code = ?');
        $st->execute([$c, $c]);
        if (!$st->fetch()) {
            return $c;
        }
    }
    throw new RuntimeException('code');
}

function clean_text($s, int $max): string
{
    $s = trim(preg_replace('/\s+/u', ' ', (string)$s));
    return mb_substr($s, 0, $max);
}

function clean_email($s): ?string
{
    $s = trim((string)$s);
    if ($s === '') {
        return null;
    }
    return filter_var($s, FILTER_VALIDATE_EMAIL) ? mb_strtolower(mb_substr($s, 0, 190)) : null;
}

function json_out($data, int $code = 200): void
{
    http_response_code($code);
    header('Content-Type: application/json; charset=utf-8');
    header('Cache-Control: no-store');
    echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    exit;
}

function fail(string $msg, int $code = 400): void
{
    json_out(['ok' => false, 'error' => $msg], $code);
}

function body(): array
{
    static $b = null;
    if ($b !== null) {
        return $b;
    }
    $raw = file_get_contents('php://input', false, null, 0, 512000);
    $b = json_decode((string)$raw, true);
    if (!is_array($b)) {
        $b = $_POST;
    }
    return $b;
}

// ---- сессии ----------------------------------------------------------------

function cookie_name(string $role): string
{
    return $role === 'teacher' ? 'en_t' : 'en_s';
}

function set_cookie(string $name, string $value, int $expires): void
{
    setcookie($name, $value, ['expires' => $expires, 'path' => '/', 'secure' => is_https(),
        'httponly' => true, 'samesite' => 'Lax']);
}

function session_start_for(PDO $pdo, string $role, int $userId): void
{
    $token = bin2hex(random_bytes(32));
    $days = $role === 'teacher' ? EN_TEACHER_DAYS : EN_STUDENT_DAYS;
    $exp = time() + $days * 86400;
    $pdo->prepare('INSERT INTO en_session (token_hash, role, user_id, created_at, last_seen_at, expires_at, user_agent)
                   VALUES (?, ?, ?, ?, ?, ?, ?)')
        ->execute([hash('sha256', $token), $role, $userId, now(), now(), date('Y-m-d H:i:s', $exp), ua()]);
    set_cookie(cookie_name($role), $token, $exp);
}

/** Пользователь роли по cookie или null. Продлевает вход не чаще раза в час. */
function current_user(PDO $pdo, string $role): ?array
{
    static $cache = [];
    if (array_key_exists($role, $cache)) {
        return $cache[$role];
    }
    $cache[$role] = null;
    $tok = (string)($_COOKIE[cookie_name($role)] ?? '');
    if (!preg_match('/^[0-9a-f]{64}$/', $tok)) {
        return null;
    }
    $st = $pdo->prepare('SELECT * FROM en_session WHERE token_hash = ? AND role = ? AND expires_at > NOW()');
    $st->execute([hash('sha256', $tok), $role]);
    $s = $st->fetch();
    if (!$s) {
        return null;
    }
    $table = $role === 'teacher' ? 'en_teacher' : 'en_student';
    $st = $pdo->prepare("SELECT * FROM $table WHERE id = ?");
    $st->execute([(int)$s['user_id']]);
    $u = $st->fetch();
    if (!$u || ($role === 'teacher' && $u['status'] !== 'active')) {
        return null;
    }
    if ($role === 'student') {
        $t = $pdo->prepare("SELECT id, name, status FROM en_teacher WHERE id = ?");
        $t->execute([(int)$u['teacher_id']]);
        $tt = $t->fetch();
        if (!$tt || $tt['status'] !== 'active') {
            return null;
        }
        $u['teacher_name'] = $tt['name'];
    }
    if (strtotime($s['last_seen_at']) < time() - 3600) {
        $days = $role === 'teacher' ? EN_TEACHER_DAYS : EN_STUDENT_DAYS;
        $exp = time() + $days * 86400;
        $pdo->prepare('UPDATE en_session SET last_seen_at = ?, expires_at = ? WHERE id = ?')
            ->execute([now(), date('Y-m-d H:i:s', $exp), $s['id']]);
        set_cookie(cookie_name($role), $tok, $exp);
    }
    $u['_session_id'] = (int)$s['id'];
    $cache[$role] = $u;
    return $u;
}

function session_end(PDO $pdo, string $role): void
{
    $tok = (string)($_COOKIE[cookie_name($role)] ?? '');
    if ($tok !== '') {
        $pdo->prepare('DELETE FROM en_session WHERE token_hash = ?')->execute([hash('sha256', $tok)]);
    }
    set_cookie(cookie_name($role), '', time() - 3600);
}

// ---- защита от перебора кодов ---------------------------------------------

/** Минут ожидания (0 — можно пробовать). 8 ошибок с адреса за 15 минут или 300 по всем адресам. */
function throttle_wait(PDO $pdo, string $kind): int
{
    $st = $pdo->prepare('SELECT COUNT(*) FROM en_login_fail WHERE kind = ? AND ip_hash = ? AND created_at > NOW() - INTERVAL 15 MINUTE');
    $st->execute([$kind, ip_hash()]);
    if ((int)$st->fetchColumn() >= 8) {
        return 15;
    }
    $st = $pdo->prepare('SELECT COUNT(*) FROM en_login_fail WHERE kind = ? AND created_at > NOW() - INTERVAL 15 MINUTE');
    $st->execute([$kind]);
    return (int)$st->fetchColumn() >= 300 ? 15 : 0;
}

function throttle_note(PDO $pdo, string $kind): void
{
    $pdo->prepare('INSERT INTO en_login_fail (kind, ip_hash, created_at) VALUES (?, ?, ?)')->execute([$kind, ip_hash(), now()]);
    if (random_int(1, 50) === 1) {
        $pdo->exec('DELETE FROM en_login_fail WHERE created_at < NOW() - INTERVAL 1 DAY');
    }
}

// ---- журнал -----------------------------------------------------------------

function log_event(PDO $pdo, string $role, int $userId, int $teacherId, string $type, array $f = []): void
{
    $data = isset($f['data']) ? json_encode($f['data'], JSON_UNESCAPED_UNICODE) : null;
    $pdo->prepare('INSERT INTO en_event (role, user_id, teacher_id, type, course, page, ex, data, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)')
        ->execute([$role, $userId, $teacherId, $type, $f['course'] ?? null,
            isset($f['page']) ? mb_substr((string)$f['page'], 0, 160) : null,
            isset($f['ex']) ? mb_substr((string)$f['ex'], 0, 60) : null, $data, now()]);
}

/** Учёт времени: секунды и страницы в текущем визите (разрыв > 30 мин — новый визит). */
function visit_touch(PDO $pdo, string $role, int $userId, int $teacherId, int $sec, int $pages): void
{
    $st = $pdo->prepare('SELECT id FROM en_visit WHERE role = ? AND user_id = ? AND last_at > NOW() - INTERVAL 30 MINUTE
                         ORDER BY last_at DESC LIMIT 1');
    $st->execute([$role, $userId]);
    $id = $st->fetchColumn();
    if ($id) {
        $pdo->prepare('UPDATE en_visit SET last_at = ?, seconds = seconds + ?, pages = pages + ? WHERE id = ?')
            ->execute([now(), $sec, $pages, $id]);
    } else {
        $pdo->prepare('INSERT INTO en_visit (role, user_id, teacher_id, started_at, last_at, seconds, pages, device)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)')
            ->execute([$role, $userId, $teacherId, now(), now(), $sec, $pages, device()]);
    }
    $table = $role === 'teacher' ? 'en_teacher' : 'en_student';
    $pdo->prepare("UPDATE $table SET last_seen_at = ?, total_seconds = total_seconds + ? WHERE id = ?")
        ->execute([now(), $sec, $userId]);
}

/** Все данные ученика — по требованию учителя, админа или самого ученика (отзыв согласия). */
/** Курс страницы или файла: /unitNN/… и media/sb|wb|video/… — Outcomes Intermediate; папка урока «<курс>-<урок>»
 *  (efrl-l01/…) — курс по префиксу; иначе первая часть пути — id курса. */
function path_course(string $f): string
{
    $f = ltrim($f, '/');
    if (preg_match('~^(unit[0-9]{2}|sb|wb|video)(/|$)~', $f)) {
        return 'outcomes-int';
    }
    if (preg_match('~^([a-z]+)-[a-z][0-9]{2}(/|$)~', $f, $m)) {
        return $m[1];
    }
    return (string)strtok($f, '/');
}

/** Курсы, открытые ученику. */
function student_courses(PDO $pdo, int $sid): array
{
    $st = $pdo->prepare('SELECT course FROM en_student_course WHERE student_id = ? AND revoked_at IS NULL ORDER BY granted_at');
    $st->execute([$sid]);
    return $st->fetchAll(PDO::FETCH_COLUMN);
}

/** Ученик может открыть курс: преподаватель открыл ему курс или задал по нему домашнюю работу. */
function student_can(PDO $pdo, int $sid, string $course): bool
{
    $st = $pdo->prepare('SELECT 1 FROM en_student_course WHERE student_id = ? AND course = ? AND revoked_at IS NULL
                         UNION SELECT 1 FROM en_hw_student hs JOIN en_hw h ON h.id = hs.hw_id WHERE hs.student_id = ? AND h.course = ?
                         LIMIT 1');
    $st->execute([$sid, $course, $sid, $course]);
    return (bool)$st->fetchColumn();
}

function delete_student_data(PDO $pdo, int $sid): void
{
    foreach (['en_space_member' => 'student_id', 'en_attempt' => 'student_id', 'en_progress' => 'student_id',
              'en_writing' => 'student_id', 'en_hw_student' => 'student_id', 'en_student_course' => 'student_id'] as $t => $col) {
        $pdo->prepare("DELETE FROM $t WHERE $col = ?")->execute([$sid]);
    }
    $pdo->prepare("DELETE FROM en_session WHERE role = 'student' AND user_id = ?")->execute([$sid]);
    $pdo->prepare("DELETE FROM en_avatar WHERE role = 'student' AND user_id = ?")->execute([$sid]);
    $pdo->prepare("DELETE FROM en_visit WHERE role = 'student' AND user_id = ?")->execute([$sid]);
    $pdo->prepare("DELETE FROM en_event WHERE role = 'student' AND user_id = ?")->execute([$sid]);
    $pdo->prepare("UPDATE en_mail SET to_email = '—' WHERE student_id = ?")->execute([$sid]);
    // согласия остаются как доказательство (152-ФЗ, ст. 9 ч. 3), с отметкой отзыва
    $pdo->prepare("UPDATE en_consent SET withdrawn_at = COALESCE(withdrawn_at, ?) WHERE role = 'student' AND user_id = ?")
        ->execute([now(), $sid]);
    $pdo->prepare('DELETE FROM en_student WHERE id = ?')->execute([$sid]);
}

function consent_missing(PDO $pdo, string $role, int $userId): array
{
    $need = $role === 'teacher' ? ['terms', 'privacy', 'cookies', 'teacher_terms'] : ['terms', 'privacy', 'cookies', 'student_consent'];
    $st = $pdo->prepare('SELECT doc, version FROM en_consent WHERE role = ? AND user_id = ? AND withdrawn_at IS NULL');
    $st->execute([$role, $userId]);
    $have = [];
    foreach ($st as $r) {
        $have[$r['doc'] . '@' . $r['version']] = true;
    }
    $miss = [];
    foreach ($need as $d) {
        if (empty($have[$d . '@' . EN_DOCS[$d]])) {
            $miss[] = $d;
        }
    }
    return $miss;
}

function send_mail(string $to, string $subject, string $text): bool
{
    $c = en_config();
    $from = (string)($c['mail_from'] ?? 'noreply@lingvaden.ru');
    $headers = "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n"
        . 'From: =?UTF-8?B?' . base64_encode('Lingvaden English') . "?= <$from>\r\n";
    if (!function_exists('mail')) {
        return false;
    }
    return @mail($to, '=?UTF-8?B?' . base64_encode($subject) . '?=', $text, $headers);
}
