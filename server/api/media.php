<?php
/**
 * Аудио и видео курсов (media/sb|wb|video — Outcomes, media/efrl — English for Real Life) — только для вошедших
 * (ученику — только открытых ему курсов), с поддержкой Range
 * (перемотка, iOS Safari). .htaccess направляет сюда все запросы /media/…
 */

declare(strict_types=1);
require __DIR__ . '/_lib.php';

$f = (string)($_GET['f'] ?? '');
if (!preg_match('~^(sb|wb|video|efrl)/[a-z0-9-]+\.(mp3|mp4)$~', $f, $m)) {
    http_response_code(404);
    exit;
}
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
    http_response_code(403);
    exit;
}
if ($denied) {
    http_response_code(403);
    exit;
}
$pdo = null;
$path = dirname(__DIR__) . '/media/' . $f;
if (!is_file($path)) {
    http_response_code(404);
    exit;
}
$size = filesize($path);
$start = 0;
$end = $size - 1;
header('Content-Type: ' . ($m[2] === 'mp4' ? 'video/mp4' : 'audio/mpeg'));
header('Accept-Ranges: bytes');
header('Cache-Control: private, max-age=604800');
header('X-Robots-Tag: noindex, nofollow');
$etag = '"' . dechex(filemtime($path)) . '-' . dechex($size) . '"';
header('ETag: ' . $etag);
if (preg_match('~^bytes=(\d*)-(\d*)$~', (string)($_SERVER['HTTP_RANGE'] ?? ''), $r)) {
    if ($r[1] === '' && $r[2] !== '') {          // последние N байт
        $start = max(0, $size - (int)$r[2]);
    } else {
        $start = (int)$r[1];
        if ($r[2] !== '') {
            $end = min((int)$r[2], $size - 1);
        }
    }
    if ($start > $end || $start >= $size) {
        http_response_code(416);
        header("Content-Range: bytes */$size");
        exit;
    }
    http_response_code(206);
    header("Content-Range: bytes $start-$end/$size");
}
$len = $end - $start + 1;
header('Content-Length: ' . $len);
if ($_SERVER['REQUEST_METHOD'] === 'HEAD') {
    exit;
}
@set_time_limit(0);
while (ob_get_level()) {
    ob_end_clean();
}
$fp = fopen($path, 'rb');
fseek($fp, $start);
while ($len > 0 && !feof($fp) && !connection_aborted()) {
    $chunk = fread($fp, (int)min(262144, $len));
    echo $chunk;
    flush();
    $len -= strlen($chunk);
}
fclose($fp);
