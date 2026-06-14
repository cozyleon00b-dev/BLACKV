================================================================================
BLACKV - ADVANCED SECURITY TESTING TOOL
================================================================================
VERSION: 2.0
DEVELOPER: COZY
RELEASE DATE: 12/6/2026
STATUS: FULL VERSION - PREMIUM
================================================================================

DESCRIPTION
================================================================================
BLACKV adalah alat pengujian keamanan website tingkat lanjut yang dirancang untuk 
security researcher dan bug hunter professional. Tools ini memiliki kemampuan 
penetration testing lengkap dengan sistem enkripsi penuh dan anti-tracking.

KEUNGGULAN BLACKV:
- Full encryption pada semua data dan log
- Anti firewall dan anti triggerwall
- Susah dilacak (trace hiding activated)
- Real attack (no simulation)
- Auto report generation
- Dual language (English/Indonesia)

================================================================================
SYSTEM REQUIREMENTS
================================================================================
1. Windows 7/8/10/11 (32bit or 64bit)
2. Python 3.8 or higher
3. Internet connection
4. Minimum RAM 2GB
5. Minimum storage 500MB

================================================================================
INSTALLATION GUIDE
================================================================================

STEP 1 - INSTALL PYTHON
--------------------------------------------------
Jika belum punya Python, download dari:
https://www.python.org/downloads/

Pilih versi 3.8 atau lebih tinggi.
SAAT INSTALL, CENTANG "Add Python to PATH"

STEP 2 - EXTRACT FILES
--------------------------------------------------
Extract semua file BLACKV ke satu folder.
Contoh: C:\BLACKV

STEP 3 - RUN INSTALLER
--------------------------------------------------
Double click file "install.bat"
Tunggu hingga proses instalasi selesai.

STEP 4 - VERIFY INSTALLATION
--------------------------------------------------
Buka CMD di folder BLACKV, ketik:
python --version

Jika muncul versi Python, instalasi berhasil.

================================================================================
HOW TO RUN BLACKV
================================================================================

METHOD 1 - DOUBLE CLICK
--------------------------------------------------
Double click file "run.bat"

METHOD 2 - VIA COMMAND PROMPT
--------------------------------------------------
Buka CMD di folder BLACKV, ketik:
python blackv.py

================================================================================
LOGIN ACCESS
================================================================================

Setelah menjalankan BLACKV, Anda akan diminta memilih akses:

BUYER ACCESS
--------------------------------------------------
PIN: 281235
Fitur: Semua menu tersedia untuk single user

DEVELOPER ACCESS
--------------------------------------------------
PIN: 281535
Fitur: Semua menu + akses full system

================================================================================
MENU GUIDE - COMPLETE TUTORIAL
================================================================================

MENU 1 - COPY ALL WEBSITE
================================================================================
Fungsi: Mengcopy semua file website target secara lengkap

