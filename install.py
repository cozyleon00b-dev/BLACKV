#!/usr/bin/env python3
# BLACKV Universal Installer

import os
import sys
import platform

def detect_os():
    system = platform.system().lower()
    if 'termux' in os.environ.get('PREFIX', ''):
        return 'termux'
    elif system == 'linux':
        return 'linux'
    elif system == 'darwin':
        return 'macos'
    elif system == 'windows':
        return 'windows'
    return 'unknown'

def run_command(cmd):
    print(f"[RUN] {cmd}")
    os.system(cmd)

def install_termux():
    print("\n[INSTALL] Termux detected")
    run_command("pkg update && pkg upgrade -y")
    run_command("pkg install git python -y")
    run_command("pip install requests")
    run_command("termux-setup-storage")

def install_linux():
    print("\n[INSTALL] Linux detected")
    if os.path.exists('/etc/debian_version'):
        print("[DISTRO] Debian/Ubuntu/Kali detected")
        run_command("sudo apt update && sudo apt install git python3 python3-pip -y")
        run_command("pip3 install requests")
    elif os.path.exists('/etc/arch-release'):
        print("[DISTRO] Arch Linux/BlackArch detected")
        run_command("sudo pacman -Syu --noconfirm")
        run_command("sudo pacman -S git python python-pip --noconfirm")
        run_command("pip install requests")
    elif os.path.exists('/etc/fedora-release'):
        print("[DISTRO] Fedora detected")
        run_command("sudo dnf install git python3 python3-pip -y")
        run_command("pip3 install requests")
    else:
        print("[ERROR] Distro not recognized")

def install_macos():
    print("\n[INSTALL] macOS detected")
    run_command("brew install git python3")
    run_command("pip3 install requests")

def install_windows():
    print("\n[INSTALL] Windows detected")
    print("[INFO] Make sure Git and Python are installed")
    run_command("pip install requests")

def main():
    print("="*50)
    print("     BLACKV UNIVERSAL INSTALLER")
    print("     VERSION 2.0")
    print("     DEVELOPER: COZY")
    print("="*50)
    
    os_type = detect_os()
    print(f"\n[DETECTED OS] {os_type}")
    
    if os_type == 'termux':
        install_termux()
    elif os_type == 'linux':
        install_linux()
    elif os_type == 'macos':
        install_macos()
    elif os_type == 'windows':
        install_windows()
    else:
        print("\n[ERROR] Unknown operating system")
        sys.exit(1)
    
    print("\n" + "="*50)
    print("[SUCCESS] BLACKV INSTALLATION COMPLETE")
    print("="*50)
    print("\nTo run BLACKV:")
    print("  python blackv.py")

if __name__ == "__main__":
    main()