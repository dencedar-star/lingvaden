<?php
/**
 * Страницы курсов — только для вошедших (учитель или ученик). .htaccess направляет сюда /unitNN/… и /efrl-lNN/…;
 * без входа — на главную, где спрашивается код.
 */

declare(strict_types=1);
require __DIR__ . '/_lib.php';

$f = (string)($_GET['f'] ?? '');
if (!preg_match('~^(unit[0-9]{2}/(index|book|writing|theory|tests|workbook)|[a-z]+-[a-z][0-9]{2}/(index|lesson))\.html$~', $f)) {
    http_response_code(404);
    exit;
}
$path = dirname(__DIR__) . '/' . $f;
try {
    $pdo = en_db();
    $ok = (bool)current_user($pdo, 'teacher');
    $s = $ok ? null : current_user($pdo, 'student');
    $ok = $ok || $s;
    // ученику — только открытые ему курсы
    $denied = $s && !student_can($pdo, (int)$s['id'], path_course($f));
} catch (Throwable $e) {
    $ok = false;
    $denied = false;
}
if (!$ok) {
    header('Cache-Control: no-store');
    header('Location: /?next=' . rawurlencode('/' . preg_replace('~index\.html$~', '', $f)), true, 302);
    exit;
}
if ($denied) {
    header('Cache-Control: no-store');
    header('Location: /me/#courses', true, 302);
    exit;
}
if (!is_file($path)) {
    http_response_code(404);
    exit;
}
header('Content-Type: text/html; charset=utf-8');
header('Cache-Control: private, no-cache');
header('X-Robots-Tag: noindex, nofollow');
readfile($path);
