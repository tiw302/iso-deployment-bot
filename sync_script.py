# Updated at 2026-04-22

import os
import subprocess
from urllib.parse import urlparse

c, g, r, y, w = '\033[96m', '\033[92m', '\033[91m', '\033[93m', '\033[0m'
remote_name = "gdrive"
remote_folder = "os-deployment-library"

def dl(url, category):
    parsed_url = urlparse(url)
    name = os.path.basename(parsed_url.path)
    if not name or ".iso" not in name:
        name = url.split('/')[-1].split('?')[0]
    if not name.endswith(".iso"):
        name += ".iso"

    local_dir = f"./temp/{category}"
    os.makedirs(local_dir, exist_ok=True)
    remote_path = f"{remote_name}:{remote_folder}/{category}/{name}"

    print(f"\n{c}[ check  ]{w} {name}")

    check = subprocess.run(["rclone", "lsf", remote_path], capture_output=True)
    if check.returncode == 0 and name in check.stdout.decode():
        print(f"{y}[ skip   ]{w} already in library.")
        return

    print(f"{c}[ fetch  ]{w} downloading...")
    cmd = [
        "aria2c", "-x", "16", "-s", "16",
        "--retry-wait=5", "--max-tries=3",
        "--file-allocation=none",
        "--check-certificate=false",
        "--dir", local_dir, "-o", name, url
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"{c}[ sync   ]{w} uploading...")
        subprocess.run([
            "rclone", "copy", "-P",
            f"{local_dir}/{name}",
            f"{remote_name}:{remote_folder}/{category}/"
        ], check=True)
        print(f"{g}[ ok     ]{w} {name} secured.")
        if os.path.exists(f"{local_dir}/{name}"):
            os.remove(f"{local_dir}/{name}")
    except Exception as e:
        print(f"{r}[ error  ]{w} {name}: {e}")

