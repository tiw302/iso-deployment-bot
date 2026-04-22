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
    
    # check if exists
    check = subprocess.run(["rclone", "lsf", remote_path], capture_output=True)
    if check.returncode == 0 and name in check.stdout.decode():
        print(f"{Y}[ SKIP   ]{W} {name}")
        return

    print(f"{C}[ FETCH  ]{W} {name}...")
    # add --retry-wait to handle network hiccups
    cmd = [
        "aria2c", "-x", "16", "-s", "16", "--retry-wait=5", "-m=0",
        "--auto-file-renaming=false", "--dir", local_dir, "-o", name, url
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"{C}[ UPLOAD ]{W} {name} to cloud...")
        # use copy instead of move for safety during testing
        subprocess.run(["rclone", "copy", f"{local_dir}/{name}", f"{REMOTE_BASE}/{category}/"], check=True)
        print(f"{G}[  OK    ]{W} {name} synced")
        # cleanup local after upload
        os.remove(f"{local_dir}/{name}")
    except Exception as e:
        print(f"{R}[ ERROR  ]{W} {name} failed")

db = { # os link
    "linux-distros/arch-based": [
        "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso",
        "https://mirror.cachyos.org/ISO/desktop/latest/cachyos-desktop-linux-x86_64-latest.iso",
        "https://iso.mirror.endeavouros.com/iso/EndeavourOS_Galileo-Neo_2024.04.iso",
        "https://mirror.kku.ac.th/manjaro/kde/24.0.0/manjaro-kde-24.0.0-240513-linux69.iso",
        "https://garudalinux.org/downloads/garuda/dr460nized/garuda-dr460nized-linux-zen-240428.iso"
    ],
    "linux-distros/independent-and-minimal": [
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-musl-latest.iso",
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-latest.iso"
    ],
    "linux-distros/debian-based": [
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.5.0-amd64-DVD-1.iso",
        "https://mirror.kku.ac.th/ubuntu-releases/24.04/ubuntu-24.04-desktop-amd64.iso",
        "https://mirror.kku.ac.th/linuxmint/stable/21.3/linuxmint-21.3-cinnamon-64bit.iso",
        "https://iso.pop-os.org/22.04/amd64/intel/41/pop-os_22.04_amd64_intel_41.iso"
    ],
    "linux-distros/redhat-fedora": [
        "https://mirror.kku.ac.th/fedora/linux/releases/40/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-40-1.14.iso",
        "https://mirror.kku.ac.th/almalinux/9/isos/x86_64/AlmaLinux-9-latest-x86_64-dvd.iso",
        "https://mirror.kku.ac.th/rocky/9/isos/x86_64/Rocky-9-latest-x86_64-dvd.iso"
    ],
    "security-pentest": [
        "https://cdimage.kali.org/kali-2024.1/kali-linux-2024.1-installer-amd64.iso",
        "https://deb.parrot.sh/parrot/iso/6.0/Parrot-security-6.0_amd64.iso",
        "https://mirror.kku.ac.th/blackarch/iso/blackarch-linux-full-2023.12.01-x86_64.iso" 
    ],
    "rescue-and-others": [
        "https://github.com/HirenBootCD/HBCD_PE_x64/releases/download/v1.0.2/HBCD_PE_x64.iso",
        "https://mirror.kku.ac.th/systemrescue/systemrescue-11.00-amd64.iso",
        "https://enterprise.proxmox.com/iso/proxmox-ve_8.1-2.iso"
    ],
    "massive-offline-packages": [
        "https://cdimage.kali.org/kali-2024.1/kali-linux-2024.1-everything-amd64.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-bd/debian-mac-12.5.0-amd64-BD-1.iso",
        "https://mirror.kku.ac.th/centos/8-stream/isos/x86_64/CentOS-Stream-8-x86_64-latest-dvd1.iso"
    ]
}

if __name__ == "__main__":
    for cat, urls in db.items():
        for url in urls: dl(url, cat)
