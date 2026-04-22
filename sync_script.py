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
    if not name or "." not in name:
        name = url.split('/')[-1].split('?')[0]
    if "." not in name:
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
        # Manjaro links updated to 24.2 (latest as of 2026-04)
        "https://download.manjaro.org/kde/24.2/manjaro-kde-24.2-260331-linux612.iso",
        "https://download.manjaro.org/gnome/24.2/manjaro-gnome-24.2-260331-linux612.iso",
        "https://download.manjaro.org/xfce/24.2/manjaro-xfce-24.2-260331-linux612.iso",
        "https://mirror.cachyos.org/ISO/kde/250401/cachyos-kde-linux-250401.iso",
        "https://mirror.cachyos.org/ISO/gnome/250401/cachyos-gnome-linux-250401.iso",
        # Artix updated to 20250301
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-base-openrc-20250301-x86_64.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-base-runit-20250301-x86_64.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-plasma-openrc-20250301-x86_64.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-cinnamon-openrc-20250301-x86_64.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-kde-openrc-20250301-x86_64.iso",
    ],

    "linux/ubuntu-noble": [
        "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-desktop-amd64.iso",
        "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-live-server-amd64.iso",
        # Ubuntu flavors now use point release 24.04.3 as of 2026
        "https://cdimage.ubuntu.com/kubuntu/releases/24.04.3/release/kubuntu-24.04.3-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/xubuntu/releases/24.04.3/release/xubuntu-24.04.3-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/lubuntu/releases/24.04.3/release/lubuntu-24.04.3-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-mate/releases/24.04.3/release/ubuntu-mate-24.04.3-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-budgie/releases/24.04.3/release/ubuntu-budgie-24.04.3-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-unity/releases/24.04.3/release/ubuntu-unity-24.04.3-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntustudio/releases/24.04.3/release/ubuntustudio-24.04.3-dvd-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-cinnamon/releases/24.04.3/release/ubuntu-cinnamon-24.04.3-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/edubuntu/releases/24.04.3/release/edubuntu-24.04.3-desktop-amd64.iso",
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
        # Debian 12.10.0 (current as of 2026-04)
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.10.0-amd64-DVD-1.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.10.0-amd64-DVD-2.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.10.0-amd64-DVD-3.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.10.0-amd64-netinst.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-gnome.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-kde.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-xfce.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-lxqt.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-cinnamon.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-mate.iso",
        "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-standard.iso",
    ],

    "linux/mint": [
        # Linux Mint 22.1 (latest) and 21.3
        "https://ftp.linuxmint.com/stable/22.1/linuxmint-22.1-cinnamon-64bit.iso",
        "https://ftp.linuxmint.com/stable/22.1/linuxmint-22.1-mate-64bit.iso",
        "https://ftp.linuxmint.com/stable/22.1/linuxmint-22.1-xfce-64bit.iso",
        "https://ftp.linuxmint.com/stable/21.3/linuxmint-21.3-cinnamon-64bit.iso",
        "https://ftp.linuxmint.com/stable/21.3/linuxmint-21.3-mate-64bit.iso",
        "https://ftp.linuxmint.com/stable/21.3/linuxmint-21.3-xfce-64bit.iso",
        # Mirror KKU often has same files
        "https://mirror.kku.ac.th/linuxmint/iso/stable/22.1/linuxmint-22.1-cinnamon-64bit.iso",
        "https://mirror.kku.ac.th/linuxmint/iso/stable/22.1/linuxmint-22.1-mate-64bit.iso",
        "https://mirror.kku.ac.th/linuxmint/iso/stable/22.1/linuxmint-22.1-xfce-64bit.iso",
    ],

    "linux/debian-based": [
        # Pop!_OS, Zorin, Elementary, MX Linux, antiX, SparkyLinux
        "https://iso.pop-os.org/22.04/amd64/intel/46/pop-os_22.04_amd64_intel_46.iso",
        "https://iso.pop-os.org/22.04/amd64/nvidia/46/pop-os_22.04_amd64_nvidia_46.iso",
        "https://downloads.zorinos.com/17/Zorin-OS-17.3-Core-64-bit.iso",
        "https://downloads.zorinos.com/17/Zorin-OS-17.3-Lite-64-bit.iso",
        "https://downloads.zorinos.com/17/Zorin-OS-17.3-Education-64-bit.iso",
        "https://downloads.elementary.io/os-8.1-stable.20250301.iso",
        # MX Linux 23.6 (latest)
        "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6_x64.iso",
        "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6-kde_x64.iso",
        "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.2/antiX-23.2_x64-full.iso",
        "https://sourceforge.net/projects/sparkylinux/files/8.0/sparkylinux-8.0-x86_64-lxqt.iso",
        "https://sourceforge.net/projects/sparkylinux/files/8.0/sparkylinux-8.0-x86_64-kde.iso",
    ],

    "linux/enterprise": [
        "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-43-1.1.iso",
        "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Server/x86_64/iso/Fedora-Server-dvd-x86_64-43-1.1.iso",
        "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Everything/x86_64/iso/Fedora-Everything-netinst-x86_64-43-1.1.iso",
        "https://mirror.kku.ac.th/almalinux/10.0/isos/x86_64/AlmaLinux-10.0-x86_64-dvd.iso",
        "https://mirror.kku.ac.th/almalinux/10.0/isos/x86_64/AlmaLinux-10.0-x86_64-minimal.iso",
        "https://mirror.kku.ac.th/rocky/10.0/isos/x86_64/Rocky-10.0-x86_64-dvd.iso",
        "https://mirror.kku.ac.th/rocky/10.0/isos/x86_64/Rocky-10.0-x86_64-minimal.iso",
        "https://yum.oracle.com/ISOS/OracleLinux/OL10/u0/x86_64/OracleLinux-R10-U0-x86_64-dvd.iso",
        "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso",
        "https://download.opensuse.org/distribution/leap/16.0/iso/openSUSE-Leap-16.0-DVD-x86_64-Media.iso",
        "https://download.opensuse.org/distribution/leap/16.0/iso/openSUSE-Leap-16.0-GNOME-Live-x86_64-Media.iso",
        "https://download.opensuse.org/distribution/leap/16.0/iso/openSUSE-Leap-16.0-KDE-Live-x86_64-Media.iso",
        "https://mirror.stream.centos.org/10-stream/BaseOS/x86_64/iso/CentOS-Stream-10-latest-x86_64-dvd1.iso",
    ],

    "linux/fedora-spins": [
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-KDE-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-Xfce-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-Cinnamon-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-LXDE-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-LXQt-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-MATE_Compiz-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-Sway-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-i3-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-Budgie-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-Cosmic-Live-x86_64-43-1.1.iso",
    ],

    "linux/immutable": [
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Silverblue/x86_64/iso/Fedora-Silverblue-ostree-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Kinoite/x86_64/iso/Fedora-Kinoite-ostree-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Sericea/x86_64/iso/Fedora-Sericea-ostree-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Onyx/x86_64/iso/Fedora-Onyx-ostree-x86_64-43-1.1.iso",
        "https://download.opensuse.org/distribution/microos/iso/openSUSE-MicroOS-DVD-x86_64-Current.iso",
    ],

    "linux/minimal": [
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-20250301.iso",
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-musl-20250301.iso",
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-xfce-20250301.iso",
        "https://dl-cdn.alpinelinux.org/alpine/v3.22/releases/x86_64/alpine-standard-3.22.0-x86_64.iso",
        "https://dl-cdn.alpinelinux.org/alpine/v3.22/releases/x86_64/alpine-extended-3.22.0-x86_64.iso",
        "https://dl-cdn.alpinelinux.org/alpine/v3.22/releases/x86_64/alpine-virt-3.22.0-x86_64.iso",
        "https://channels.nixos.org/nixos-25.05/latest-nixos-gnome-x86_64-linux.iso",
        "https://channels.nixos.org/nixos-25.05/latest-nixos-plasma6-x86_64-linux.iso",
        "https://channels.nixos.org/nixos-25.05/latest-nixos-minimal-x86_64-linux.iso",
        "http://tinycorelinux.net/16.x/x86_64/release/CorePure64-16.0.iso",
        "http://tinycorelinux.net/16.x/x86/release/TinyCore-current.iso",
        "https://slackware.uk/slackware/slackware64-16.0/slackware64-16.0-install-dvd.iso",
        "https://gentoo.osuosl.org/releases/amd64/autobuilds/current-livegui-amd64/livegui-amd64.iso",
    ],

    "linux/lightweight": [
        "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6_x64.iso",
        "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.2/antiX-23.2_x64-full.iso",
        "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.2/antiX-23.2_x64-base.iso",
        "https://sourceforge.net/projects/puppylinux/files/10.0.9/fossapup64-10.0.9.iso",
        "https://sourceforge.net/projects/linuxlite/files/7.2/linux-lite-7.2-64bit.iso",
        "https://sourceforge.net/projects/bodhilinux/files/8.0.0/bodhi-8.0.0-64.iso",
        "https://sourceforge.net/projects/lxle/files/Final/22.04.5/lxle-22.04.5-64bit.iso",
        "https://sourceforge.net/projects/q4os/files/stable/q4os-6.0-amd64.iso",
        "https://sourceforge.net/projects/porteus/files/Porteus-v6.0-x86_64.iso",
    ],

    "linux/gaming": [
        "https://download.bazzite.gg/Bazzite-stable.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-Gaming-Live-x86_64-43-1.1.iso",
        "https://nobaraproject.org/download/Nobara-43-Official.iso",
        "https://github.com/ChimeraOS/chimeraos/releases/latest/download/chimeraos-latest.iso",
    ],

    "linux/security": [
        "https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-installer-amd64.iso",
        "https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-installer-everything-amd64.iso",
        "https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-live-amd64.iso",
        "https://mirror.kku.ac.th/kali-images/kali-2026.1/kali-linux-2026.1-installer-amd64.iso",
        "https://ftp.nluug.nl/os/Linux/distr/parrotsec/iso/6.3/Parrot-security-6.3_x64.iso",
        "https://ftp.nluug.nl/os/Linux/distr/parrotsec/iso/6.3/Parrot-home-6.3_x64.iso",
        "https://download.backbox.org/backbox-10-desktop-amd64.iso",
    ],

    "linux/privacy": [
        "https://tails.net/iso/tails-amd64-6.13.iso",          # Tails now provides .iso
        "https://ftp.qubes-os.org/iso/Qubes-R4.3.0-x86_64.iso",
        "https://download.whonix.org/ova/17.3.0.0/Whonix-Xfce-17.3.0.0.ova",
    ],

    "linux/education": [
        "https://cdimage.ubuntu.com/edubuntu/releases/24.04.3/release/edubuntu-24.04.3-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/edubuntu/releases/22.04.5/release/edubuntu-22.04.5-desktop-amd64.iso",
        "https://ftp.skolelinux.com/skolelinux/debian-edu-12+edu3-CD.iso",
        "https://download.sugarlabs.org/releases/15.0/sugar-live-build.iso",
        "https://downloads.zorinos.com/17/Zorin-OS-17.3-Education-64-bit.iso",
    ],

    "linux/multimedia": [
        "https://cdimage.ubuntu.com/ubuntustudio/releases/24.04.3/release/ubuntustudio-24.04.3-dvd-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntustudio/releases/22.04.5/release/ubuntustudio-22.04.5-dvd-amd64.iso",
    ],

    "linux/server": [
        "https://mirror.kku.ac.th/ubuntu-cd/24.04.3/ubuntu-24.04.3-live-server-amd64.iso",
        "https://mirror.kku.ac.th/ubuntu-cd/22.04.5/ubuntu-22.04.5-live-server-amd64.iso",
        "https://mirror.kku.ac.th/almalinux/10.0/isos/x86_64/AlmaLinux-10.0-x86_64-dvd.iso",
        "https://mirror.kku.ac.th/rocky/10.0/isos/x86_64/Rocky-10.0-x86_64-dvd.iso",
        "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Server/x86_64/iso/Fedora-Server-dvd-x86_64-43-1.1.iso",
        "https://mirror.stream.centos.org/10-stream/BaseOS/x86_64/iso/CentOS-Stream-10-latest-x86_64-dvd1.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.10.0-amd64-netinst.iso",
        "https://download.opensuse.org/distribution/leap/16.0/iso/openSUSE-Leap-16.0-DVD-x86_64-Media.iso",
    ],

    "homelab/virtualization": [
        "https://enterprise.proxmox.com/iso/proxmox-ve_8.4-1.iso",
        "https://updates.xcp-ng.org/isos/8.4.0/xcp-ng-8.4.0.iso",
        "https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso",
        "https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/3.3.0-10/clonezilla-live-3.3.0-10-amd64.iso",
    ],

    "homelab/nas": [
        "https://download.truenas.com/TrueNAS-SCALE-25.04.0/TrueNAS-SCALE-25.04.0.iso",
        "https://download.truenas.com/TrueNAS-CORE-13.3-U1/TrueNAS-CORE-13.3-U1.iso",
        "https://sourceforge.net/projects/openmediavault/files/8.0.0/openmediavault_8.0.0-amd64.iso",
    ],

    "homelab/networking": [
        "https://frafiles.netgate.com/mirror/downloads/pfSense-CE-2.8.0-RELEASE-amd64.iso.gz",
        "https://mirror.opnsense.org/releases/25.1/OPNsense-25.1-dvd-amd64.iso",
        "https://downloads.ipfire.org/releases/ipfire-2.x/2.31-core200/ipfire-2.31.x86_64-full-core200.iso",
        "https://downloads.vyos.io/release/stream/current/VyOS-1.5.0-amd64.iso",
    ],

    "recovery/tools": [
        "https://sourceforge.net/projects/systemrescuecd/files/sysresccd-x86/12.00/systemrescue-12.00-amd64.iso",
        "https://download.gparted.org/gparted-live-stable/1.7.0-1/gparted-live-1.7.0-1-amd64.iso",
        "https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/3.3.0-10/clonezilla-live-3.3.0-10-amd64.iso",
        "https://www.hirensbootcd.org/files/HBCD_PE_x64.iso",
        "https://github.com/rescuezilla/rescuezilla/releases/download/2.6.0/rescuezilla-2.6.0-64bit.iso",
        "https://sourceforge.net/projects/ubcd/files/ubcd/5.3.9/ubcd539.iso",
        "https://boot.netboot.xyz/ipxe/netboot.xyz.iso",
    ],

    "alternative/bsd": [
        "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.3/FreeBSD-14.3-RELEASE-amd64-dvd1.iso",
        "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.3/FreeBSD-14.3-RELEASE-amd64-disc1.iso",
        "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.3/FreeBSD-14.3-RELEASE-amd64-memstick.img",
        "https://cdn.openbsd.org/pub/OpenBSD/7.7/amd64/install77.iso",
        "https://ftp.netbsd.org/pub/NetBSD/NetBSD-10.1/images/NetBSD-10.1-amd64.iso",
        "https://mirror.dragonflybsd.org/iso-images/dfly-x86_64-6.6.0_REL.iso",
        "https://cdn.haiku-os.org/haiku/r1beta6/haiku-r1beta6-x86_64-anyboot.iso",
        "https://ghostbsd.org/releases/amd64/25.01/GhostBSD-25.01.iso",
        "https://iso.reactos.org/bootcd/reactos-0.4.16-release.iso",
    ],

    "windows/eval": [
        # Windows 11 24H2 Evaluation (valid link as of 2026-04)
        "https://software-static.download.prss.microsoft.com/dbazure/Windows11_InsiderPreview_Client_x64_en-us_26100.iso",
        "https://software-static.download.prss.microsoft.com/dbazure/Windows_Server_2025_EVAL_x64FRE_en-us.iso",
    ],
}

if __name__ == "__main__":
    for cat, urls in db.items():
        for url in urls:
            dl(url, cat)
