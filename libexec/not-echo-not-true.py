#!/usr/bin/env python3
import os
import sys
import time
import shutil

__version__ = "1.6.0-libnene"

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
    print("Source: https://github.com/luisadha/nene/tree/main\n")

# Ambil apps dari update-lists
raw_apps = []
pkg_file = os.path.join(os.environ["HOME"], ".local/share/nene/update-lists")

if os.path.isfile(pkg_file):
    with open(pkg_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(maxsplit=2)
            if len(parts) == 3:
                name, url, label = parts
            elif len(parts) == 2:
                name, url = parts
                label = "Free Trial"
            elif len(parts) == 1:
                name = parts[0]
                url = f"https://luisadha.github.io/{name.lower()}"  # default URL
                label = "Free Trial"
            else:
                continue
            raw_apps.append((name, url, label))
else:
    print(f"No package file found at {pkg_file}")

# Sortir berdasarkan nama
apps = sorted(raw_apps, key=lambda x: x[0])

# === Menu utama ===
while True:
    banner()

    if not apps:
        print("No installed apps found.\nExiting..")
        break

    # Hitung panjang kolom nomor + nama
    max_len = max(len(f"{i}) {name}") for i, (name, _, _) in enumerate(apps, start=1))

    # Tampilkan menu
    for i, (name, _, status) in enumerate(apps, start=1):
        print(f"{i}) {name:<{max_len - len(str(i))}} | {status}")

    # EXIT
    print(f"{'0) EXIT':<{max_len}} |")

    # Input user
    try:
        choice = input("\nSelect an option: ").strip()
        if not choice.isdigit():
            continue
        choice = int(choice)
    except (EOFError, KeyboardInterrupt):
        print("\nExiting..")
        sys.exit(0)

    if choice == 0:
        print("You selected (0)\nExiting..")
        break
    elif 1 <= choice <= len(apps):
        name, url, _ = apps[choice - 1]
        print(f"You selected ({choice}): {name}\nLaunching..")
        time.sleep(1)
        os.system(f'bash -c "source <(curl -sSL {url})"')
    else:
        print("Invalid option.\n")
