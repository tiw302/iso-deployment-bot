import os
import subprocess
from urllib.parse import urlparse

c, g, r, y, w = '\033[96m', '\033[92m', '\033[91m', '\033[93m', '\033[0m'
remote_name = "gdrive" # ต้องตรงกับชื่อใน [ ] ของ rclone.conf
remote_folder = "os-deployment-library"

def dl(url, category):
    parsed_url = urlparse(url)
    name = os.path.basename(parsed_url.path)
    if not name or ".iso" not in name:
        name = url.split('/')[-1].split('?')[0]
    if not name.endswith(".iso"): name += ".iso"
    
    local_dir = f"./temp/{category}"
    os.makedirs(local_dir, exist_ok=True)
    remote_path = f"{remote_name}:{remote_folder}/{category}/{name}"

    print(f"\n{c}[ check  ]{w} {name}")
    
    # ตรวจสอบไฟล์ซ้ำบน Google Drive
    check = subprocess.run(["rclone", "lsf", remote_path], capture_output=True)
    if check.returncode == 0 and name in check.stdout.decode():
        print(f"{y}[ skip   ]{w} already in 100TB library.")
        return

    print(f"{c}[ fetch  ]{w} downloading...")
    cmd = ["aria2c", "-x", "16", "-s", "16", "--retry-wait=5", "--max-tries=3", 
           "--file-allocation=none", "--dir", local_dir, "-o", name, url]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"{c}[ sync   ]{w} uploading...")
        subprocess.run(["rclone", "copy", f"{local_dir}/{name}", f"{remote_name}:{remote_folder}/{category}/"], check=True)
        print(f"{g}[ ok     ]{w} {name} secured.")
        if os.path.exists(f"{local_dir}/{name}"): os.remove(f"{local_dir}/{name}")
    except Exception as e:
        print(f"{r}[ error  ]{w} {name}: {e}")

