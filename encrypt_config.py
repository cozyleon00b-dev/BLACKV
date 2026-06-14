#!/usr/bin/env python3
# BLACKV Config Encryptor

import base64
import os
import json

KEY = 281535

def encrypt_config():
    config_data = {
        "version": "2.0",
        "developer": "Cozy",
        "date": "12/6/2026",
        "buyer_pin": "281235",
        "dev_pin": "281535",
        "max_ddos": 200,
        "max_dos": 100
    }
    
    json_str = json.dumps(config_data)
    
    encrypted = []
    for i, char in enumerate(json_str):
        key_byte = (KEY + i) % 256
        encrypted.append(chr(ord(char) ^ key_byte))
    
    encrypted_str = base64.b64encode(''.join(encrypted).encode()).decode()
    
    with open("config.enc", "w") as f:
        f.write(encrypted_str)
    
    print("Config encrypted and saved to config.enc")

if __name__ == "__main__":
    encrypt_config()