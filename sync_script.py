# Updated at 2026-04-22

import os
import subprocess
from urllib.parse import urlparse
import shutil

c, g, r, y, w = '\033[96m', '\033[92m', '\033[91m', '\033[93m', '\033[0m'
remote_name = "gdrive"
remote_folder = "os-deployment-library"

SINGLE_STREAM_HOSTS = [
    "sourceforge.net",
    "downloads.sourceforge.net",
    "ftp.linuxmint.com",
    "downloads.zorinos.com",
    "download.gparted.org",
    "download.rescuezilla.com",
    "mirror.dragonflybsd.org",
    "frafiles.netgate.com",
    "mirror.opnsense.org",
    "www.ultimatebootcd.com",
    "software-static.download.prss.microsoft.com",
]

def is_single_stream(url):
    host = urlparse(url).netloc.lower()
    return any(h in host for h in SINGLE_STREAM_HOSTS)

def dl(url, category):
    parsed_url = urlparse(url)
    name = os.path.basename(parsed_url.path)
    if not name or "." not in name:
        name = url.split('/')[-1].split('?')[0]
    if "." not in name:
        name += ".iso"
    if name.endswith(".img"):
        name = name.replace(".img", ".img.iso")

    local_dir = f"./temp/{category}"
    os.makedirs(local_dir, exist_ok=True)
    local_file = os.path.join(local_dir, name)
    remote_path = f"{remote_name}:{remote_folder}/{category}/{name}"

    print(f"\n{c}[ check  ]{w} {name}")

    check = subprocess.run(["rclone", "lsf", remote_path], capture_output=True)
    if check.returncode == 0 and name in check.stdout.decode():
        print(f"{y}[ skip   ]{w} already in library.")
        return

    print(f"{c}[ fetch  ]{w} downloading...")

    if is_single_stream(url):
        cmd = [
            "aria2c", "-x", "1", "-s", "1",
            "--retry-wait=10", "--max-tries=5",
            "--file-allocation=none",
            "--check-certificate=false",
            "--allow-overwrite=true",
            "--auto-file-renaming=false",
            "--dir", local_dir, "-o", name, url
        ]
    else:
        cmd = [
            "aria2c", "-x", "16", "-s", "16",
            "--retry-wait=5", "--max-tries=3",
            "--file-allocation=none",
            "--check-certificate=false",
            "--allow-overwrite=true",
            "--auto-file-renaming=false",
            "--dir", local_dir, "-o", name, url
        ]

    try:
        subprocess.run(cmd, check=True)
        print(f"{c}[ sync   ]{w} uploading...")
        
        subprocess.run([
            "rclone", "move", "-P",
            local_file,
            f"{remote_name}:{remote_folder}/{category}/"
        ], check=True)
        
        print(f"{g}[ ok     ]{w} {name} secured.")
        
    except Exception as e:
        print(f"{r}[ error  ]{w} {name}: {e}")
    finally:
        if os.path.exists(local_file):
            os.remove(local_file)
        try:
            os.rmdir(local_dir)
        except:
            pass