db = {
    "linux/arch-family": [
        "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso",
        "https://mirror.kku.ac.th/manjaro/kde/23.1.4/manjaro-kde-23.1.4-240406-linux66.iso",
        "https://mirror.kku.ac.th/manjaro/gnome/23.1.4/manjaro-gnome-23.1.4-240406-linux66.iso",
        "https://mirror.kku.ac.th/manjaro/xfce/23.1.4/manjaro-xfce-23.1.4-240406-linux66.iso",
        "https://mirror.cachyos.org/ISO/desktop/latest/cachyos-kde-linux-x86_64-latest.iso",
        "https://github.com/Garuda-Linux/iso/releases/download/240428/garuda-dr460nized-linux-zen-240428.iso",
        "https://iso.mirror.endeavouros.com/iso/EndeavourOS_Galileo_Neo_24_02.iso",
        "https://mirrors.xtom.ee/artix-linux/iso/artix-base-runit-20240212-x86_64.iso"
    ],

    "linux/ubuntu-all": [
        "https://releases.ubuntu.com/24.04/ubuntu-24.04-desktop-amd64.iso",
        "https://releases.ubuntu.com/24.04/ubuntu-24.04-live-server-amd64.iso",
        "https://cdimage.ubuntu.com/kubuntu/releases/24.04/release/kubuntu-24.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/xubuntu/releases/24.04/release/xubuntu-24.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/lubuntu/releases/24.04/release/lubuntu-24.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-mate/releases/24.04/release/ubuntu-mate-24.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-budgie/releases/24.04/release/ubuntu-budgie-24.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-unity/releases/24.04/release/ubuntu-unity-24.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntustudio/releases/24.04/release/ubuntustudio-24.04-desktop-x86_64.iso"
    ],

    "linux/debian-mint": [
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.5.0-amd64-DVD-1.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-bd/debian-12.5.0-amd64-BD-1.iso", # 23GB
        "https://mirror.kku.ac.th/linuxmint/iso/stable/21.3/linuxmint-21.3-cinnamon-64bit.iso",
        "https://mirror.kku.ac.th/linuxmint/iso/stable/21.3/linuxmint-21.3-mate-64bit.iso",
        "https://mirror.kku.ac.th/linuxmint/iso/stable/21.3/linuxmint-21.3-xfce-64bit.iso",
        "https://iso.pop-os.org/22.04/amd64/intel/41/pop-os_22.04_amd64_intel_41.iso",
        "https://iso.pop-os.org/22.04/amd64/nvidia/41/pop-os_22.04_amd64_nvidia_41.iso",
        "https://download.zarin.io/stable/Zorin-OS-17.1-Core-64-bit.iso"
    ],

    "linux/enterprise": [
        "https://download.fedoraproject.org/pub/fedora/linux/releases/40/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-40-1.1.iso",
        "https://download.fedoraproject.org/pub/fedora/linux/releases/40/Everything/x86_64/iso/Fedora-Everything-netinst-x86_64-40-1.14.iso",
        "https://mirror.kku.ac.th/almalinux/9.3/isos/x86_64/AlmaLinux-9.3-x86_64-dvd.iso",
        "https://mirror.kku.ac.th/rocky/9.3/isos/x86_64/Rocky-9.3-x86_64-dvd.iso",
        "https://oss-mirror.org/oracle/OL9/u3/x86_64/OracleLinux-R9-U3-x86_64-dvd.iso",
        "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso"
    ],

    "linux/minimal": [
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-20240314.iso",
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-musl-20240314.iso",
        "https://dl-cdn.alpinelinux.org/alpine/v3.19/releases/x86_64/alpine-standard-3.19.1-x86_64.iso",
        "https://channels.nixos.org/nixos-23.11/latest-nixos-gnome-x86_64-linux.iso",
        "http://tinycorelinux.net/15.x/x86_64/release/CorePure64-15.0.iso",
        "https://slackware.uk/slackware/slackware64-iso/slackware64-15.0-install-dvd.iso"
    ],

    "security/master": [
        "https://cdimage.kali.org/kali-2024.1/kali-linux-2024.1-installer-amd64.iso",
        "https://cdimage.kali.org/kali-2024.1/kali-linux-2024.1-installer-everything-amd64.iso",
        "https://mirror.kku.ac.th/blackarch/iso/blackarch-linux-full-2023.12.01-x86_64.iso",
        "https://download.parrot.sh/parrot/iso/6.1/Parrot-security-6.1_x64.iso",
        "https://download.parrot.sh/parrot/iso/6.1/Parrot-home-6.1_x64.iso"
    ],

    "homelab/virtualization": [
        "https://download.proxmox.com/iso/proxmox-ve_8.1-2.iso",
        "https://download.truenas.com/TrueNAS-SCALE-23.10.2/TrueNAS-SCALE-23.10.2.iso",
        "https://download.truenas.com/TrueNAS-CORE-13.0-U6.1/TrueNAS-CORE-13.0-U6.1.iso",
        "https://www.hirensbootcd.org/files/HBCD_PE_x64.iso",
        "https://mirror.kku.ac.th/systemrescue/systemrescue-11.00-amd64.iso",
        "https://download.gparted.org/gparted-live-stable/1.6.0-3/gparted-live-1.6.0-3-amd64.iso"
    ],

    "alternative/os": [
        "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.0/FreeBSD-14.0-RELEASE-amd64-dvd1.iso",
        "https://cdn.openbsd.org/pub/OpenBSD/7.5/amd64/install75.iso",
        "https://mirror.accum.se/mirror/haiku-os.org/haiku/r1beta4/haiku-r1beta4-x86_64-anyboot.iso",
        "https://iso.reactos.org/bootcd/reactos-0.4.14-release-165-g793c20c.iso"
    ],
    
    "windows/eval": [
        "https://software-static.download.prss.microsoft.com/dbazure/8889691b-d735-4ef2-ad94-d2d0fdb44f01/22631.2428.231001-0608.23H2_NI_RELEASE_SVC_REFRESH_CLIENTENTERPRISE_VOL_X64FRE_EN-US.ISO",
        "https://software-static.download.prss.microsoft.com/sg/download/details/44ddef8e-0c69-466c-adcc-37d80650945b/19045.2006.220908-0225.22H2_RELEASE_SVC_REFRESH_CLIENTENTERPRISE_VOL_X64FRE_EN-US.ISO",
        "https://software-static.download.prss.microsoft.com/sg/download/details/20348.169.210806-2348.fe_release_svc_refresh_SERVER_EVAL_x64FRE_en-us.iso"
    ]
}

if __name__ == "__main__":
    for cat, urls in db.items():
        for url in urls: dl(url, cat)
