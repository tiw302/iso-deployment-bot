import os
import subprocess
from urllib.parse import urlparse

# terminal colors
c, g, r, y, w = '\033[96m', '\033[92m', '\033[91m', '\033[93m', '\033[0m'

# remote name must match the one in your rclone.conf
remote_base = "gdrive:os-deployment-library"

def dl(url, category):
    # strip query strings for clean filename
    parsed_url = urlparse(url)
    name = os.path.basename(parsed_url.path)
    if not name.endswith('.iso'):
        name += '.iso'
        
    local_dir = f"./temp/{category}"
    os.makedirs(local_dir, exist_ok=True)
    remote_path = f"{remote_base}/{category}/{name}"

    print(f"\n{c}[ check  ]{w} {name}")
    
    # query rclone to avoid duplicates
    check = subprocess.run(["rclone", "lsf", remote_path], capture_output=True)
    if check.returncode == 0 and name in check.stdout.decode():
        print(f"{y}[ skip   ]{w} {name} exists on remote.")
        return

    print(f"{c}[ fetch  ]{w} downloading...")
    # --file-allocation=none is safer for github runner disk
    cmd = [
        "aria2c", "-x", "16", "-s", "16", "--retry-wait=5", "--max-tries=0",
        "--auto-file-renaming=false", "--file-allocation=none", 
        "--dir", local_dir, "-o", name, url
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"{c}[ sync   ]{w} uploading to school drive...")
        subprocess.run(["rclone", "copy", f"{local_dir}/{name}", f"{remote_base}/{category}/"], check=True)
        print(f"{g}[ ok     ]{w} {name} synced.")
        os.remove(f"{local_dir}/{name}")
    except Exception as e:
        print(f"{r}[ error  ]{w} {name}: {e}")
        if os.path.exists(f"{local_dir}/{name}"):
            os.remove(f"{local_dir}/{name}")

db = {
    "linux-distros/arch-based": [
        "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso",
        "https://mirror.kku.ac.th/manjaro/kde/24.0.0/manjaro-kde-24.0.0-240513-linux69.iso"
    ],
    "linux-distros/debian-ubuntu": [
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.5.0-amd64-DVD-1.iso",
        "https://mirror.kku.ac.th/ubuntu-releases/24.04/ubuntu-24.04-desktop-amd64.iso"
    ],
    "massive-offline-packages": [
        "https://cdimage.kali.org/kali-2024.1/kali-linux-2024.1-everything-amd64.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-bd/debian-mac-12.5.0-amd64-BD-1.iso"
    ]
}

if __name__ == "__main__":
    print(f"{c}[ system ]{w} init sync protocol (school drive 100tb mode)")
    for cat, urls in db.items():
        for url in urls: 
            dl(url, cat)
    print(f"{g}[ system ]{w} sync completed.")
