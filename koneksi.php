<?php
session_start();

$host = "localhost";
$user = "root";
$pass = "";
$db   = "db_crud";

$koneksi = mysqli_connect($host, $user, $pass, $db);

if (!$koneksi) {
    die("Koneksi gagal: " . mysqli_connect_error());
}

mysqli_set_charset($koneksi, "utf8mb4");

// Daftar pilihan jurusan
$daftar_jurusan = [
    "Teknik Informatika",
    "Sistem Informasi",
    "Teknik Elektro",
    "Manajemen",
    "Akuntansi"
];

// Fungsi keamanan untuk mencegah XSS
function e($teks) {
    return htmlspecialchars($teks ?? '', ENT_QUOTES, 'UTF-8');
}
?>