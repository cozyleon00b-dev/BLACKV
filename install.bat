@echo off
title BLACKV INSTALLER
color 0C

echo ================================================
echo           BLACKV INSTALLATION
echo ================================================
echo.

echo [1] Checking Python installation...
python --version > nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo Please install Python 3.8 or higher
    echo Download from: https://python.org
    pause
    exit
)
echo [SUCCESS] Python found

echo.
echo [2] Installing requirements...
pip install requests

echo.
echo [3] Creating directories...
mkdir cloned > nul 2>&1
mkdir reports > nul 2>&1
mkdir xml_output > nul 2>&1

echo.
echo [4] Setting up firewall bypass...
netsh advfirewall set allprofiles state off > nul 2>&1

echo.
echo ================================================
echo           INSTALLATION COMPLETE
echo ================================================
echo.
echo To run BLACKV:
echo python blackv.py
echo.
pause