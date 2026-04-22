import os
import subprocess
from urllib.parse import urlparse

# terminal colors
c, g, r, y, w = '\033[96m', '\033[92m', '\033[91m', '\033[0m'

# remote name must match the one in your rclone.conf
remote_base = "gdrive:os-deployment-library"

def dl(url, category):
    parsed_url = urlparse(url)
    name = os.path.basename(parsed_url.path)
    if not name:
        name = "downloaded_file.iso"
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
    cmd = [
        "aria2c", "-x", "16", "-s", "16", "--retry-wait=5", "--max-tries=0",
        "--auto-file-renaming=false", "--file-allocation=none", 
        "--dir", local_dir, "-o", name, url
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"{c}[ sync   ]{w} uploading to school drive (100TB mode)...")
        subprocess.run(["rclone", "copy", f"{local_dir}/{name}", f"{remote_base}/{category}/"], check=True)
        print(f"{g}[ ok     ]{w} {name} synced successfully.")
        if os.path.exists(f"{local_dir}/{name}"):
            os.remove(f"{local_dir}/{name}")
    except Exception as e:
        print(f"{r}[ error  ]{w} {name}: {e}")
        if os.path.exists(f"{local_dir}/{name}"):
            os.remove(f"{local_dir}/{name}")

# ISO Database - Top Distros & Heavy Packages
db = {
    "linux-distros/arch-family": [
        "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso",
        "https://mirror.kku.ac.th/manjaro/kde/23.1.4/manjaro-kde-23.1.4-240406-linux66.iso",
        "https://github.com/Garuda-Linux/iso/releases/download/240428/garuda-dr460nized-linux-zen-240428.iso"
    ],
    "linux-distros/debian-ubuntu": [
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.5.0-amd64-DVD-1.iso",
        "https://mirror.kku.ac.th/ubuntu-releases/24.04/ubuntu-24.04-desktop-amd64.iso",
        "https://mirror.kku.ac.th/linuxmint/iso/stable/21.3/linuxmint-21.3-cinnamon-64bit.iso"
    ],
    "linux-distros/fedora-suse": [
        "https://download.fedoraproject.org/pub/fedora/linux/releases/40/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-40-1.1.iso",
        "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso"
    ],
    "massive-packages/security": [
        "https://cdimage.kali.org/kali-2024.1/kali-linux-2024.1-installer-everything-amd64.iso", # ตัวใหญ่พิเศษ 10GB+
        "https://download.parrot.sh/parrot/iso/6.1/Parrot-security-6.1_x64.iso"
    ],
    "massive-packages/offline-repo": [
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-bd/debian-12.5.0-amd64-BD-1.iso", # Blu-ray ISO ใหญ่มาก
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.5.0-amd64-DVD-2.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.5.0-amd64-DVD-3.iso"
    ]
}

if __name__ == "__main__":
    print(f"{c}[ system ]{w} starting master sync for 100TB library")
    for cat, urls in db.items():
        for url in urls: 
            dl(url, cat)
    print(f"\n{g}[ system ]{w} all tasks completed.")
