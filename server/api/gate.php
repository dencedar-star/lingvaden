<?php
/**
 * Страницы курсов — только для вошедших (учитель или ученик). .htaccess направляет сюда /unitNN/…;
 * без входа — на главную, где спрашивается код.
 */

declare(strict_types=1);
require __DIR__ . '/_lib.php';

$f = (string)($_GET['f'] ?? '');
if (!preg_match('~^unit[0-9]{2}/(index|book|writing|theory|tests|workbook)\.html$~', $f)) {
    http_response_code(404);
    exit;
}
$path = dirname(__DIR__) . '/' . $f;
try {
    $pdo = en_db();
    $ok = current_user($pdo, 'teacher') || current_user($pdo, 'student');
} catch (Throwable $e) {
    $ok = false;
}
if (!$ok) {
    header('Cache-Control: no-store');
    header('Location: /?next=' . rawurlencode('/' . preg_replace('~index\.html$~', '', $f)), true, 302);
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