db = {

    "linux/arch-family": [
        "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso",
        # Manjaro 24.2 (latest as of 2026-04)
        "https://download.manjaro.org/kde/24.2/manjaro-kde-24.2-260331-linux612.iso",
        "https://download.manjaro.org/gnome/24.2/manjaro-gnome-24.2-260331-linux612.iso",
        "https://download.manjaro.org/xfce/24.2/manjaro-xfce-24.2-260331-linux612.iso",
        # CachyOS 250401
        "https://mirror.cachyos.org/ISO/kde/250401/cachyos-kde-linux-250401.iso",
        "https://mirror.cachyos.org/ISO/gnome/250401/cachyos-gnome-linux-250401.iso",
        "https://mirror.cachyos.org/ISO/plasma/250401/cachyos-desktop-linux-250401.iso",
        # Artix 20250301
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-base-openrc-20250301-x86_64.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-base-runit-20250301-x86_64.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-plasma-openrc-20250301-x86_64.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-cinnamon-openrc-20250301-x86_64.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-kde-openrc-20250301-x86_64.iso",
        "https://mirrors.dotsrc.org/artix-linux/iso/artix-gnome-openrc-20250301-x86_64.iso",
        # EndeavourOS (latest release ISO)
        "https://mirror.alpix.eu/endeavouros/iso/EndeavourOS_Gemini-Nova_25.04.iso",
        # Garuda Linux
        "https://iso.builds.garudalinux.org/iso/latest/garuda/kde-lite/latest.iso",
        "https://iso.builds.garudalinux.org/iso/latest/garuda/dr460nized/latest.iso",
        "https://iso.builds.garudalinux.org/iso/latest/garuda/gnome/latest.iso",
        "https://iso.builds.garudalinux.org/iso/latest/garuda/xfce/latest.iso",
        # BlackArch (security + Arch)
        "https://ftp.halifax.rwth-aachen.de/blackarch/iso/blackarch-linux-full-2025.01.01-x86_64.iso",
        "https://ftp.halifax.rwth-aachen.de/blackarch/iso/blackarch-linux-slim-2025.01.01-x86_64.iso",
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
        "https://cdimage.ubuntu.com/ubuntu-kylin/releases/24.04.2/release/ukui-24.04.2-desktop-amd64.iso",
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
        "https://cdimage.ubuntu.com/edubuntu/releases/22.04.5/release/edubuntu-22.04.5-desktop-amd64.iso",
    ],

    "linux/ubuntu-plucky": [
        "https://releases.ubuntu.com/25.04/ubuntu-25.04-desktop-amd64.iso",
        "https://releases.ubuntu.com/25.04/ubuntu-25.04-live-server-amd64.iso",
        "https://cdimage.ubuntu.com/kubuntu/releases/25.04/release/kubuntu-25.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/xubuntu/releases/25.04/release/xubuntu-25.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/lubuntu/releases/25.04/release/lubuntu-25.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-mate/releases/25.04/release/ubuntu-mate-25.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-budgie/releases/25.04/release/ubuntu-budgie-25.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntu-cinnamon/releases/25.04/release/ubuntu-cinnamon-25.04-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntustudio/releases/25.04/release/ubuntustudio-25.04-dvd-amd64.iso",
        "https://cdimage.ubuntu.com/edubuntu/releases/25.04/release/edubuntu-25.04-desktop-amd64.iso",
    ],

    "linux/debian": [
        # Debian 12 Bookworm (stable/current symlink always resolves to latest point release)
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
        # Debian 13 Trixie (testing netinst – rolling)
        "https://cdimage.debian.org/cdimage/weekly-builds/amd64/iso-cd/debian-testing-amd64-netinst.iso",
    ],

    "linux/mint": [
        # Mint 22.1 (Ubuntu 24.04 base) via official FTP
        "https://ftp.linuxmint.com/stable/22.1/linuxmint-22.1-cinnamon-64bit.iso",
        "https://ftp.linuxmint.com/stable/22.1/linuxmint-22.1-mate-64bit.iso",
        "https://ftp.linuxmint.com/stable/22.1/linuxmint-22.1-xfce-64bit.iso",
        # Mint 21.3 (Ubuntu 22.04 base)
        "https://ftp.linuxmint.com/stable/21.3/linuxmint-21.3-cinnamon-64bit.iso",
        "https://ftp.linuxmint.com/stable/21.3/linuxmint-21.3-mate-64bit.iso",
        "https://ftp.linuxmint.com/stable/21.3/linuxmint-21.3-xfce-64bit.iso",
        # LMDE 7 (Debian base)
        "https://ftp.linuxmint.com/stable/lmde7/lmde-7-cinnamon-64bit.iso",
        "https://ftp.linuxmint.com/stable/lmde7/lmde-7-mate-64bit.iso",
        # KKU mirror (Thailand) fallback
        "https://mirror.kku.ac.th/linuxmint/iso/stable/22.1/linuxmint-22.1-cinnamon-64bit.iso",
        "https://mirror.kku.ac.th/linuxmint/iso/stable/22.1/linuxmint-22.1-mate-64bit.iso",
        "https://mirror.kku.ac.th/linuxmint/iso/stable/22.1/linuxmint-22.1-xfce-64bit.iso",
    ],

    "linux/debian-based": [
        # Pop!_OS 22.04 (System76)
        "https://iso.pop-os.org/22.04/amd64/intel/46/pop-os_22.04_amd64_intel_46.iso",
        "https://iso.pop-os.org/22.04/amd64/nvidia/46/pop-os_22.04_amd64_nvidia_46.iso",
        # Zorin OS 17.3
        "https://downloads.zorinos.com/17/Zorin-OS-17.3-Core-64-bit.iso",
        "https://downloads.zorinos.com/17/Zorin-OS-17.3-Lite-64-bit.iso",
        "https://downloads.zorinos.com/17/Zorin-OS-17.3-Education-64-bit.iso",
        # elementary OS 8.1
        "https://downloads.elementary.io/os-8.1-stable.20250301.iso",
        # MX Linux 23.6
        "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6_x64.iso/download",
        "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6-kde_x64.iso/download",
        # antiX 23.2
        "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.2/antiX-23.2_x64-full.iso/download",
        # SparkyLinux 8.0
        "https://sourceforge.net/projects/sparkylinux/files/8.0/sparkylinux-8.0-x86_64-lxqt.iso/download",
        "https://sourceforge.net/projects/sparkylinux/files/8.0/sparkylinux-8.0-x86_64-kde.iso/download",
        # KDE Neon (Ubuntu LTS base + latest KDE)
        "https://files.kde.org/neon/images/user/current/neon-user-current.iso",
        # Deepin 23
        "https://cdimage.deepin.com/releases/23.1/deepin-desktop-community-23.1-amd64.iso",
        # Trisquel 11 (fully free Ubuntu)
        "https://ftp.rediris.es/trisquel/iso/nabia/trisquel_11.0_amd64.iso",
        # PureOS 10 (Purism)
        "https://downloads.puri.sm/pureOS/10.0/PureOS-10.0-gnome-live.iso",
        # GNOME OS nightly (testing)
        "https://os.gnome.org/download/latest/gnome_os_installer_nightly_x86_64.iso",
        # Ubuntu Cinnamon 24.04.2
        "https://cdimage.ubuntu.com/ubuntu-cinnamon/releases/24.04.2/release/ubuntu-cinnamon-24.04.2-desktop-amd64.iso",
    ],

    "linux/enterprise": [
        # Fedora 43 Workstation / Server / Everything
        "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-43-1.1.iso",
        "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Server/x86_64/iso/Fedora-Server-dvd-x86_64-43-1.1.iso",
        "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Everything/x86_64/iso/Fedora-Everything-netinst-x86_64-43-1.1.iso",
        # AlmaLinux 9.5 (KKU mirror Thailand)
        "https://mirror.kku.ac.th/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-dvd.iso",
        "https://mirror.kku.ac.th/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-minimal.iso",
        # Rocky Linux 9.5
        "https://mirror.kku.ac.th/rocky/9.5/isos/x86_64/Rocky-9.5-x86_64-dvd.iso",
        "https://mirror.kku.ac.th/rocky/9.5/isos/x86_64/Rocky-9.5-x86_64-minimal.iso",
        # Oracle Linux 9.5
        "https://yum.oracle.com/ISOS/OracleLinux/OL9/u5/x86_64/OracleLinux-R9-U5-x86_64-dvd.iso",
        "https://yum.oracle.com/ISOS/OracleLinux/OL9/u5/x86_64/OracleLinux-R9-U5-x86_64-boot.iso",
        # CentOS Stream 9
        "https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso",
        "https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-boot.iso",
        # openSUSE Leap 15.6
        "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-DVD-x86_64-Media.iso",
        "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-GNOME-Live-x86_64-Media.iso",
        "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-KDE-Live-x86_64-Media.iso",
        # openSUSE Tumbleweed (rolling)
        "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso",
        "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-KDE-Live-x86_64-Current.iso",
        "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-GNOME-Live-x86_64-Current.iso",
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
        # Fedora Labs
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Scientific_KDE-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Security-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Design_suite-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Robotics_Suite-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Gaming-Live-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Jam_KDE-Live-x86_64-43-1.1.iso",
    ],

    "linux/immutable": [
        # Fedora Atomic
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Silverblue/x86_64/iso/Fedora-Silverblue-ostree-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Kinoite/x86_64/iso/Fedora-Kinoite-ostree-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Sericea/x86_64/iso/Fedora-Sericea-ostree-x86_64-43-1.1.iso",
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Onyx/x86_64/iso/Fedora-Onyx-ostree-x86_64-43-1.1.iso",
        # openSUSE MicroOS
        "https://download.opensuse.org/distribution/microos/iso/openSUSE-MicroOS-DVD-x86_64-Current.iso",
        # Vanilla OS 2
        "https://github.com/Vanilla-OS/os/releases/latest/download/vanillaos-2-desktop-amd64.iso",
        # NixOS (current stable)
        "https://channels.nixos.org/nixos-24.11/latest-nixos-gnome-x86_64-linux.iso",
        "https://channels.nixos.org/nixos-24.11/latest-nixos-plasma6-x86_64-linux.iso",
        # Endless OS
        "https://images.endlessos.com/reimage/endless-eos6.0.0-amd64-amd64.200-base.iso",
    ],

    "linux/rolling": [
        # Solus
        "https://mirrors.rit.edu/solus/images/4.6/Solus-4.6-Budgie.iso",
        "https://mirrors.rit.edu/solus/images/4.6/Solus-4.6-GNOME.iso",
        "https://mirrors.rit.edu/solus/images/4.6/Solus-4.6-Plasma.iso",
        # Void Linux (rolling)
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-20250201.iso",
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-musl-20250201.iso",
        "https://repo-default.voidlinux.org/live/current/void-live-x86_64-xfce-20250201.iso",
        # Devuan (Debian without systemd)
        "https://files.devuan.org/devuan_excalibur/installer-iso/devuan_excalibur_5.0.1_amd64_desktop.iso",
        "https://files.devuan.org/devuan_excalibur/installer-iso/devuan_excalibur_5.0.1_amd64_minimal-live.iso",
        # PCLinuxOS
        "https://ftp.nluug.nl/os/Linux/distr/pclinuxos/pclinuxos/live-cd/pclinuxos64-KDE-2024.12.iso",
        # Mageia
        "https://distrib-coffee.ipsl.jussieu.fr/pub/linux/Mageia/iso/9/Mageia-9-x86_64-DVD.iso",
        # OpenMandriva
        "https://sourceforge.net/projects/openmandriva/files/release/24.12/OpenMandriva-24.12-plasma6.x86_64.iso/download",
    ],

    "linux/minimal": [
        # Alpine Linux 3.21
        "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-standard-3.21.3-x86_64.iso",
        "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-extended-3.21.3-x86_64.iso",
        "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-virt-3.21.3-x86_64.iso",
        # NixOS 24.11
        "https://channels.nixos.org/nixos-24.11/latest-nixos-minimal-x86_64-linux.iso",
        # TinyCore
        "http://tinycorelinux.net/16.x/x86_64/release/CorePure64-16.0.iso",
        "http://tinycorelinux.net/16.x/x86/release/TinyCore-current.iso",
        # Slackware 15.0
        "https://slackware.uk/slackware/slackware64-15.0/slackware64-15.0-install-dvd.iso",
        # Gentoo Live GUI
        "https://gentoo.osuosl.org/releases/amd64/autobuilds/current-livegui-amd64/livegui-amd64.iso",
        # Funtoo Stage3 (meta-live)
        # Clear Linux (Intel)
        "https://cdn.download.clearlinux.org/releases/current/clear/clear-live.iso",
        # Bedrock Linux (meta-distro installer)
        "https://github.com/bedrocklinux/bedrocklinux-userspace/releases/latest/download/bedrock-linux-0.7.30-x86_64.sh",
        # Parabola GNU/Linux (free Arch)
        "https://redirector.parabolagnulinux.org/iso/2025.02/parabola-systemd-2025.02.01-netinstall-multilib-x86_64.iso",
        # Calculate Linux
        "https://www.calculate-linux.org/downloads/en/cld/amd64/current/cld-amd64.iso",
    ],

    "linux/lightweight": [
        # MX Linux 23.5 (Fluxbox edition)
        "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.5/MX-23.5_fluxbox_x64.iso/download",
        # antiX 23.1
        "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.1/antiX-23.1_x64-full.iso/download",
        "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.1/antiX-23.1_x64-base.iso/download",
        "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.1/antiX-23.1_x64-net.iso/download",
        # Puppy Linux
        "https://sourceforge.net/projects/puppylinux/files/puppy-fossa/fossapup64-9.5.iso/download",
        # Linux Lite 7.2
        "https://sourceforge.net/projects/linuxlite/files/7.2/linux-lite-7.2-64bit.iso/download",
        # Bodhi Linux 7.0
        "https://sourceforge.net/projects/bodhilinux/files/7.0.0/bodhi-7.0.0-64.iso/download",
        # LXLE 22.04
        "https://sourceforge.net/projects/lxle/files/LXLE22043/lxle-22043-64bit.iso/download",
        # Q4OS 5.8
        "https://sourceforge.net/projects/q4osinux/files/q4os-5.8-amd64.r1.iso/download",
        # Porteus 5.0
        "https://sourceforge.net/projects/porteus/files/Porteus-v5.0-x86_64.iso/download",
        # SliTaz 5.0 (mini 30MB)
        "https://mirror.slitaz.org/iso/5.0/slitaz-5.0.iso",
        # Absolute Linux
        "https://sourceforge.net/projects/absolute-linux/files/Absolute-15.0.19/absolute-15.0.19.iso/download",
        # Peppermint OS 12
        "https://peppermintos.com/iso/Peppermint-12-20240201-amd64.iso",
        # KNOPPIX 9.1
        "https://ftp.knoppix.nl/os/Linux/distr/knoppix/KNOPPIX_V9.1CD-2021-01-25-EN.iso",
    ],

    "linux/gaming": [
        # Bazzite (Fedora-atomic gaming)
        "https://download.bazzite.gg/Bazzite-stable.iso",
        # Fedora Gaming Spin
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Gaming-Live-x86_64-43-1.1.iso",
        # Nobara (Fedora gaming-patched)
        "https://nobara-images.nobaraproject.org/Nobara-43-Official-2025-10-01.iso",
        # ChimeraOS (SteamOS-like)
        "https://chimeraos.org/images/latest/chimera-latest.iso",
        # Drauger OS 7.6
        "https://draugeros.org/iso/drauger-os-7.6-amd64.iso",
        # Lakka (RetroArch-based console)
        "https://le-builds.lakka.tv/Generic.x86_64/Lakka-Generic.x86_64-5.0.iso",
        # Batocera Linux v40
        "https://mirrors.o2switch.fr/batocera/x86_64/stable/last/batocera-x86_64-40.img.gz",
        # RetroPie (x86 build)
        "https://downloads.retropie.org.uk/RetroPie-x86/retropie-buster-4.8-x86.iso",
    ],

    "linux/security": [
        # Kali Linux 2025.1
        "https://cdimage.kali.org/kali-2025.1/kali-linux-2025.1-installer-amd64.iso",
        "https://cdimage.kali.org/kali-2025.1/kali-linux-2025.1-installer-everything-amd64.iso",
        "https://cdimage.kali.org/kali-2025.1/kali-linux-2025.1-live-amd64.iso",
        # KKU mirror (Thailand)
        "https://mirror.kku.ac.th/kali-images/kali-2025.1/kali-linux-2025.1-installer-amd64.iso",
        # Parrot Security 6.2
        "https://ftp.nluug.nl/os/Linux/distr/parrotsec/iso/6.2/Parrot-security-6.2_x64.iso",
        "https://ftp.nluug.nl/os/Linux/distr/parrotsec/iso/6.2/Parrot-home-6.2_x64.iso",
        # BackBox 9
        "https://releases.backbox.org/backbox-9-desktop-amd64.iso",
        # CAINE 14 (Computer-Aided INvestigation)
        "https://www.caine-live.net/pages/downloadcaine14.html",  # use direct if available
        # REMnux 7 (malware analysis)
        "https://remnux.org/downloads/remnux-v7-focal-ova.iso",
        # DEFT Zero 2018.2 (digital forensics)
        "https://sourceforge.net/projects/deft/files/DEFT-Zero/2018.2/deft-zero-2018.2.iso/download",
        # Pentoo 2024.0 (Gentoo-based security)
        "https://sourceforge.net/projects/pentoo/files/Pentoo/2024.0/pentoo-amd64-2024.0.iso/download",
    ],

    "linux/privacy": [
        # Tails 6.11 (now ships .iso)
        "https://tails.net/torrents/files/tails-amd64-6.13.iso",
        # Qubes OS 4.2.3
        "https://ftp.qubes-os.org/iso/Qubes-R4.2.3-x86_64.iso",
        # Whonix 17.2.3.7
        "https://download.whonix.org/ova/17.2.3.7/Whonix-Xfce-17.2.3.7.ova",
        # Kodachi 9 (privacy live)
        "https://sourceforge.net/projects/linuxkodachi/files/kodachi-9-64.iso/download",
        # heads (QubesOS variant)
        # Subgraph OS (discontinued but archived)
    ],

    "linux/education": [
        "https://cdimage.ubuntu.com/edubuntu/releases/24.04.2/release/edubuntu-24.04.2-desktop-amd64.iso",
        "https://cdimage.ubuntu.com/edubuntu/releases/22.04.5/release/edubuntu-22.04.5-desktop-amd64.iso",
        "https://ftp.skolelinux.com/skolelinux/debian-edu-12+edu2-CD.iso",
        "https://download.sugarlabs.org/releases/14.0/sugar-live-build.iso",
        "https://downloads.zorinos.com/17/Zorin-OS-17.3-Education-64-bit.iso",
        # Fedora Education
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Robotics_Suite-Live-x86_64-43-1.1.iso",
        # OpenSUSE Education
        "https://download.opensuse.org/education/release/42.3/openSUSE-Edu-li-f-e-42.3-0-i586_x86_64.iso",
        # UberStudent 5.1
        "https://sourceforge.net/projects/uberstudent/files/UberStudent/5.1/UberStudent-5.1-Athena-amd64.iso/download",
    ],

    "linux/multimedia": [
        "https://cdimage.ubuntu.com/ubuntustudio/releases/24.04.2/release/ubuntustudio-24.04.2-dvd-amd64.iso",
        "https://cdimage.ubuntu.com/ubuntustudio/releases/22.04.5/release/ubuntustudio-22.04.5-dvd-amd64.iso",
        # AV Linux MXE 2023
        "https://sourceforge.net/projects/avlinux/files/2023.11.19/AV_Linux_MXE_2023.11.19_x86_64.iso/download",
        # Fedora Jam (audio production)
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Jam_KDE-Live-x86_64-43-1.1.iso",
        # KXStudio (professional audio)
        "https://downloads.sourceforge.net/project/kxstudio/Releases/KXStudio_14.04.5_amd64.iso",
        # Fedora Design Suite
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Design_suite-Live-x86_64-43-1.1.iso",
    ],

    "linux/server": [
        "https://mirror.kku.ac.th/ubuntu-cd/24.04.2/ubuntu-24.04.2-live-server-amd64.iso",
        "https://mirror.kku.ac.th/ubuntu-cd/22.04.5/ubuntu-22.04.5-live-server-amd64.iso",
        "https://releases.ubuntu.com/25.04/ubuntu-25.04-live-server-amd64.iso",
        "https://mirror.kku.ac.th/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-dvd.iso",
        "https://mirror.kku.ac.th/rocky/9.5/isos/x86_64/Rocky-9.5-x86_64-dvd.iso",
        "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Server/x86_64/iso/Fedora-Server-dvd-x86_64-43-1.1.iso",
        "https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso",
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.10.0-amd64-netinst.iso",
        # Debian 11 Bullseye (still LTS)
        "https://cdimage.debian.org/cdimage/archive/11.11.0/amd64/iso-cd/debian-11.11.0-amd64-netinst.iso",
        # openSUSE Leap server
        "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-DVD-x86_64-Media.iso",
        # Oracle Linux 9
        "https://yum.oracle.com/ISOS/OracleLinux/OL9/u5/x86_64/OracleLinux-R9-U5-x86_64-dvd.iso",
    ],

    "linux/scientific": [
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Scientific_KDE-Live-x86_64-43-1.1.iso",
        # Scientific Linux 7.9 (CERN/Fermilab, archived)
        "https://ftp.scientificlinux.org/linux/scientific/7.9/x86_64/iso/SL-7.9-x86_64-2021-01-26-boot.iso",
        "https://ftp.scientificlinux.org/linux/scientific/7.9/x86_64/iso/SL-7.9-x86_64-2021-01-26-Everything-DVD1.iso",
        # Bio-Linux 8 (bioinformatics)
        "https://nebc.nox.ac.uk/tools/bio-linux/bio-linux-8.0.iso",
    ],

    "homelab/virtualization": [
        # Proxmox VE 8.3
        "https://enterprise.proxmox.com/iso/proxmox-ve_8.3-1.iso",
        # XCP-ng 8.3
        "https://updates.xcp-ng.org/isos/8.3.0/xcp-ng-8.3.0.iso",
        # VirtIO Windows drivers
        "https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso",
        # CloneZilla 3.2.0
        "https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/3.2.0-5/clonezilla-live-3.2.0-5-amd64.iso/download",
        # Harvester HCI (Rancher)
        "https://releases.rancher.com/harvester/v1.4.0/harvester-v1.4.0-amd64.iso",
        # oVirt 4.5 Node
        "https://resources.ovirt.org/pub/ovirt-4.5/iso/ovirt-node-ng-installer-4.5.3-2023060913.el8.iso",
        # Kimchi (QEMU web management) – no ISO, skip
        # VMware Workstation Player ISO helper – no standalone ISO
        # DRBL server
        "https://sourceforge.net/projects/drbl/files/drbl_stable/2.32.1/drbl-live-stable-2.32.1-amd64.iso/download",
    ],

    "homelab/nas": [
        # TrueNAS Scale 24.10
        "https://download.truenas.com/TrueNAS-SCALE-24.10.2/TrueNAS-SCALE-24.10.2.iso",
        # TrueNAS Core 13 (legacy FreeBSD-based)
        "https://download.truenas.com/TrueNAS-CORE-13.0-U6.2/TrueNAS-CORE-13.0-U6.2.iso",
        # OpenMediaVault 7.4
        "https://sourceforge.net/projects/openmediavault/files/7.4.7/openmediavault_7.4.7-amd64.iso/download",
        # Rockstor 5.0
        "https://sourceforge.net/projects/rockstor/files/5.0.15-0/Rockstor-5.0.15-0-x86_64.iso/download",
        # XigmaNAS 13.3
        "https://sourceforge.net/projects/xigmanas/files/XigmaNAS-13.3/XigmaNAS-x64-13.3.0.9.1.iso/download",
        # Amahi HDA7
        "https://sourceforge.net/projects/amahi/files/hda7.iso/download",
        # EasyNAS (openSUSE-based)
        "https://sourceforge.net/projects/easynascloud/files/v1.0.0/easynascloud-1.0.0-amd64.iso/download",
    ],

    "homelab/networking": [
        # pfSense CE 2.7.2
        "https://frafiles.netgate.com/mirror/downloads/pfSense-CE-2.7.2-RELEASE-amd64.iso.gz",
        # OPNsense 25.1
        "https://mirror.opnsense.org/releases/25.1/OPNsense-25.1-dvd-amd64.iso",
        # IPFire 2.29
        "https://downloads.ipfire.org/releases/ipfire-2.x/2.29-core190/ipfire-2.29.x86_64-full-core190.iso",
        # VyOS 1.4 (LTS Sagitta)
        "https://downloads.vyos.io/release/stream/1.4/VyOS-1.4-rolling-202412010026-amd64.iso",
        # ClearOS 7.9
        "https://sourceforge.net/projects/clearos/files/clearos-7.9-core.x86_64.iso/download",
        # Untangle NG Firewall 17.0
        "https://downloads.untangle.com/untangle-17.0-x86_64.iso",
        # ZeroShell 3.9.5
        "https://zeroshell.org/download/ZeroShell-3.9.5-x86_64.iso",
        # IPCop 2.1.9
        "https://sourceforge.net/projects/ipcop/files/IPCop-2.1.9-install-cd.i486.iso/download",
        # OpenWrt x86 (router OS on x86)
        "https://downloads.openwrt.org/releases/23.05.5/targets/x86/64/openwrt-23.05.5-x86-64-generic-ext4-combined.img.gz",
    ],

    "recovery/tools": [
        # SystemRescue 11.03
        "https://mirror.kku.ac.th/systemrescue/systemrescue-11.03-amd64.iso",
        # GParted Live 1.6.0-10
        "https://download.gparted.org/gparted-live-stable/1.6.0-10/gparted-live-1.6.0-10-amd64.iso",
        # CloneZilla Live 3.2.0
        "https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/3.2.0-5/clonezilla-live-3.2.0-5-amd64.iso/download",
        # Rescuezilla 2.5
        "https://download.rescuezilla.com/rescuezilla-2.5.0-64bit.iso",
        # Ultimate Boot CD 5.3.9
        "https://sourceforge.net/projects/ubcd/files/ubcd/5.3.9/ubcd539.iso/download",
        # qt-fsarchiver
        "https://sourceforge.net/projects/qt-fsarchiver/files/qt-fsarchiver-18.06.3-x86_64.iso/download",
        # Hiren's Boot CD PE x64
        "https://www.hirensbootcd.org/files/HBCD_PE_x64.iso",
        # netboot.xyz (iPXE-based network boot)
        "https://boot.netboot.xyz/ipxe/netboot.xyz.iso",
        # ShredOS (secure disk erasure)
        "https://github.com/PartialVolume/shredos.x86_64/releases/download/v2023.04.01_26_x86-64_0.38.4/shredos_2023.04.01_26_x86-64.img",
        # MemTest86 (free version)
        "https://www.memtest86.com/downloads/memtest86-usb.zip",
        # Finnix 125 (recovery live)
        "https://www.finnix.org/releases/125/finnix-125.iso",
    ],

    "android-x86": [
        # Android-x86 9.0 (Pie)
        "https://sourceforge.net/projects/android-x86/files/Release%209.0/android-x86_64-9.0-r2.iso/download",
        # BlissOS 16 (Android 13 for x86)
        "https://sourceforge.net/projects/blissos-x86/files/Official/BlissOS16/Generic/BlissOS-16.9.9-x86_64-OFFICIAL.iso/download",
        # PrimeOS 2.1 (Android-x86 fork)
        "https://sourceforge.net/projects/primeos/files/64-bit/PrimeOS_2.1.0_64.iso/download",
        # Phoenix OS 3.6.1
        "https://sourceforge.net/projects/phoenix-os/files/Phoenix_OS_v3.6.1_x64.iso/download",
    ],

    "chromeos": [
        # ChromeOS Flex (Google's official x86 ChromeOS)
        "https://dl.google.com/chromeos-flex/channels/stable/chromeos_flex_14316.1.0_reven_recovery_stable-channel_mp-v2.bin.zip",
        # Brunch (ChromeOS on any x86 hardware) – needs a wrapper script, no direct ISO
    ],

    "alternative/bsd": [
        # FreeBSD 14.2
        "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-amd64-dvd1.iso",
        "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-amd64-disc1.iso",
        "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-amd64-memstick.img",
        # FreeBSD 13.4 (older stable)
        "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/13.4/FreeBSD-13.4-RELEASE-amd64-dvd1.iso",
        # OpenBSD 7.6
        "https://cdn.openbsd.org/pub/OpenBSD/7.6/amd64/install76.iso",
        # NetBSD 10.1
        "https://ftp.netbsd.org/pub/NetBSD/NetBSD-10.1/images/NetBSD-10.1-amd64.iso",
        # DragonFlyBSD 6.4
        "https://mirror.dragonflybsd.org/iso-images/dfly-x86_64-6.4.0_REL.iso",
        # Haiku r1beta5
        "https://mirror.accum.se/mirror/haiku-os.org/haiku/r1beta5/haiku-r1beta5-x86_64-anyboot.iso",
        # GhostBSD 24.10.1
        "https://ghostbsd.org/releases/amd64/24.10.1/GhostBSD-24.10.1.iso",
        # NomadBSD 1.4 (FreeBSD-based persistent live)
        "https://nomadbsd.org/download/nomadbsd-20231013.i386.img",
        "https://nomadbsd.org/download/nomadbsd-20231013.amd64.img",
        # helloSystem (macOS-like BSD)
        "https://github.com/helloSystem/ISO/releases/download/r0.8.2/hello-0.8.2_0.8.2-BSD.iso",
        # MidnightBSD 3.2
        "https://www.midnightbsd.org/ftp/pub/MidnightBSD/MidnightBSD-3.2.0-RELEASE-amd64-disc1.iso",
        # ReactOS 0.4.15 (Windows NT clone)
        "https://iso.reactos.org/bootcd/reactos-0.4.15-release.iso",
    ],

    "windows/eval": [
        # Windows 11 23H2 Enterprise Eval
        "https://software-static.download.prss.microsoft.com/dbazure/8889691b-d735-4ef2-ad94-d2d0fdb44f01/22631.2428.231001-0608.23H2_NI_RELEASE_SVC_REFRESH_CLIENTENTERPRISE_VOL_X64FRE_EN-US.ISO",
        # Windows 10 22H2 Enterprise Eval
        "https://software-static.download.prss.microsoft.com/sg/download/details/44ddef8e-0c69-466c-adcc-37d80650945b/19045.2006.220908-0225.22H2_RELEASE_SVC_REFRESH_CLIENTENTERPRISE_VOL_X64FRE_EN-US.ISO",
        # Windows Server 2022 Eval
        "https://software-static.download.prss.microsoft.com/sg/download/details/20348.169.210806-2348.fe_release_svc_refresh_SERVER_EVAL_x64FRE_en-us.iso",
        # Windows Server 2019 Eval
        "https://software-download.microsoft.com/download/pr/17763.253.190108-0006.rs5_release_svc_refresh_SERVER_EVAL_x64FRE_en-us.iso",
    ],

    "specialized/containers": [
        # RancherOS (Docker-first OS, archived)
        "https://github.com/rancher/os/releases/download/v1.5.8/rancheros.iso",
        # k3OS (k3s + OS, archived)
        "https://github.com/rancher/k3os/releases/download/v0.22.2-k3s1r1/k3os-amd64.iso",
        # Talos Linux (Kubernetes OS)
        "https://github.com/siderolabs/talos/releases/download/v1.8.4/talos-amd64.iso",
        # Flatcar Container Linux
        "https://stable.release.flatcar-linux.net/amd64-usr/current/flatcar_production_iso_image.iso",
        # Core OS (archived Fedora CoreOS replaces this)
        "https://builds.coreos.fedoraproject.org/prod/streams/stable/builds/latest/x86_64/fedora-coreos-latest-live.x86_64.iso",
    ],

    "specialized/vintage": [
        # FreeDOS 1.3 (open-source DOS)
        "https://www.freedos.org/download/download/FD13-LiveCD.iso",
        # Kolibri OS (tiny OS written in ASM)
        "https://kolibrios.org/download/kolibrios.iso",
        # MenuetOS 1.52 (x86-64 OS in ASM)
        "https://menuetos.net/downloads/M64-136.zip",
        # TempleOS 5.03 (archived)
        "https://templeos.org/Downloads/TempleOSLite.ISO",
    ],

    "arm/raspberry-pi": [
        # Raspberry Pi OS (full, Bookworm-based, x86 emulation image for QEMU)
        "https://downloads.raspberrypi.com/raspios_full_armhf/images/raspios_full_armhf-latest/2024-11-19-raspios-bookworm-armhf-full.img.xz",
        # Ubuntu 24.04 Server for RPi (ARM64 image)
        "https://cdimage.ubuntu.com/ubuntu-server/noble/daily-preinstalled/current/noble-preinstalled-server-arm64+raspi.img.xz",
        # Kali for RPi4 (ARM64)
        "https://cdimage.kali.org/kali-2025.1/kali-linux-2025.1-raspberry-pi-arm64.img.xz",
        # RetroPie 4.8 (RPi 4)
        "https://github.com/RetroPie/RetroPie-Setup/releases/download/4.8/retropie-buster-4.8-rpi4_400.img.gz",
        # DietPi (x86_64 image)
        "https://dietpi.com/downloads/images/DietPi_NativePC-BIOS_x86_64-Bookworm.img.xz",
    ],

    "linux/desktop-misc": [
        # Feren OS (KDE-based)
        "https://sourceforge.net/projects/ferenoslinux/files/22.04/ferenos-22.04-amd64.iso/download",
        # Nitrux OS (AppImage-first)
        "https://sourceforge.net/projects/nitruxos/files/Release/ISO/Nitrux_OS_3.8.1-nx-desktop-amd64.iso/download",
        # Reborn OS
        "https://github.com/RebornOS-Developers/reborn-iso-profiles/releases/latest/download/RebornOS-2024.12.31-x86_64.iso",
        # BigLinux (Brazilian, KDE)
        "https://sourceforge.net/projects/biglinux/files/BigLinux_2024-11-15.iso/download",
        # XeroLinux KDE
        "https://sourceforge.net/projects/xerolinux/files/XeroLinux-KDE-2025.03.iso/download",
        # Spiral Linux (pre-configured Debian)
        "https://spirallinux.github.io/ISO/SpiralLinux_KDE_12.231101_x86-64.iso",
        # Rhino Linux (Ubuntu rolling)
        "https://sourceforge.net/projects/rhinolinux/files/rhino-linux-2024.1.iso/download",
        # tinyOS / Q4OS Trinity
        "https://sourceforge.net/projects/q4osinux/files/q4os-5.4-amd64.r1-trinity.iso/download",
        # Voyager 24.04 (Xfce Ubuntu)
        "https://sourceforge.net/projects/linuxvoyager/files/voyager-24.04-amd64.iso/download",
        # Mabox Linux (Openbox, Arch-based)
        "https://sourceforge.net/projects/mabox-linux/files/mabox-24.11-morpheus-amd64.iso/download",
        # Hyperbola GNU/Linux (fully free)
        "https://www.hyperbola.info/downloads/isos/hyperbola-0.4.1-x86_64.iso",
    ],
}


if __name__ == "__main__":
    total = sum(len(v) for v in db.values())
    print(f"{c}[ info   ]{w} Total entries: {total} across {len(db)} categories")
    for cat, urls in db.items():
        for url in urls:
            dl(url, cat)