Cara Penggunaan:
1. Pilih menu 1
2. Masukkan URL target (contoh: https://targetwebsite.com)
3. Tunggu proses cloning selesai

Hasil:
- Semua file HTML, CSS, JavaScript, Images akan tersimpan
- Lokasi: folder "cloned/[nama website]/"

Contoh Command:
Target URL: https://example.com
Hasil: cloned/example com/index.html + semua assets

Tips: Tools ini akan mendeteksi dan mengunduh semua resource otomatis

================================================================================

MENU 2 - CHECK ADMIN AUTH LOGIN AND PASSWORD
================================================================================
Fungsi: Mencari halaman login admin dan panel authentication

Cara Penggunaan:
1. Pilih menu 2
2. Masukkan URL target
3. Tunggu scanning selesai

Hasil:
- Daftar semua halaman login yang ditemukan
- Status authentication requirement
- Rekomendasi default credentials

Laporan tersimpan di: reports/[nama website] - ADMIN_AUTH.txt

List Path yang Discan:
- /admin, /login, /administrator, /wp-admin
- /cpanel, /dashboard, /adminpanel
- /auth, /signin, /backend
- dan 20+ path lainnya

================================================================================

MENU 3 - CHECK BUGS (BUG HUNTER MODE)
================================================================================
Fungsi: Scan komprehensif untuk mencari vulnerabilities

Jenis Bug yang DiScan:
--------------------------------------------------
1. SQL Injection (SQLi)
   - Test parameter: id, page, user, q, search, cat, product
   - Payload: 1', 1%27, ' OR '1'='1

2. Cross Site Scripting (XSS)
   - Payload: <script>alert(1)</script>
   - Test di semua parameter

3. Local File Inclusion (LFI)
   - Test: ../../../../etc/passwd
   - Backup file exposure

4. Exposed Files
   - robots.txt
   - .htaccess
   - backup.zip
   - config.php.bak

5. Admin Panel Exposure
   - Scan 20+ admin path variants

Cara Penggunaan:
1. Pilih menu 3
2. Masukkan URL target
3. Tunggu scan selesai (1-2 menit)

Hasil Laporan:
- Daftar semua vulnerabilities yang ditemukan
- Lokasi tepat vulnerability
- Rekomendasi exploit

Laporan: reports/[nama website] - BUG_HUNTER.txt

================================================================================

MENU 4 - DDOS ATTACK
================================================================================
Fungsi: Distributed Denial of Service attack simulation

Parameter:
--------------------------------------------------
- Max attack: 200 requests
- Multi-threading: 10 threads per request
- Protocol: TCP/IP with keep-alive

Cara Penggunaan:
1. Pilih menu 4
2. Masukkan URL target
3. Masukkan jumlah attack (1-200)
4. Tunggu proses selesai

Technical Detail:
- Setiap 1 attack = 10 packet requests
- Attack 200 = 2000 total packets
- Menggunakan socket connection langsung
- Bypass common firewall rules

Hasil:
- Server akan mengalami overload
- Website menjadi tidak responsif
- Log attack tersimpan di folder reports

Peringatan: Gunakan hanya untuk testing website sendiri

================================================================================

MENU 5 - DOS ATTACK
================================================================================
Fungsi: Denial of Service attack (single source)

Parameter:
--------------------------------------------------
- Max attack: 100 requests
- Heavy request: 5 request per attack
- HTTP/1.1 with keep-alive

Cara Penggunaan:
1. Pilih menu 5
2. Masukkan URL target
3. Masukkan jumlah attack (1-100)
4. Tunggu proses selesai

Perbedaan DDOS dan DOS:
- DDOS: Multi-thread, lebih agresif
- DOS: Single source, lebih stealth

================================================================================

MENU 6 - XML (MODIFY WEBSITE)
================================================================================
Fungsi: Memodifikasi tampilan website target

Cara Penggunaan:
1. Pilih menu 6
2. Masukkan URL target
3. Masukkan pesan yang ingin ditampilkan
4. Masukkan judul baru

Hasil:
- File HTML termodifikasi tersimpan di folder "xml_output"
- Siap untuk di-deploy ke server target

Contoh:
Target: https://example.com
Pesan: Hacked by BLACKV
Judul: Security Test

Hasil file: xml_output/example com_modified.html

================================================================================

MENU 7 - CREDIT AND INFO
================================================================================
Menampilkan informasi tool:
- Developer: Cozy
- Release Date: 12/6/2026
- Version: 2.0
- Status: Buyer/Developer

================================================================================

MENU 8 - CHANGE LANGUAGE
================================================================================
Fungsi: Mengganti bahasa antarmuka

Pilihan Bahasa:
--------------------------------------------------
1. English (Default)
2. Indonesia

Gunakan sebelum login untuk pengalaman terbaik

================================================================================
REPORT SYSTEM
================================================================================

Semua aktivitas akan tercatat dalam laporan otomatis:

Format Laporan:
--------------------------------------------------
Nama File: [nama website] - [tool name].txt
Lokasi: folder "reports/"

Isi Laporan:
- Target URL
- Tool yang digunakan
- Tanggal dan waktu
- Hasil lengkap scanning/attack

Contoh nama file:
"example com - ADMIN_AUTH.txt"
"example com - BUG_HUNTER.txt"
"example com - DDOS.txt"

================================================================================
ANTI DETECTION FEATURES
================================================================================

BLACKV dilengkapi proteksi anti-detection:

1. Firewall Bypass
   - Otomatis menonaktifkan Windows Firewall sementara
   - Menggunakan rotated User-Agent

2. Trace Hiding
   - IP renewal system
   - No persistent logs di local machine

3. Encryption
   - Semua data tersimpan dalam format terenkripsi
   - Menggunakan XOR cipher dengan key 281535/281235

4. No Triggerwall
   - Attack pattern tidak terdeteksi sebagai DDoS
   - Menggunakan randomized request intervals

================================================================================
TROUBLESHOOTING
================================================================================

ERROR: Python not found
--------------------------------------------------
Solusi: Install Python dari python.org
Pastikan centang "Add Python to PATH"

ERROR: Module not found
--------------------------------------------------
Solusi: Jalankan install.bat sebagai Administrator

ERROR: Connection timeout
--------------------------------------------------
Solusi: 
- Periksa koneksi internet
- Matikan antivirus sementara
- Jalankan sebagai Administrator

ERROR: Access denied
--------------------------------------------------
Solusi:
- Pastikan PIN yang dimasukkan benar
- Buyer PIN: 281235
- Developer PIN: 281535

ERROR: Target website not responding
--------------------------------------------------
Solusi:
- Website mungkin sedang down
- Coba gunakan VPN
- Kurangi jumlah attack

================================================================================
LEGAL DISCLAIMER
================================================================================
BLACKV dirancang untuk tujuan PENGUJIAN KEAMANAN dan PENDIDIKAN.
Pengguna bertanggung jawab penuh atas penggunaan tools ini.

Hanya gunakan pada:
- Website milik sendiri
- Website yang memiliki izin tertulis untuk testing
- Environment laboratorium keamanan

Penggunaan ilegal akan ditanggung sepenuhnya oleh pengguna.

================================================================================
CONTACT & SUPPORT
================================================================================
Developer: Cozy
Version: 2.0
Release: 12/6/2026

Untuk support dan update:
- Hubungi via channel resmi
- Sertakan bukti pembelian

================================================================================
CHANGELOG
================================================================================

Version 2.0 (12/6/2026)
--------------------------------------------------
- Initial release
- Full 7 menu features
- Dual language support
- Auto report generation
- Full encryption system
- Anti detection features
- Real attack capability

================================================================================
END OF README
================================================================================