import os
import subprocess
from urllib.parse import urlparse

# terminal colors
c, g, r, y, w = '\033[96m', '\033[92m', '\033[91m', '\033[93m', '\033[0m'

# configure your remote rclone destination here
remote_base = "gdrive:os-deployment-library"

def dl(url, category):
    # strip query strings to ensure clean filename
    parsed_url = urlparse(url)
    name = os.path.basename(parsed_url.path)
    
    if not name.endswith('.iso'):
        name += '.iso'
        
    local_dir = f"./temp/{category}"
    os.makedirs(local_dir, exist_ok=True)
    remote_path = f"{remote_base}/{category}/{name}"

    print(f"\n{c}[ check  ]{w} {name}")
    
    # query rclone to prevent redundant downloads
    check = subprocess.run(["rclone", "lsf", remote_path], capture_output=True)
    if check.returncode == 0 and name in check.stdout.decode():
        print(f"{y}[ skip   ]{w} {name} already exists on remote.")
        return

    print(f"{c}[ fetch  ]{w} downloading payload...")
    
    # --file-allocation=none prevents disk lockups on massive files
    cmd = [
        "aria2c", "-x", "16", "-s", "16", "--retry-wait=5", "--max-tries=0",
        "--auto-file-renaming=false", "--file-allocation=none", 
        "--dir", local_dir, "-o", name, url
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"{c}[ sync   ]{w} uploading {name} to cloud...")
        
        subprocess.run(["rclone", "copy", f"{local_dir}/{name}", f"{remote_base}/{category}/"], check=True)
        print(f"{g}[ ok     ]{w} {name} synced successfully.")
        
        # cleanup local storage to free up space
        os.remove(f"{local_dir}/{name}")
        
    except Exception as e:
        print(f"{r}[ error  ]{w} {name} process failed: {e}")
        if os.path.exists(f"{local_dir}/{name}"):
            os.remove(f"{local_dir}/{name}")

db = {
    "linux-distros/arch-based": [
        "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso",
        "https://mirror.cachyos.org/ISO/desktop/latest/cachyos-desktop-linux-x86_64-latest.iso",
        "https://iso.mirror.endeavouros.com/iso/latest/EndeavourOS-latest.iso",
        "https://mirror.kku.ac.th/manjaro/kde/latest/manjaro-kde-latest.iso",
        "https://garudalinux.org/downloads/garuda/dr460nized/garuda-dr460nized-linux-zen-latest.iso"
    ],
    "linux-distros/independent-and-minimal": [
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-musl-latest.iso",
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-latest.iso",
        "https://dl-cdn.alpinelinux.org/alpine/latest-stable/releases/x86_64/alpine-standard-3.19.1-x86_64.iso",
        "https://channels.nixos.org/nixos-23.11/latest-nixos-gnome-x86_64-linux.iso"
    ],
    "linux-distros/debian-based": [
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.5.0-amd64-DVD-1.iso",
        "https://mirror.kku.ac.th/ubuntu-releases/24.04/ubuntu-24.04-desktop-amd64.iso",
        "https://mirror.kku.ac.th/ubuntu-releases/24.04/ubuntu-24.04-live-server-amd64.iso",
        "https://mirror.kku.ac.th/linuxmint/stable/21.3/linuxmint-21.3-cinnamon-64bit.iso",
        "https://iso.pop-os.org/22.04/amd64/intel/41/pop-os_22.04_amd64_intel_41.iso"
    ],
    "linux-distros/redhat-fedora": [
        "https://mirror.kku.ac.th/fedora/linux/releases/40/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-40-1.14.iso",
        "https://mirror.kku.ac.th/fedora/linux/releases/40/Server/x86_64/iso/Fedora-Server-dvd-x86_64-40-1.14.iso",
        "https://mirror.kku.ac.th/almalinux/9/isos/x86_64/AlmaLinux-9-latest-x86_64-dvd.iso",
        "https://mirror.kku.ac.th/rocky/9/isos/x86_64/Rocky-9-latest-x86_64-dvd.iso"
    ],
    "security-pentest": [
        "https://cdimage.kali.org/kali-2024.1/kali-linux-2024.1-installer-amd64.iso",
        "https://deb.parrot.sh/parrot/iso/6.0/Parrot-security-6.0_amd64.iso",
        "https://mirror.kku.ac.th/blackarch/iso/blackarch-linux-full-2023.12.01-x86_64.iso"
    ],
    "homelab-and-rescue": [
        "https://enterprise.proxmox.com/iso/proxmox-ve_8.1-2.iso",
        "https://download.truenas.com/TrueNAS-SCALE-23.10.2/TrueNAS-SCALE-23.10.2.iso",
        "https://mirror.kku.ac.th/systemrescue/systemrescue-11.00-amd64.iso",
        "https://github.com/HirenBootCD/HBCD_PE_x64/releases/download/v1.0.2/HBCD_PE_x64.iso"
    ],
    "massive-offline-packages": [
        "https://cdimage.kali.org/kali-2024.1/kali-linux-2024.1-everything-amd64.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-bd/debian-mac-12.5.0-amd64-BD-1.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-bd/debian-mac-12.5.0-amd64-BD-2.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-bd/debian-mac-12.5.0-amd64-BD-3.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-bd/debian-mac-12.5.0-amd64-BD-4.iso",
        "https://mirror.kku.ac.th/centos/8-stream/isos/x86_64/CentOS-Stream-8-x86_64-latest-dvd1.iso",
        "https://mirrors.edge.kernel.org/opensuse/distribution/leap/15.5/iso/openSUSE-Leap-15.5-DVD-x86_64-Media.iso"
    ]
}

if __name__ == "__main__":
    print(f"\n{c}[ system ]{w} initializing sync protocol...")
    
    for cat, urls in db.items():
        for url in urls: 
            dl(url, cat)
            
    print(f"\n{g}[ system ]{w} sync completed.")
