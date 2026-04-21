import os
import subprocess

C, G, R, Y, W = '\033[96m', '\033[92m', '\033[91m', '\033[93m', '\033[0m'
REMOTE_BASE = "gdrive:os-deployment-library"

def dl(url, category):
    name = url.split('/')[-1].split('?')[0]
    local_dir = f"./temp/{category}"
    os.makedirs(local_dir, exist_ok=True)
    remote_path = f"{REMOTE_BASE}/{category}/{name}"

    print(f"{C}[ CHECK  ]{W} {name}")
    
    # Check if exists
    check = subprocess.run(["rclone", "lsf", remote_path], capture_output=True)
    if check.returncode == 0 and name in check.stdout.decode():
        print(f"{Y}[ SKIP   ]{W} {name}")
        return

    print(f"{C}[ FETCH  ]{W} {name}...")
    # Add --retry-wait to handle network hiccups
    cmd = [
        "aria2c", "-x", "16", "-s", "16", "--retry-wait=5", "-m=0",
        "--auto-file-renaming=false", "--dir", local_dir, "-o", name, url
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"{C}[ UPLOAD ]{W} {name} to cloud...")
        # Use copy instead of move for safety during testing
        subprocess.run(["rclone", "copy", f"{local_dir}/{name}", f"{REMOTE_BASE}/{category}/"], check=True)
        print(f"{G}[  OK    ]{W} {name} synced")
        # Cleanup local after upload
        os.remove(f"{local_dir}/{name}")
    except Exception as e:
        print(f"{R}[ ERROR  ]{W} {name} failed")

db = {
    "Linux-Distros/Arch-Based": [
        "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso",
        "https://mirror.isoc.or.th/manjaro/kde/25.0/manjaro-kde-25.0-64bit.iso",
        "https://iso.mirror.endeavouros.com/iso/EndeavourOS_Galileo_Neo_24_04.iso"
    ],
    "Linux-Distros/Debian-Based": [
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.9.0-amd64-DVD-1.iso",
        "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-desktop-amd64.iso",
        "https://mirrors.layeronline.com/linuxmint/stable/22.1/linuxmint-22.1-cinnamon-64bit.iso"
    ],
    "Linux-Distros/RedHat-Based": [
        "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-43-1.1.iso",
        "https://mirrors.xtom.jp/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-dvd.iso"
    ],
    "Security-Pentest": [
        "https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-installer-amd64.iso",
        "https://deb.parrot.sh/parrot/iso/7.0/Parrot-security-7.0_amd64.iso",
        "https://mirror.accum.se/mirror/blackarch/iso/blackarch-linux-full-2025.12.01-x86_64.iso"
    ],
    "Windows-Evaluation": [
        "https://software-static.download.prss.microsoft.com/dblo/9813/Win11_24H2_English_x64v3.iso",
        "https://software-static.download.prss.microsoft.com/sg/download/evalcenter/Win11_24H2_English_x64_Enterprise.iso"
    ]
}

if __name__ == "__main__":
    for cat, urls in db.items():
        for url in urls: dl(url, cat)
