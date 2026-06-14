#!/data/data/com.termux/files/usr/bin/bash

echo "=========================================="
echo "     BLACKV TERMUX SETUP"
echo "=========================================="

echo "[1/5] Updating packages..."
pkg update && pkg upgrade -y

echo "[2/5] Installing dependencies..."
pkg install git python -y

echo "[3/5] Cloning BLACKV repository..."
git clone https://github.com/YOUR_USERNAME/BLACKV.git

cd BLACKV

echo "[4/5] Installing Python modules..."
pip install requests

echo "[5/5] Setting up storage access..."
termux-setup-storage

echo "alias blackv='cd ~/BLACKV && python blackv.py'" >> ~/.bashrc

echo ""
echo "=========================================="
echo "SETUP COMPLETE!"
echo "=========================================="
echo "Run: cd ~/BLACKV && python blackv.py"
echo "=========================================="