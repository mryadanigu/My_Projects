#!/usr/bin/env python3

import subprocess

def install_dependencies():
    print("\n[*] Installing dependencies...\n")
    subprocess.run(["pip", "install", "requests", "beautifulsoup4", "tqdm", "colorama"])

def main():
    install_dependencies()
    print("\n[*] Setup complete!")

if __name__ == "__main__":
    main()

