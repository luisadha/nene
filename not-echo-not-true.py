#!/usr/bin/env python3

import os
import sys
import time
import shutil

__version__ = ""1.4.32-nightly"

def center_text(text):
    width = shutil.get_terminal_size((80, 20)).columns
    return text.center(width)

def logo():
    text = "[ !echo <(!True) ]"
    width = shutil.get_terminal_size((80, 20)).columns
    padding = (width - len(text) - 2) // 2
    padding = max(padding, 0)
    banner = "=" * padding + " " + text + " " + "=" * padding
    if len(banner) < width:
        banner += "="
    print(banner)

def banner():
    print("\n")
    logo()
    print("\n" + center_text("Try online apps from luisadha using Curl") + "\n")
    print("=" * shutil.get_terminal_size((80, 20)).columns)
    print(f"Script: nene {__version__}")
    print("Author: luisadha")
    print("Source: https://not-echo-not-true.carrd.co\n")

# Daftar aplikasi dan URL-nya (tanpa nomor)
raw_apps = [
    ("Alrc-Termux", "https://alrc.luisadha.my.id", "Install for free"),
    ("Anti-hangman", "https://luisadha.github.io/anti-hangman", "Free Trial"),
    ("Ascii-Live-Termux", "https://luisadha.github.io/ascii-live-termux", "Free Trial"),
    ("Brandomusic", "https://luisadha.github.io/brandomusic", "Free Trial"),
    ("Pangram-Cli", "https://luisadha.github.io/pangram-cli", "Free Trial"),
    ("Termcreed", "https://luisadha.github.io/termcreed", "Free Trial"),
    ("Weapon-Url-Opener", "https://luisadha.github.io/weapon-url-opener", "Free Trial"),
    ("Weapon-Url-Opener (Nightly)", "https://luisadha.github.io/weapon-url-opener-nightly", "Free Trial"),
]

# Sortir berdasarkan nama
apps = sorted(raw_apps, key=lambda x: x[0])

while True:
    banner()

    # Hitung lebar kolom nama aplikasi terpanjang
    max_name_len = max(len(name) for name, _, _ in apps)

    # Tampilkan menu
    for i, (name, _, status) in enumerate(apps, start=1):
        print(f"{i}) {name.ljust(max_name_len)} | {status}")
    print("0) EXIT")

    # Input user
    try:
        choice = input("\nSelect an option: ").strip()
        if not choice.isdigit():
            continue
        choice = int(choice)
    except EOFError:
        print("\nAutomatically selected (0) because end-of-file was reached.\nExiting..")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nCaught ^C\nExiting..")
        sys.exit(1)

    if choice == 0:
        print("You selected (0)\nExiting..")
        break
    elif 1 <= choice <= len(apps):
        name, url, _ = apps[choice - 1]
        print(f"You selected ({choice}): {name}")
        time.sleep(1)
        os.system(f'bash -c "source <(curl -sSL {url})"')
    else:
        print("Invalid option.\n")
