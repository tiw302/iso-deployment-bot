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

db = { # iso link
    "linux-distros/arch-based": [
        "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso",
        "https://mirror.isoc.or.th/manjaro/kde/25.0/manjaro-kde-25.0-64bit.iso",
        "https://iso.mirror.endeavouros.com/iso/EndeavourOS_Galileo_Neo_24_04.iso",
        "https://mirrors.n0p.me/cachyos/desktop/260101/cachyos-desktop-linux-260101.iso",
        "https://garudalinux.org/downloads/garuda/dr460nized/garuda-dr460nized-linux-zen-250210.iso"
    ],
    "linux-distros/debian-based": [
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.9.0-amd64-DVD-1.iso",
        "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-desktop-amd64.iso",
        "https://mirrors.layeronline.com/linuxmint/stable/22.1/linuxmint-22.1-cinnamon-64bit.iso",
        "https://download.popos.org/iso/22.04/amd64/intel/41/pop-os_22.04_amd64_intel_41.iso",
        "https://mirrors.edge.kernel.org/mx-linux/MX-23.5_x64.iso",
        "https://download.astralinux.ru/astra/stable/2.12_common_edition/iso/astra-1.7.5-22.08.2023_14.47.iso"
    ],
    "linux-distros/redhat-fedora": [
        "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-43-1.1.iso",
        "https://mirrors.xtom.jp/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-dvd.iso",
        "https://download.rockylinux.org/pub/rocky/9/isos/x86_64/Rocky-9.5-x86_64-dvd.iso"
    ],
    "security-pentest": [
        "https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-installer-amd64.iso",
        "https://deb.parrot.sh/parrot/iso/7.0/Parrot-security-7.0_amd64.iso",
        "https://mirror.accum.se/mirror/blackarch/iso/blackarch-linux-full-2025.12.01-x86_64.iso",
        "https://mirrors.ocf.berkeley.edu/pentoo/Pentoo_Full_x86_64_2024.0.iso"
    ],
    "windows-evaluation": [
        "https://software-static.download.prss.microsoft.com/dblo/9813/Win11_24H2_English_x64v3.iso",
        "https://software-static.download.prss.microsoft.com/sg/download/evalcenter/Win11_24H2_English_x64_Enterprise.iso",
        "https://software-static.download.prss.microsoft.com/sg/download/evalcenter/WinServer2025-English-Final.iso"
    ],
    "rescue-and-others": [
        "https://github.com/HirenBootCD/HBCD_PE_x64/releases/download/v1.0.2/HBCD_PE_x64.iso",
        "https://ftp.nluug.nl/pub/os/Linux/distr/systemrescuecd/systemrescue-11.00-amd64.iso",
        "https://download.proxmox.com/iso/proxmox-ve_8.3-1.iso",
        "https://images.linuxcontainers.org/images/openwrt/23.05/amd64/default/20240421_07%3A45/config.iso"
    ]
}

if __name__ == "__main__":
    for cat, urls in db.items():
        for url in urls: dl(url, cat)
