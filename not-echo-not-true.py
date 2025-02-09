#/usr/bin/env python3

import os
import time
import shutil

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
    print("Script: nent v1.0-stable")
    print("Author: luisadha\n")

apps = [
    (1, "Alrc-Termux", "Free")
] + sorted([
    (2, "Anti-hangman", "Free"),
    (3, "Ascii-Live-Termux", "Free"),
    (4, "Brandomusic", "Free"),
    (5, "Termcreed", "Free"),
    (6, "Weapon-Url-Opener", "Trial"),
], key=lambda x: x[1])

while True:
    banner()

    for num, name, status in apps:
        print(f"{num}) {name.ljust(20)} | {status}")

    print("0) EXIT")

    try:
        choice = int(input("\nSelect an option: ").strip())
    except ValueError:
        continue
    if choice == 0:
        print("Exiting...")
        break  
    if choice == 1:
        url = "https://alrc.luisadha.my.id"
    else:
        urls = {
            2: "anti-hangman",
            3: "ascii-live-termux",
            4: "brandomusic",
            5: "termcreed",
            6: "weapon-url-opener",
        }
        url = f"https://luisadha.github.io/{urls.get(choice, '')}"

    if url:
        print(f"You selected ({choice})")
        time.sleep(1)
        os.system(f'bash -c "source <(curl -L {url})"')