db = {
    "linux/arch-family": [
        "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso",
        "https://download.manjaro.org/kde/24.1.2/manjaro-kde-24.1.2-241216-linux612.iso",
        "https://download.manjaro.org/gnome/24.1.2/manjaro-gnome-24.1.2-241216-linux612.iso",
        "https://download.manjaro.org/xfce/24.1.2/manjaro-xfce-24.1.2-241216-linux612.iso",
        "https://mirror.cachyos.org/ISO/kde/latest/cachyos-kde-linux-x86_64-latest.iso",
        "https://mirror.cachyos.org/ISO/gnome/latest/cachyos-gnome-linux-x86_64-latest.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-base-openrc-20241201-x86_64.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-base-runit-20241201-x86_64.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-plasma-openrc-20241201-x86_64.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-cinnamon-openrc-20241201-x86_64.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-kde-openrc-20241201-x86_64.iso",
    ],

    "linux/ubuntu-noble": [
        "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-desktop-amd64.iso",
        "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-live-server-amd64.iso",
        "https://cdimage.ubuntu.com/kubuntu/releases/24.04.2/release/kubuntu-24.04.2-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/xubuntu/releases/24.04.2/release/xubuntu-24.04.2-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/lubuntu/releases/24.04.2/release/lubuntu-24.04.2-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-mate/releases/24.04.2/release/ubuntu-mate-24.04.2-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-budgie/releases/24.04.2/release/ubuntu-budgie-24.04.2-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-unity/releases/24.04.2/release/ubuntu-unity-24.04.2-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntustudio/releases/24.04.2/release/ubuntustudio-24.04.2-dvd-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-cinnamon/releases/24.04.2/release/ubuntu-cinnamon-24.04.2-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/edubuntu/releases/24.04.2/release/edubuntu-24.04.2-desktop-amd64.iso",
    ],

    "linux/ubuntu-jammy": [
        "https://releases.ubuntu.com/22.04.5/ubuntu-22.04.5-desktop-amd64.iso",
        "https://releases.ubuntu.com/22.04.5/ubuntu-22.04.5-live-server-amd64.iso",
        "https://cdimage.ubuntu.com/kubuntu/releases/22.04.5/release/kubuntu-22.04.5-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/xubuntu/releases/22.04.5/release/xubuntu-22.04.5-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/lubuntu/releases/22.04.5/release/lubuntu-22.04.5-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-mate/releases/22.04.5/release/ubuntu-mate-22.04.5-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-budgie/releases/22.04.5/release/ubuntu-budgie-22.04.5-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntustudio/releases/22.04.5/release/ubuntustudio-22.04.5-dvd-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-cinnamon/releases/22.04.5/release/ubuntu-cinnamon-22.04.5-desktop-amd64.iso",
    ],

    "linux/ubuntu-plucky": [
        "https://releases.ubuntu.com/25.04/ubuntu-25.04-desktop-amd64.iso",
        "https://releases.ubuntu.com/25.04/ubuntu-25.04-live-server-amd64.iso",
        "https://cdimage.ubuntu.com/kubuntu/releases/25.04/release/kubuntu-25.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/xubuntu/releases/25.04/release/xubuntu-25.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/lubuntu/releases/25.04/release/lubuntu-25.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-mate/releases/25.04/release/ubuntu-mate-25.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-budgie/releases/25.04/release/ubuntu-budgie-25.04-desktop-amd64.iso",
    ],

    "linux/debian": [
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.9.0-amd64-DVD-1.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.9.0-amd64-DVD-2.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.9.0-amd64-DVD-3.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.9.0-amd64-netinst.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.9.0-amd64-gnome.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.9.0-amd64-kde.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.9.0-amd64-xfce.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.9.0-amd64-lxqt.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.9.0-amd64-cinnamon.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.9.0-amd64-mate.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.9.0-amd64-standard.iso",
    ],

    "linux/mint": [
        "https://ftp.linuxmint.com/stable/22.1/linuxmint-22.1-cinnamon-64bit.iso",
        "https://ftp.linuxmint.com/stable/22.1/linuxmint-22.1-mate-64bit.iso",
        "https://ftp.linuxmint.com/stable/22.1/linuxmint-22.1-xfce-64bit.iso",
        "https://ftp.linuxmint.com/stable/21.3/linuxmint-21.3-cinnamon-64bit.iso",
        "https://ftp.linuxmint.com/stable/21.3/linuxmint-21.3-mate-64bit.iso",
        "https://ftp.linuxmint.com/stable/21.3/linuxmint-21.3-xfce-64bit.iso",
        "https://mirror.kku.ac.th/linuxmint/iso/stable/22.1/linuxmint-22.1-cinnamon-64bit.iso",
        "https://mirror.kku.ac.th/linuxmint/iso/stable/22.1/linuxmint-22.1-mate-64bit.iso",
        "https://mirror.kku.ac.th/linuxmint/iso/stable/22.1/linuxmint-22.1-xfce-64bit.iso",
    ],

    "linux/debian-based": [
        "https://iso.pop-os.org/22.04/amd64/intel/42/pop-os_22.04_amd64_intel_42.iso",
        "https://iso.pop-os.org/22.04/amd64/nvidia/42/pop-os_22.04_amd64_nvidia_42.iso",
        "https://downloads.zorinos.com/17/Zorin-OS-17.2-Core-64-bit.iso",
        "https://downloads.zorinos.com/17/Zorin-OS-17.2-Lite-64-bit.iso",
        "https://downloads.zorinos.com/17/Zorin-OS-17.2-Education-64-bit.iso",
        "https://downloads.elementary.io/os-8.0-stable.20241001.iso",
        "https://sourceforge.net/projects/mxlinux/files/Final/MX-23.5/MX-23.5_x64.iso",
        "https://sourceforge.net/projects/mxlinux/files/Final/MX-23.5/MX-23.5-kde_x64.iso",
        "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.1/antiX-23.1_x64-full.iso",
        "https://sourceforge.net/projects/sparkylinux/files/7.5/sparkylinux-7.5-x86_64-lxqt.iso",
        "https://sourceforge.net/projects/sparkylinux/files/7.5/sparkylinux-7.5-x86_64-kde.iso",
        "https://cdimage.ubuntu.com/ubuntu-cinnamon/releases/24.04.2/release/ubuntu-cinnamon-24.04.2-desktop-amd64.iso",
    ],

    "linux/enterprise": [
        "https://download.fedoraproject.org/pub/fedora/linux/releases/42/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-42-1.1.iso",
        "https://download.fedoraproject.org/pub/fedora/linux/releases/42/Server/x86_64/iso/Fedora-Server-dvd-x86_64-42-1.1.iso",
        "https://download.fedoraproject.org/pub/fedora/linux/releases/42/Everything/x86_64/iso/Fedora-Everything-netinst-x86_64-42-1.1.iso",
        "https://mirror.kku.ac.th/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-dvd.iso",
        "https://mirror.kku.ac.th/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-minimal.iso",
        "https://mirror.kku.ac.th/rocky/9.5/isos/x86_64/Rocky-9.5-x86_64-dvd.iso",
        "https://mirror.kku.ac.th/rocky/9.5/isos/x86_64/Rocky-9.5-x86_64-minimal.iso",
        "https://yum.oracle.com/ISOS/OracleLinux/OL9/u5/x86_64/OracleLinux-R9-U5-x86_64-dvd.iso",
        "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso",
        "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-DVD-x86_64-Media.iso",
        "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-GNOME-Live-x86_64-Media.iso",
        "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-KDE-Live-x86_64-Media.iso",
        "https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso",
        "https://mirror.stream.centos.org/10-stream/BaseOS/x86_64/iso/CentOS-Stream-10-latest-x86_64-dvd1.iso",
    ],

    "linux/fedora-spins": [
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-KDE-Live-x86_64-42-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-Xfce-Live-x86_64-42-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-Cinnamon-Live-x86_64-42-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-LXDE-Live-x86_64-42-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-LXQt-Live-x86_64-42-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-MATE_Compiz-Live-x86_64-42-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-Sway-Live-x86_64-42-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-i3-Live-x86_64-42-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-Budgie-Live-x86_64-42-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-Cosmic-Live-x86_64-42-1.1.iso",
    ],

    "linux/immutable": [
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Silverblue/x86_64/iso/Fedora-Silverblue-ostree-x86_64-42-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Kinoite/x86_64/iso/Fedora-Kinoite-ostree-x86_64-42-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Sericea/x86_64/iso/Fedora-Sericea-ostree-x86_64-42-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Onyx/x86_64/iso/Fedora-Onyx-ostree-x86_64-42-1.1.iso",
        "https://download.opensuse.org/distribution/microos/iso/openSUSE-MicroOS-DVD-x86_64-Current.iso",
    ],

    "linux/minimal": [
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-20241201.iso",
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-musl-20241201.iso",
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-xfce-20241201.iso",
        "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-standard-3.21.0-x86_64.iso",
        "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-extended-3.21.0-x86_64.iso",
        "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-virt-3.21.0-x86_64.iso",
        "https://channels.nixos.org/nixos-24.11/latest-nixos-gnome-x86_64-linux.iso",
        "https://channels.nixos.org/nixos-24.11/latest-nixos-plasma6-x86_64-linux.iso",
        "https://channels.nixos.org/nixos-24.11/latest-nixos-minimal-x86_64-linux.iso",
        "http://tinycorelinux.net/15.x/x86_64/release/CorePure64-15.0.iso",
        "http://tinycorelinux.net/15.x/x86/release/TinyCore-current.iso",
        "https://slackware.uk/slackware/slackware64-15.0/slackware64-15.0-install-dvd.iso",
        "https://gentoo.osuosl.org/releases/amd64/autobuilds/current-livegui-amd64/livegui-amd64.iso",
    ],

    "linux/lightweight": [
        "https://sourceforge.net/projects/mxlinux/files/Final/MX-23.5/MX-23.5_x64.iso",
        "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.1/antiX-23.1_x64-full.iso",
        "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.1/antiX-23.1_x64-base.iso",
        "https://downloads.sourceforge.net/project/puppy/puppy/9.5/fossapup64-9.5.iso",
        "https://sourceforge.net/projects/linuxlite/files/6.8/linux-lite-6.8-64bit.iso",
        "https://sourceforge.net/projects/bodhilinux/files/7.0.0/bodhi-7.0.0-64.iso",
        "https://sourceforge.net/projects/lxle-os/files/LXLE22.04.3/lxle-22.04.3-64-bit.iso",
        "https://sourceforge.net/projects/q4osinux/files/q4os-5.8-amd64.r1.iso",
        "https://sourceforge.net/projects/porteus/files/Porteus-v5.0-x86_64.iso",
        "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-standard-3.21.0-x86_64.iso",
    ],

    "linux/gaming": [
        "https://download.bazzite.gg/Bazzite-stable.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-Gaming-Live-x86_64-42-1.1.iso",
        "https://nobara-images.nobaraproject.org/Nobara-42-Official-2025-04-01.iso",
        "https://chimeraos.org/images/latest/chimera-latest.iso",
    ],

    "linux/security": [
        "https://cdimage.kali.org/kali-2025.1/kali-linux-2025.1-installer-amd64.iso",
        "https://cdimage.kali.org/kali-2025.1/kali-linux-2025.1-installer-everything-amd64.iso",
        "https://cdimage.kali.org/kali-2025.1/kali-linux-2025.1-live-amd64.iso",
        "https://mirrors.dotsrc.org/kali-images/kali-2025.1/kali-linux-2025.1-installer-amd64.iso",
        "https://ftp.nluug.nl/os/Linux/distr/parrotsec/iso/6.2/Parrot-security-6.2_x64.iso",
        "https://ftp.nluug.nl/os/Linux/distr/parrotsec/iso/6.2/Parrot-home-6.2_x64.iso",
        "https://www.backbox.org/download/backbox-9-desktop-amd64.iso",
        "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-DVD-x86_64-Media.iso",
    ],

    "linux/privacy": [
        "https://tails.net/torrents/files/tails-amd64-6.11.img",
        "https://ftp.qubes-os.org/iso/Qubes-R4.2.3-x86_64.iso",
        "https://download.whonix.org/ova/17.2.3.7/Whonix-Xfce-17.2.3.7.ova",
    ],

    "linux/education": [
        "https://cdimage.ubuntu.com/edubuntu/releases/24.04.2/release/edubuntu-24.04.2-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/edubuntu/releases/22.04.5/release/edubuntu-22.04.5-desktop-amd64.iso",
        "https://ftp.skolelinux.com/skolelinux/debian-edu-12+edu2-CD.iso",
        "https://download.sugarlabs.org/releases/14.0/sugar-live-build.iso",
        "https://downloads.zorinos.com/17/Zorin-OS-17.2-Education-64-bit.iso",
        "https://www.edubuntu.org/download/edubuntu-24.04.2-desktop-amd64.iso",
    ],

    "linux/multimedia": [
        "https://cdimage.ubuntu.com/ubuntustudio/releases/24.04.2/release/ubuntustudio-24.04.2-dvd-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntustudio/releases/22.04.5/release/ubuntustudio-22.04.5-dvd-amd64.iso",
        "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-DVD-x86_64-Media.iso",
        "https://sourceforge.net/projects/doudoulinux/files/DoudouLinux-2012.iso",
    ],

    "linux/server": [
        "https://mirror.kku.ac.th/ubuntu-cd/24.04.2/ubuntu-24.04.2-live-server-amd64.iso",
        "https://mirror.kku.ac.th/ubuntu-cd/22.04.5/ubuntu-22.04.5-live-server-amd64.iso",
        "https://mirror.kku.ac.th/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-dvd.iso",
        "https://mirror.kku.ac.th/rocky/9.5/isos/x86_64/Rocky-9.5-x86_64-dvd.iso",
        "https://download.fedoraproject.org/pub/fedora/linux/releases/42/Server/x86_64/iso/Fedora-Server-dvd-x86_64-42-1.1.iso",
        "https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.9.0-amd64-netinst.iso",
        "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-DVD-x86_64-Media.iso",
    ],

    "homelab/virtualization": [
        "https://download.proxmox.com/iso/proxmox-ve_8.3-1.iso",
        "https://updates.xcp-ng.org/isos/8.3.0/xcp-ng-8.3.0.iso",
        "https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso",
        "https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/3.2.0-5/clonezilla-live-3.2.0-5-amd64.iso",
        "https://sourceforge.net/projects/drbl/files/drbl_stable/2.32.1/drbl-live-stable-2.32.1-amd64.iso",
    ],

    "homelab/nas": [
        "https://download.truenas.com/TrueNAS-SCALE-24.10.2/TrueNAS-SCALE-24.10.2.iso",
        "https://download.truenas.com/TrueNAS-CORE-13.0-U6.2/TrueNAS-CORE-13.0-U6.2.iso",
        "https://sourceforge.net/projects/openmediavault/files/7.4.7/openmediavault_7.4.7-amd64.iso",
        "https://sourceforge.net/projects/rockstor/files/5.0.15-0/Rockstor-5.0.15-0-x86_64.iso",
        "https://sourceforge.net/projects/amahi/files/hda7.iso",
    ],

    "homelab/networking": [
        "https://frafiles.netgate.com/mirror/downloads/pfSense-CE-2.7.2-RELEASE-amd64.iso.gz",
        "https://mirror.opnsense.org/releases/24.7/OPNsense-24.7-dvd-amd64.iso",
        "https://downloads.ipfire.org/releases/ipfire-2.x/2.29-core190/ipfire-2.29.x86_64-full-core190.iso",
        "https://downloads.vyos.io/release/stream/equuleus/1.3.9/VyOS-1.3.9-amd64.iso",
        "https://sourceforge.net/projects/ipcop/files/IPCop-2.1.9-install-cd.i486.iso",
        "https://ftp.hosteurope.de/mirror/ftp.zeroshell.net/cdrom/ZeroShell-3.9.5-x86_64.iso",
    ],

    "recovery/tools": [
        "https://mirror.kku.ac.th/systemrescue/systemrescue-11.03-amd64.iso",
        "https://download.gparted.org/gparted-live-stable/1.6.0-10/gparted-live-1.6.0-10-amd64.iso",
        "https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/3.2.0-5/clonezilla-live-3.2.0-5-amd64.iso",
        "https://www.hirensbootcd.org/files/HBCD_PE_x64.iso",
        "https://download.rescuezilla.com/rescuezilla-2.5.0-64bit.iso",
        "https://www.ultimatebootcd.com/download/ubcd556.iso",
        "https://boot.netboot.xyz/ipxe/netboot.xyz.iso",
        "https://sourceforge.net/projects/qt-fsarchiver/files/qt-fsarchiver-18.06.3-x86_64.iso",
        "https://f2.tdlp.in.th/systemrescue/systemrescue-11.03-amd64.iso",
    ],

    "alternative/bsd": [
        "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-amd64-dvd1.iso",
        "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-amd64-disc1.iso",
        "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-amd64-memstick.img",
        "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/13.4/FreeBSD-13.4-RELEASE-amd64-dvd1.iso",
        "https://cdn.openbsd.org/pub/OpenBSD/7.6/amd64/install76.iso",
        "https://ftp.netbsd.org/pub/NetBSD/NetBSD-10.0/images/NetBSD-10.0-amd64.iso",
        "https://mirror.dragonflybsd.org/iso-images/dfly-x86_64-6.4.0_REL.iso",
        "https://mirror.accum.se/mirror/haiku-os.org/haiku/r1beta5/haiku-r1beta5-x86_64-anyboot.iso",
        "https://ghostbsd.org/releases/amd64/24.10.1/GhostBSD-24.10.1.iso",
        "https://iso.reactos.org/bootcd/reactos-0.4.15-release.iso",
        "https://www.midnightbsd.org/ftp/pub/MidnightBSD/MidnightBSD-3.2.0-RELEASE-amd64-disc1.iso",
    ],

    "windows/eval": [
        "https://software-static.download.prss.microsoft.com/dbazure/8889691b-d735-4ef2-ad94-d2d0fdb44f01/22631.2428.231001-0608.23H2_NI_RELEASE_SVC_REFRESH_CLIENTENTERPRISE_VOL_X64FRE_EN-US.ISO",
        "https://software-static.download.prss.microsoft.com/sg/download/details/44ddef8e-0c69-466c-adcc-37d80650945b/19045.2006.220908-0225.22H2_RELEASE_SVC_REFRESH_CLIENTENTERPRISE_VOL_X64FRE_EN-US.ISO",
        "https://software-static.download.prss.microsoft.com/sg/download/details/20348.169.210806-2348.fe_release_svc_refresh_SERVER_EVAL_x64FRE_en-us.iso",
        "https://go.microsoft.com/fwlink/p/?LinkID=2208844&clcid=0x409&culture=en-us&country=us",
    ],
}

if __name__ == "__main__":
    for cat, urls in db.items():
        for url in urls:
            dl(url, cat)
