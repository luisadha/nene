#/usr/bin/env python3

import os
import sys
import time
import shutil

__version__ = "v1.2.2+1-nightly-20250601"

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
    print(f"Source: https://not-echo-not-true.carrd.co")
    print("\n")

apps = [
    (1, "Alrc-Termux", "Install for free")
] + sorted([
    (2, "Anti-hangman", "Free Trial"),
    (3, "Ascii-Live-Termux", "Free Trial"),
    (4, "Brandomusic", "Free Trial"),
    (5, "Termcreed", "Free Trial"),
    (6, "Weapon-Url-Opener", "Free Trial"),
    (7, "Weapon-Url-Opener (Nightly)", "Free Trial"),
    (8, "Pangram-Cli", "Free Trial"),
], key=lambda x: x[1])

while True:
    banner()
    # Hitung lebar kolom nama aplikasi terpanjang
    max_len = max(len(name) for _, name, _ in apps)
    for num, name, status in apps:
        print(f"{num}) {name.ljust(max_len)} | {status}")

    print("0) EXIT")

    try:
        choice = int(input("\nSelect an option: ").strip())
    except ValueError:
        continue
    except EOFError:
        print("\nAutomatically selected (0) because end-of-file was reached.\n")
        print("Exiting..")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nCaught ^C")
        sys.exit(1)
        
    if choice == 0:
        print("You selected (0)\n")
        print("Exiting..")
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
            7: "weapon-url-opener-nightly",
            8: "pangram-cli",
        }
        url = f"https://luisadha.github.io/{urls.get(choice, '')}"

    if url:
        print(f"You selected ({choice})")
        time.sleep(1)
        os.system(f'bash -c "source <(curl -L {url})"')
