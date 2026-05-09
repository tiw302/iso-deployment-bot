# updated 2026-05

DB: dict[str, list[dict]] = {

    # ubuntu
    "linux/ubuntu": [
        {"name": "Ubuntu Cinnamon 24.04.2", "url": "https://cdimage.ubuntu.com/ubuntu-cinnamon/releases/24.04.2/release/ubuntu-cinnamon-24.04.2-desktop-amd64.iso", "size": "3.5GB"},
        {"name": "Ubuntu Budgie 24.04.2", "url": "https://cdimage.ubuntu.com/ubuntu-budgie/releases/24.04.2/release/ubuntu-budgie-24.04.2-desktop-amd64.iso", "size": "3.3GB"},
        {"name": "Kubuntu 26.04", "url": "https://cdimage.ubuntu.com/kubuntu/releases/26.04/release/kubuntu-26.04-desktop-amd64.iso", "size": "4.0GB"},
        {"name": "Xubuntu 26.04", "url": "https://cdimage.ubuntu.com/xubuntu/releases/26.04/release/xubuntu-26.04-desktop-amd64.iso", "size": "3.3GB"},
        {"name": "Lubuntu 26.04", "url": "https://cdimage.ubuntu.com/lubuntu/releases/26.04/release/lubuntu-26.04-desktop-amd64.iso", "size": "3.0GB"},
        {"name": "Ubuntu MATE 26.04", "url": "https://cdimage.ubuntu.com/ubuntu-mate/releases/26.04/release/ubuntu-mate-26.04-desktop-amd64.iso", "size": "3.6GB"},
        {"name": "Edubuntu 26.04", "url": "https://cdimage.ubuntu.com/edubuntu/releases/26.04/release/edubuntu-26.04-desktop-amd64.iso", "size": "4.9GB"},
        {"name": "Ubuntu Unity 24.04.2", "url": "https://cdimage.ubuntu.com/ubuntu-unity/releases/24.04.2/release/ubuntu-unity-24.04.2-desktop-amd64.iso", "size": "3.4GB"},
        {"name": "Ubuntu Kylin 24.04.2", "url": "https://cdimage.ubuntu.com/ubuntu-kylin/releases/24.04.2/release/ukui-24.04.2-desktop-amd64.iso", "size": "3.8GB"},
        {"name": "Edubuntu 24.04.2", "url": "https://cdimage.ubuntu.com/edubuntu/releases/24.04.2/release/edubuntu-24.04.2-desktop-amd64.iso", "size": "4.8GB"},
    ],

    # ubuntu 24.04 noble
    "linux/ubuntu-noble": [
        {"name": "Ubuntu 24.04.2 Desktop", "url": "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-desktop-amd64.iso", "size": "5.7GB"},
        {"name": "Ubuntu 24.04.2 Server", "url": "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-live-server-amd64.iso", "size": "2.6GB"},
        {"name": "Kubuntu 24.04.2", "url": "https://cdimage.ubuntu.com/kubuntu/releases/24.04.2/release/kubuntu-24.04.2-desktop-amd64.iso", "size": "3.9GB"},
        {"name": "Xubuntu 24.04.2", "url": "https://cdimage.ubuntu.com/xubuntu/releases/24.04.2/release/xubuntu-24.04.2-desktop-amd64.iso", "size": "3.2GB"},
        {"name": "Lubuntu 24.04.2", "url": "https://cdimage.ubuntu.com/lubuntu/releases/24.04.2/release/lubuntu-24.04.2-desktop-amd64.iso", "size": "2.9GB"},
        {"name": "Ubuntu MATE 24.04.2", "url": "https://cdimage.ubuntu.com/ubuntu-mate/releases/24.04.2/release/ubuntu-mate-24.04.2-desktop-amd64.iso", "size": "3.5GB"},
        {"name": "Ubuntu Studio (Dev + Creative)", "url": "https://cdimage.ubuntu.com/ubuntustudio/releases/24.04.2/release/ubuntustudio-24.04.2-dvd-amd64.iso", "size": "4.9GB"},
    ],

    # ubuntu 25.04 plucky
    "linux/ubuntu-plucky": [
        {"name": "Ubuntu 25.04 Desktop", "url": "https://releases.ubuntu.com/25.04/ubuntu-25.04-desktop-amd64.iso", "size": "5.8GB"},
        {"name": "Ubuntu 25.04 Server", "url": "https://releases.ubuntu.com/25.04/ubuntu-25.04-live-server-amd64.iso", "size": "2.7GB"},
    ],

    # ubuntu 22.04 jammy
    "linux/ubuntu-jammy": [
        {"name": "Ubuntu 22.04.5 LTS Desktop", "url": "https://releases.ubuntu.com/22.04.5/ubuntu-22.04.5-desktop-amd64.iso", "size": "4.7GB"},
        {"name": "Ubuntu 22.04.5 LTS Server", "url": "https://releases.ubuntu.com/22.04.5/ubuntu-22.04.5-live-server-amd64.iso", "size": "2.1GB"},
        {"name": "Kubuntu 22.04.5", "url": "https://cdimage.ubuntu.com/kubuntu/releases/22.04.5/release/kubuntu-22.04.5-desktop-amd64.iso", "size": "3.7GB"},
        {"name": "Xubuntu 22.04.5", "url": "https://cdimage.ubuntu.com/xubuntu/releases/22.04.5/release/xubuntu-22.04.5-desktop-amd64.iso", "size": "3.0GB"},
    ],

    # debian
    "linux/debian": [
        {"name": "Debian 13 Trixie Netinst", "url": "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-13.4.0-amd64-netinst.iso", "size": "660MB"},
        {"name": "Debian 13 Live GNOME", "url": "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-13.0.0-amd64-gnome.iso", "size": "3.5GB"},
        {"name": "Debian 12.10 Netinst", "url": "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.10.0-amd64-netinst.iso", "size": "660MB"},
        {"name": "Debian 13 Live KDE", "url": "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-13.0.0-amd64-kde.iso", "size": "3.6GB"},
        {"name": "Debian 13 Live XFCE", "url": "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-13.0.0-amd64-xfce.iso", "size": "3.1GB"},
        {"name": "Debian 13 Live Cinnamon", "url": "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-13.0.0-amd64-cinnamon.iso", "size": "3.3GB"},
        {"name": "Debian 12.10 DVD-1", "url": "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.10.0-amd64-DVD-1.iso", "size": "4.0GB"},
    ],

    # debian derivatives
    "linux/debian-based": [
        {"name": "Pop!_OS 24.04 NVIDIA", "url": "https://iso.pop-os.org/24.04/amd64/nvidia/46/pop-os_24.04_amd64_nvidia_46.iso", "size": "2.8GB"},
        {"name": "Zorin OS 17.3 Core", "url": "https://downloads.zorinos.com/17/Zorin-OS-17.3-Core-64-bit.iso", "size": "3.8GB"},
        {"name": "elementary OS 8.1", "url": "https://downloads.elementary.io/os-8.1-stable.20250301.iso", "size": "2.7GB"},
        {"name": "MX Linux 23.6 KDE", "url": "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6-kde_x64.iso/download", "size": "3.2GB"},
        {"name": "KDE Neon User Current", "url": "https://files.kde.org/neon/images/user/current/neon-user-current.iso", "size": "3.1GB"},
        {"name": "Deepin 23.1", "url": "https://cdimage.deepin.com/releases/23.1/deepin-desktop-community-23.1-amd64.iso", "size": "4.2GB"},
        {"name": "Zorin OS 17.3 Lite", "url": "https://downloads.zorinos.com/17/Zorin-OS-17.3-Lite-64-bit.iso", "size": "2.2GB"},
        {"name": "Feren OS 22.04", "url": "https://sourceforge.net/projects/ferenoslinux/files/22.04/ferenos-22.04-amd64.iso/download", "size": "3.1GB"},
        {"name": "Nitrux OS 3.8", "url": "https://sourceforge.net/projects/nitruxos/files/Release/ISO/Nitrux_OS_3.8.1-nx-desktop-amd64.iso/download", "size": "3.4GB"},
        {"name": "BigLinux latest", "url": "https://sourceforge.net/projects/biglinux/files/latest/download", "size": "3.5GB"},
        {"name": "SparkyLinux 8 KDE", "url": "https://sourceforge.net/projects/sparkylinux/files/8.0/sparkylinux-8.0-x86_64-kde.iso/download", "size": "2.7GB"},
        {"name": "Pop!_OS 24.04 Development", "url": "https://iso.pop-os.org/24.04/amd64/intel/46/pop-os_24.04_amd64_intel_46.iso", "size": "2.6GB"},
        {"name": "Zorin OS 17.3 Education", "url": "https://downloads.zorinos.com/17/Zorin-OS-17.3-Education-64-bit.iso", "size": "3.9GB"},
        {"name": "Linux Mint 22.3 Cinnamon (KKU mirror)", "url": "https://mirror.kku.ac.th/linuxmint/iso/stable/22.3/linuxmint-22.3-cinnamon-64bit.iso", "size": "2.9GB"},
        {"name": "Nitrux OS latest", "url": "https://sourceforge.net/projects/nitruxos/files/Release/ISO/latest/download", "size": "3.4GB"},
        {"name": "MX Linux 23.6 XFCE", "url": "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6_x64.iso/download", "size": "2.7GB"},
        {"name": "antiX 23.2 Full", "url": "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.2/antiX-23.2_x64-full.iso/download", "size": "1.8GB"},
        {"name": "SparkyLinux 8 LXQt", "url": "https://sourceforge.net/projects/sparkylinux/files/8.0/sparkylinux-8.0-x86_64-lxqt.iso/download", "size": "2.0GB"},
        {"name": "KDE Neon Testing", "url": "https://files.kde.org/neon/images/testing/neon-testing-current.iso", "size": "3.2GB"},
    ],

    # linux mint
    "linux/mint": [
        {"name": "Linux Mint 22.3 Cinnamon", "url": "https://ftp.linuxmint.com/stable/22.3/linuxmint-22.3-cinnamon-64bit.iso", "size": "2.9GB"},
        {"name": "Linux Mint 22.3 MATE", "url": "https://ftp.linuxmint.com/stable/22.3/linuxmint-22.3-mate-64bit.iso", "size": "2.7GB"},
        {"name": "Linux Mint 22.3 XFCE", "url": "https://ftp.linuxmint.com/stable/22.3/linuxmint-22.3-xfce-64bit.iso", "size": "2.6GB"},
        {"name": "LMDE 7 Cinnamon", "url": "https://ftp.linuxmint.com/stable/lmde7/lmde-7-cinnamon-64bit.iso", "size": "2.8GB"},
    ],

    # arch family
    "linux/arch-family": [
        {"name": "Arch Linux latest", "url": "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso", "size": "1.1GB"},
        {"name": "Manjaro KDE latest", "url": "https://download.manjaro.org/kde/latest/manjaro-kde-latest.iso", "size": "4.2GB"},
        {"name": "Manjaro GNOME latest", "url": "https://download.manjaro.org/gnome/latest/manjaro-gnome-latest.iso", "size": "4.0GB"},
        {"name": "Manjaro XFCE latest", "url": "https://download.manjaro.org/xfce/latest/manjaro-xfce-latest.iso", "size": "3.7GB"},
        {"name": "EndeavourOS latest", "url": "https://mirror.alpix.eu/endeavouros/iso/latest/EndeavourOS_Cassini_latest.iso", "size": "3.0GB"},
        {"name": "Garuda Dr460nized latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/dr460nized/latest.iso", "size": "3.0GB"},
        {"name": "Garuda GNOME latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/gnome/latest.iso", "size": "3.0GB"},
        {"name": "CachyOS KDE latest", "url": "https://mirror.cachyos.org/ISO/kde/latest/cachyos-kde-linux-latest.iso", "size": "3.1GB"},
        {"name": "Artix KDE OpenRC", "url": "https://mirrors.dotsrc.org/artix-linux/iso/latest/artix-kde-openrc-latest-x86_64.iso", "size": "2.8GB"},
        {"name": "BlackArch Full", "url": "https://ftp.halifax.rwth-aachen.de/blackarch/iso/blackarch-linux-full-2025.01.01-x86_64.iso", "size": "21GB"},
        {"name": "Garuda KDE Lite latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/kde-lite/latest.iso", "size": "2.8GB"},
        {"name": "Garuda XFCE latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/xfce/latest.iso", "size": "2.7GB"},
        {"name": "Artix GNOME OpenRC", "url": "https://mirrors.dotsrc.org/artix-linux/iso/latest/artix-gnome-openrc-latest-x86_64.iso", "size": "2.6GB"},
        {"name": "RebornOS latest", "url": "https://github.com/RebornOS-Developers/reborn-iso-profiles/releases/latest/download/RebornOS-latest-x86_64.iso", "size": "3.5GB"},
    ],

    # enterprise / rpm
    "linux/enterprise": [
        {"name": "Fedora 44 Workstation", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-44-1.1.iso", "size": "2.2GB"},
        {"name": "AlmaLinux 9.5 DVD", "url": "https://mirror.kku.ac.th/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-dvd.iso", "size": "10.4GB"},
        {"name": "Rocky Linux 9.5 DVD", "url": "https://mirror.kku.ac.th/rocky/9.5/isos/x86_64/Rocky-9.5-x86_64-dvd.iso", "size": "10.6GB"},
        {"name": "openSUSE Leap 15.6 DVD", "url": "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-DVD-x86_64-Media.iso", "size": "4.7GB"},
        {"name": "CentOS Stream 9 DVD", "url": "https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso", "size": "9.5GB"},
        {"name": "AlmaLinux 9.5 Minimal", "url": "https://mirror.kku.ac.th/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-minimal.iso", "size": "1.8GB"},
        {"name": "Rocky Linux 9.5 Minimal", "url": "https://mirror.kku.ac.th/rocky/9.5/isos/x86_64/Rocky-9.5-x86_64-minimal.iso", "size": "1.9GB"},
        {"name": "Oracle Linux 9.5 DVD", "url": "https://yum.oracle.com/ISOS/OracleLinux/OL9/u5/x86_64/OracleLinux-R9-U5-x86_64-dvd.iso", "size": "10.0GB"},
        {"name": "EuroLinux 9.4 Desktop", "url": "https://fbi.cdn.euro-linux.com/iso/EuroLinux-9.4-x86_64-dvd.iso", "size": "9.8GB"},
        {"name": "Fedora 44 Server", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Server/x86_64/iso/Fedora-Server-dvd-x86_64-44-1.1.iso", "size": "2.4GB"},
        {"name": "openSUSE Tumbleweed DVD", "url": "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso", "size": "4.9GB"},
        {"name": "openSUSE Leap 15.6 GNOME Live", "url": "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-GNOME-Live-x86_64-Media.iso", "size": "1.2GB"},
    ],

    # server
    "linux/server": [
        {"name": "Ubuntu 26.04 LTS Server", "url": "https://releases.ubuntu.com/26.04/ubuntu-26.04-live-server-amd64.iso", "size": "2.7GB"},
    ],

    # fedora spins & labs
    "linux/fedora-spins": [
        {"name": "Fedora 44 KDE Spin", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Spins/x86_64/iso/Fedora-KDE-Live-x86_64-44-1.1.iso", "size": "2.6GB"},
        {"name": "Fedora 44 XFCE Spin", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Spins/x86_64/iso/Fedora-Xfce-Live-x86_64-44-1.1.iso", "size": "1.7GB"},
        {"name": "Fedora 44 Cinnamon Spin", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Spins/x86_64/iso/Fedora-Cinnamon-Live-x86_64-44-1.1.iso", "size": "2.3GB"},
        {"name": "Fedora 44 Scientific KDE", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Labs/x86_64/iso/Fedora-Scientific_KDE-Live-x86_64-44-1.1.iso", "size": "3.7GB"},
        {"name": "Fedora 44 Sway Spin", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Spins/x86_64/iso/Fedora-Sway-Live-x86_64-44-1.1.iso", "size": "1.8GB"},
        {"name": "Fedora 44 i3 Spin", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Spins/x86_64/iso/Fedora-i3-Live-x86_64-44-1.1.iso", "size": "1.7GB"},
        {"name": "Fedora 44 Budgie Spin", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Spins/x86_64/iso/Fedora-Budgie-Live-x86_64-44-1.1.iso", "size": "2.1GB"},
        {"name": "Fedora 44 Security Lab", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Labs/x86_64/iso/Fedora-Security-Live-x86_64-44-1.1.iso", "size": "2.4GB"},
        {"name": "Fedora 44 Design Suite", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Labs/x86_64/iso/Fedora-Design_suite-Live-x86_64-44-1.1.iso", "size": "2.8GB"},
    ],

    # gaming
    "linux/gaming": [
        {"name": "Nobara 43 Official", "url": "https://nobara-images.nobaraproject.org/Nobara-43-Official-2025-10-01.iso", "size": "4.0GB"},
        {"name": "Bazzite Stable (Gaming Immutable)", "url": "https://download.bazzite.gg/Bazzite-stable.iso", "size": "4.0GB"},
        {"name": "ChimeraOS latest", "url": "https://chimeraos.org/images/latest/chimera-latest.iso", "size": "3.5GB"},
        {"name": "Garuda Gaming latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/gaming/latest.iso", "size": "3.5GB"},
        {"name": "Drauger OS 7.6", "url": "https://draugeros.org/iso/drauger-os-7.6-amd64.iso", "size": "3.2GB"},
        {"name": "Batocera x86_64 v40", "url": "https://mirrors.o2switch.fr/batocera/x86_64/stable/last/batocera-x86_64-40.img.gz", "size": "2.4GB"},
        {"name": "Fedora 44 Gaming Lab", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Labs/x86_64/iso/Fedora-Gaming-Live-x86_64-44-1.1.iso", "size": "3.4GB"},
        {"name": "Nobara 44 Gaming", "url": "https://nobara-images.nobaraproject.org/Nobara-44-Official.iso", "size": "4.2GB"},
        {"name": "Bazzite Deck Edition", "url": "https://download.bazzite.gg/Bazzite-Deck.iso", "size": "4.1GB"},
        {"name": "Lakka Latest", "url": "https://le-builds.lakka.tv/Generic.x86_64/Lakka-Generic.x86_64-latest.iso", "size": "550MB"},
        {"name": "Batocera x86_64 Latest", "url": "https://mirrors.o2switch.fr/batocera/x86_64/stable/last/batocera-x86_64-latest.img.gz", "size": "2.5GB"},
    ],

    # security
    "linux/security": [
        {"name": "Kali Linux 2026.1 Installer", "url": "https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-installer-amd64.iso", "size": "4.4GB"},
        {"name": "Kali Linux 2026.1 Live", "url": "https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-live-amd64.iso", "size": "3.9GB"},
        {"name": "Parrot Security 6.2", "url": "https://ftp.nluug.nl/os/Linux/distr/parrotsec/iso/6.2/Parrot-security-6.2_x64.iso", "size": "5.1GB"},
        {"name": "Kali Linux 2026.1 Everything", "url": "https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-installer-everything-amd64.iso", "size": "13.1GB"},
        {"name": "Parrot Home 6.2", "url": "https://ftp.nluug.nl/os/Linux/distr/parrotsec/iso/6.2/Parrot-home-6.2_x64.iso", "size": "2.7GB"},
        {"name": "BlackArch Slim 2025", "url": "https://ftp.halifax.rwth-aachen.de/blackarch/iso/blackarch-linux-slim-2025.01.01-x86_64.iso", "size": "4.0GB"},
        {"name": "Kali Linux 2026.1 Installer (KKU)", "url": "https://mirror.kku.ac.th/kali-images/kali-2026.1/kali-linux-2026.1-installer-amd64.iso", "size": "4.4GB"},
        {"name": "Pentoo 2024", "url": "https://sourceforge.net/projects/pentoo/files/Pentoo/2024.0/pentoo-amd64-2024.0.iso/download", "size": "6.5GB"},
    ],

    # pentesting & red team
    "linux/pentesting": [
        {"name": "BackBox 9", "url": "https://releases.backbox.org/backbox-9-desktop-amd64.iso", "size": "3.0GB"},
    ],

    # forensic & digital investigation
    "linux/forensic": [
        {"name": "CAINE 14 Forensic", "url": "https://www.caine-live.net/caine14/caine14.0.iso", "size": "3.7GB"},
        {"name": "DEFT Zero 2018.2", "url": "https://sourceforge.net/projects/deft/files/DEFT-Zero/2018.2/deft-zero-2018.2.iso/download", "size": "2.2GB"},
        {"name": "Tsurugi Linux 2024", "url": "https://sourceforge.net/projects/tsurugi-linux/files/2024.1/tsurugi-linux-2024.1-amd64.iso/download", "size": "17.0GB"},
        {"name": "REMnux Malware Analysis", "url": "https://remnux.org/downloads/remnux-v7-focal-ova.iso", "size": "3.0GB"},
    ],

    # privacy & security focused
    "linux/privacy": [
        {"name": "Tails 6.13", "url": "https://tails.net/torrents/files/tails-amd64-6.13.iso", "size": "1.4GB"},
        {"name": "Qubes OS 4.2.3", "url": "https://ftp.qubes-os.org/iso/Qubes-R4.2.3-x86_64.iso", "size": "6.5GB"},
        {"name": "Whonix 17 XFCE", "url": "https://download.whonix.org/ova/17.2.3.7/Whonix-Xfce-17.2.3.7.ova", "size": "1.7GB"},
        {"name": "Tails Latest", "url": "https://tails.net/torrents/files/tails-amd64-latest.iso", "size": "1.4GB"},
    ],

    # immutable / atomic desktops
    "linux/immutable": [
        {"name": "Fedora Silverblue 44", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Silverblue/x86_64/iso/Fedora-Silverblue-ostree-x86_64-44-1.1.iso", "size": "2.3GB"},
        {"name": "Fedora Kinoite 44", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Kinoite/x86_64/iso/Fedora-Kinoite-ostree-x86_64-44-1.1.iso", "size": "2.4GB"},
        {"name": "Vanilla OS 2 Desktop", "url": "https://github.com/Vanilla-OS/os/releases/latest/download/vanillaos-2-desktop-amd64.iso", "size": "2.0GB"},
        {"name": "openSUSE MicroOS DVD", "url": "https://download.opensuse.org/distribution/microos/iso/openSUSE-MicroOS-DVD-x86_64-Current.iso", "size": "1.8GB"},
        {"name": "NixOS 24.11 GNOME", "url": "https://channels.nixos.org/nixos-24.11/latest-nixos-gnome-x86_64-linux.iso", "size": "2.4GB"},
        {"name": "NixOS 24.11 Plasma", "url": "https://channels.nixos.org/nixos-24.11/latest-nixos-plasma6-x86_64-linux.iso", "size": "2.5GB"},
    ],

    # wayland / tiling wm
    "linux/wayland-tiling": [
        {"name": "Regolith Linux (i3)", "url": "https://github.com/regolith-linux/regolith-ubuntu-iso/releases/latest/download/regolith-ubuntu-3.2-amd64.iso", "size": "2.5GB"},
    ],

    # rolling release
    "linux/rolling": [
        {"name": "openSUSE Tumbleweed KDE", "url": "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-KDE-Live-x86_64-Current.iso", "size": "1.4GB"},
        {"name": "Void Linux Minimal", "url": "https://repo-default.voidlinux.org/live/current/void-live-x86_64-20250201.iso", "size": "900MB"},
        {"name": "openSUSE Tumbleweed GNOME", "url": "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-GNOME-Live-x86_64-Current.iso", "size": "1.3GB"},
        {"name": "Void Linux XFCE", "url": "https://repo-default.voidlinux.org/live/current/void-live-x86_64-xfce-20250201.iso", "size": "1.1GB"},
        {"name": "Solus Plasma", "url": "https://mirrors.rit.edu/solus/images/4.6/Solus-4.6-Plasma.iso", "size": "2.1GB"},
    ],

    # lightweight
    "linux/lightweight": [
        {"name": "Puppy Linux FossaPup64 9.5", "url": "https://sourceforge.net/projects/puppylinux/files/puppy-fossa/fossapup64-9.5.iso/download", "size": "450MB"},
        {"name": "Linux Lite 7.2", "url": "https://sourceforge.net/projects/linuxlite/files/7.2/linux-lite-7.2-64bit.iso/download", "size": "2.0GB"},
        {"name": "Bodhi Linux 7.0", "url": "https://sourceforge.net/projects/bodhilinux/files/7.0.0/bodhi-7.0.0-64.iso/download", "size": "1.1GB"},
        {"name": "Peppermint OS 12", "url": "https://peppermintos.com/iso/Peppermint-12-20240201-amd64.iso", "size": "1.8GB"},
        {"name": "antiX 23.2 Base", "url": "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.2/antiX-23.2_x64-base.iso/download", "size": "1.0GB"},
        {"name": "MX Linux 23.6 Fluxbox", "url": "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6_fluxbox_x64.iso/download", "size": "2.1GB"},
        {"name": "Puppy Linux Latest", "url": "https://sourceforge.net/projects/puppylinux/files/latest/download", "size": "450MB"},
        {"name": "Porteus 5.0 KDE", "url": "https://sourceforge.net/projects/porteus/files/Porteus-v5.0-x86_64.iso/download", "size": "350MB"},
        {"name": "Slax 11.6", "url": "https://www.slax.org/download.php?type=x86_64&file=slax-64bit-11.6.0.iso", "size": "340MB"},
        {"name": "4MLinux 45.0", "url": "https://sourceforge.net/projects/linux4m/files/45.0/4MLinux-45.0-x86_64.iso/download", "size": "900MB"},
        {"name": "LXLE 22.04", "url": "https://sourceforge.net/projects/lxle/files/LXLE22043/lxle-22043-64bit.iso/download", "size": "1.8GB"},
    ],

    # minimal & diy
    "linux/minimal": [
        {"name": "Alpine Linux 3.21 Standard", "url": "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-standard-3.21.3-x86_64.iso", "size": "215MB"},
        {"name": "Alpine Linux 3.21 Extended", "url": "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-extended-3.21.3-x86_64.iso", "size": "625MB"},
        {"name": "Alpine Virt", "url": "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-virt-3.21.3-x86_64.iso", "size": "210MB"},
        {"name": "Gentoo LiveGUI", "url": "https://gentoo.osuosl.org/releases/amd64/autobuilds/current-livegui-amd64/livegui-amd64.iso", "size": "4.5GB"},
        {"name": "Slackware 15.0 DVD", "url": "https://slackware.uk/slackware/slackware64-15.0/slackware64-15.0-install-dvd.iso", "size": "8.0GB"},
    ],

    # homelab
    "homelab": [
        {"name": "Proxmox VE 8.3", "url": "https://enterprise.proxmox.com/iso/proxmox-ve_8.3-1.iso", "size": "1.3GB"},
        {"name": "TrueNAS SCALE 24.10.2", "url": "https://download.truenas.com/TrueNAS-SCALE-24.10.2/TrueNAS-SCALE-24.10.2.iso", "size": "2.3GB"},
        {"name": "OPNsense 25.1", "url": "https://mirror.opnsense.org/releases/25.1/OPNsense-25.1-dvd-amd64.iso", "size": "1.1GB"},
        {"name": "Proxmox Backup Server", "url": "https://enterprise.proxmox.com/iso/proxmox-backup-server_3.2-1.iso", "size": "1.1GB"},
        {"name": "TrueNAS CORE 13", "url": "https://download.truenas.com/TrueNAS-CORE-13.0-U6.2/TrueNAS-CORE-13.0-U6.2.iso", "size": "1.2GB"},
        {"name": "IPFire 2.29", "url": "https://downloads.ipfire.org/releases/ipfire-2.x/2.29-core190/ipfire-2.29.x86_64-full-core190.iso", "size": "600MB"},
        {"name": "VyOS 1.4", "url": "https://downloads.vyos.io/release/stream/1.4/VyOS-1.4-rolling-202412010026-amd64.iso", "size": "580MB"},
    ],

    # virtualization
    "homelab/virtualization": [
        {"name": "Proxmox VE 9.1", "url": "https://enterprise.proxmox.com/iso/proxmox-ve_9.1-1.iso", "size": "1.83GB"},
        {"name": "XCP-ng 8.3", "url": "https://updates.xcp-ng.org/isos/8.3.0/xcp-ng-8.3.0.iso", "size": "1.0GB"},
        {"name": "Harvester HCI v1.4", "url": "https://releases.rancher.com/harvester/v1.4.0/harvester-v1.4.0-amd64.iso", "size": "4.6GB"},
    ],

    # nas
    "homelab/nas": [
        {"name": "OpenMediaVault 7.4", "url": "https://sourceforge.net/projects/openmediavault/files/7.4.7/openmediavault_7.4.7-amd64.iso/download", "size": "1.1GB"},
        {"name": "Rockstor 5.0", "url": "https://sourceforge.net/projects/rockstor/files/5.0.15-0/Rockstor-5.0.15-0-x86_64.iso/download", "size": "2.2GB"},
    ],

    # vintage / novelty / retro
    "specialized/vintage": [
        {"name": "FreeDOS 1.3 LiveCD", "url": "https://www.freedos.org/download/download/FD13-LiveCD.iso", "size": "20MB"},
        {"name": "KolibriOS Latest", "url": "https://kolibrios.org/download/kolibrios.iso", "size": "8MB"},
        {"name": "Damn Small Linux 2024", "url": "https://www.damnsmalllinux.org/2024/download/dsl-2024.06.01-x86_64.iso", "size": "50MB"},
        {"name": "TinyCore Pure64 16.0", "url": "http://tinycorelinux.net/16.x/x86_64/release/CorePure64-16.0.iso", "size": "17MB"},
        {"name": "ReactOS 0.4.15", "url": "https://iso.reactos.org/bootcd/reactos-0.4.15-release.iso", "size": "270MB"},
        {"name": "MenuetOS 1.52", "url": "https://menuetos.net/downloads/M64-136.zip", "size": "5MB"},
        {"name": "TinyCore Linux 16", "url": "http://tinycorelinux.net/16.x/x86_64/release/TinyCorePure64-current.iso", "size": "157MB"},
    ],

    # containers & cloud native
    "specialized/containers": [
        {"name": "Talos Linux v1.8", "url": "https://github.com/siderolabs/talos/releases/download/v1.8.4/talos-amd64.iso", "size": "110MB"},
        {"name": "Flatcar Container Linux", "url": "https://stable.release.flatcar-linux.net/amd64-usr/current/flatcar_production_iso_image.iso", "size": "500MB"},
        {"name": "Fedora CoreOS Latest", "url": "https://builds.coreos.fedoraproject.org/prod/streams/stable/builds/latest/x86_64/fedora-coreos-latest-live.x86_64.iso", "size": "860MB"},
    ],

    # risc / emulation / research
    "specialized/risc-emulation": [
        {"name": "Redox OS Desktop", "url": "https://static.redox-os.org/img/x86_64/redox_desktop_x86_64_latest.img.zst", "size": "300MB"},
        {"name": "HelenOS 0.12", "url": "https://helenos.org/downloads/helenos-0.12.1-amd64.iso", "size": "50MB"},
        {"name": "Genode Sculpt", "url": "https://depot.genode.org/genodelabs/sculpt/24.04/sculpt-24-04.img", "size": "180MB"},
    ],

    # recovery & rescue tools
    "recovery/tools": [
        {"name": "SystemRescue Latest", "url": "https://mirror.kku.ac.th/systemrescue/systemrescue-11.03-amd64.iso", "size": "1.1GB"},
        {"name": "GParted Live Latest", "url": "https://download.gparted.org/gparted-live-stable/1.6.0-10/gparted-live-1.6.0-10-amd64.iso", "size": "660MB"},
        {"name": "CloneZilla 3.2.0", "url": "https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/3.2.0-5/clonezilla-live-3.2.0-5-amd64.iso/download", "size": "490MB"},
        {"name": "Rescuezilla Latest", "url": "https://download.rescuezilla.com/rescuezilla-2.5.0-64bit.iso", "size": "1.2GB"},
        {"name": "Ultimate Boot CD 5.3.9", "url": "https://sourceforge.net/projects/ubcd/files/ubcd/5.3.9/ubcd539.iso/download", "size": "960MB"},
        {"name": "Hiren's BootCD PE x64", "url": "https://www.hirensbootcd.org/files/HBCD_PE_x64.iso", "size": "2.7GB"},
        {"name": "CloneZilla Latest", "url": "https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/latest/clonezilla-live-amd64.iso/download", "size": "490MB"},
        {"name": "Ventoy Latest", "url": "https://github.com/ventoy/Ventoy/releases/latest/download/ventoy-x86_64.iso", "size": "80MB"},
    ],

    # backup & recovery
    "recovery/backup": [
        {"name": "qt-fsarchiver", "url": "https://sourceforge.net/projects/qt-fsarchiver/files/qt-fsarchiver-18.06.3-x86_64.iso/download", "size": "600MB"},
    ],

    # raspberry pi
    "arm/raspberry-pi": [
        {"name": "Raspberry Pi OS Full latest", "url": "https://downloads.raspberrypi.com/raspios_full_armhf/images/raspios_full_armhf-latest/2024-11-19-raspios-bookworm-armhf-full.img.xz", "size": "2.8GB"},
        {"name": "Ubuntu Server 24.04 RPi", "url": "https://cdimage.ubuntu.com/ubuntu-server/noble/daily-preinstalled/current/noble-preinstalled-server-arm64+raspi.img.xz", "size": "1.5GB"},
        {"name": "Raspberry Pi OS Lite", "url": "https://downloads.raspberrypi.com/raspios_lite_armhf/images/raspios_lite_armhf-latest/2024-11-19-raspios-bookworm-armhf-lite.img.xz", "size": "1.0GB"},
        {"name": "Kali Linux RPi", "url": "https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-raspberry-pi-arm64.img.xz", "size": "3.1GB"},
        {"name": "LibreELEC RPi4", "url": "https://releases.libreelec.tv/LibreELEC-RPi4.aarch64-12.0.2.img.gz", "size": "450MB"},
    ],

    # arm / sbc
    "arm/sbc": [
        {"name": "Armbian Latest (Generic)", "url": "https://dl.armbian.com/_dl/armbian-bookworm-cli-arm64.img.xz", "size": "800MB"},
        {"name": "DietPi ARM64", "url": "https://dietpi.com/downloads/images/DietPi_RPi_ARM64-Bookworm.img.xz", "size": "450MB"},
    ],

    # windows evaluation
    "windows/eval": [
        {"name": "Windows 11 23H2 Enterprise Eval", "url": "https://software-static.download.prss.microsoft.com/dbazure/8889691b-d735-4ef2-ad94-d2d0fdb44f01/22631.2428.231001-0608.23H2_NI_RELEASE_SVC_REFRESH_CLIENTENTERPRISE_VOL_X64FRE_EN-US.ISO", "size": "5.4GB"},
        {"name": "Windows 10 22H2 Enterprise Eval", "url": "https://software-static.download.prss.microsoft.com/sg/download/details/44ddef8e-0c69-466c-adcc-37d80650945b/19045.2006.220908-0225.22H2_RELEASE_SVC_REFRESH_CLIENTENTERPRISE_VOL_X64FRE_EN-US.ISO", "size": "5.8GB"},
        {"name": "Windows Server 2022 Eval", "url": "https://software-static.download.prss.microsoft.com/sg/download/details/20348.169.210806-2348.fe_release_svc_refresh_SERVER_EVAL_x64FRE_en-us.iso", "size": "5.0GB"},
        {"name": "Windows Server 2019 Eval", "url": "https://software-download.microsoft.com/download/pr/17763.253.190108-0006.rs5_release_svc_refresh_SERVER_EVAL_x64FRE_en-us.iso", "size": "4.7GB"},
        {"name": "Windows 11 24H2 Enterprise Eval", "url": "https://software-static.download.prss.microsoft.com/dbazure/8889691b-d735-4ef2-ad94-d2d0fdb44f01/26100.1.240331-1435.ge_release_svc_refresh_CLIENTENTERPRISE_VOL_X64FRE_en-us.iso", "size": "6.0GB"},
        {"name": "Windows Server 2025 Preview", "url": "https://software-static.download.prss.microsoft.com/sg/download/details/26100.1.240331-1435.ge_release_svc_refresh_SERVER_EVAL_x64FRE_en-us.iso", "size": "5.2GB"},
    ],

    # android-x86
    "android-x86": [
        {"name": "BlissOS 16.9.9 Official", "url": "https://sourceforge.net/projects/blissos-x86/files/Official/BlissOS16/Generic/BlissOS-16.9.9-x86_64-OFFICIAL.iso/download", "size": "2.4GB"},
        {"name": "Android-x86 9.0-r2", "url": "https://sourceforge.net/projects/android-x86/files/Release%209.0/android-x86_64-9.0-r2.iso/download", "size": "1.0GB"},
        {"name": "PrimeOS 2.1.0", "url": "https://sourceforge.net/projects/primeos/files/64-bit/PrimeOS_2.1.0_64.iso/download", "size": "1.6GB"},
    ],

    # chromeos
    "chromeos": [
        {"name": "ChromeOS Flex Stable", "url": "https://dl.google.com/chromeos-flex/channels/stable/chromeos_flex_14316.1.0_reven_recovery_stable-channel_mp-v2.bin.zip", "size": "1.8GB"},
    ],

    # bsd / alternative
    "alternative/bsd": [
        {"name": "FreeBSD 14.2 DVD", "url": "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-amd64-dvd1.iso", "size": "4.8GB"},
        {"name": "OpenBSD 7.6 amd64", "url": "https://cdn.openbsd.org/pub/OpenBSD/7.6/amd64/install76.iso", "size": "650MB"},
        {"name": "NetBSD 10.1 amd64", "url": "https://ftp.netbsd.org/pub/NetBSD/NetBSD-10.1/images/NetBSD-10.1-amd64.iso", "size": "560MB"},
        {"name": "GhostBSD 24.10.1", "url": "https://ghostbsd.org/releases/amd64/24.10.1/GhostBSD-24.10.1.iso", "size": "3.1GB"},
        {"name": "DragonFlyBSD 6.4.0", "url": "https://mirror.dragonflybsd.org/iso-images/dfly-x86_64-6.4.0_REL.iso", "size": "1.8GB"},
    ],

    # ai / machine learning
    "linux/ai-ml": [
        {"name": "Fedora AI Spin", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Labs/x86_64/iso/Fedora-AI-Live-x86_64-44-1.1.iso", "size": "3.5GB"},
        {"name": "Ubuntu AI 24.04", "url": "https://cdimage.ubuntu.com/ubuntu-ai/releases/24.04/ubuntu-ai-24.04-desktop-amd64.iso", "size": "4.2GB"},
        {"name": "NVIDIA AI Enterprise Base", "url": "https://developer.download.nvidia.com/compute/nvaie/iso/nvaie-24.04.iso", "size": "3.8GB"},
    ],

    # developer tools
    "linux/developer": [
        {"name": "Calculate Linux Desktop", "url": "https://www.calculate-linux.org/downloads/en/cld/amd64/current/cld-amd64.iso", "size": "3.0GB"},
    ],

    # desktop environments
    "linux/desktop-env": [
        {"name": "GNOME OS Nightly Installer", "url": "https://os.gnome.org/download/latest/gnome_os_installer_nightly_x86_64.iso", "size": "4.0GB"},
        {"name": "Cutefish OS 0.8", "url": "https://sourceforge.net/projects/cutefishos/files/0.8/cutefish-os-0.8-amd64.iso/download", "size": "2.4GB"},
        {"name": "BlendOS Latest", "url": "https://github.com/blend-os/blendos/releases/latest/download/blendos-2024.iso", "size": "2.1GB"},
    ],

    # embedded & iot
    "linux/embedded": [
        {"name": "DietPi NativePC", "url": "https://dietpi.com/downloads/images/DietPi_NativePC-BIOS_x86_64-Bookworm.img.xz", "size": "500MB"},
        {"name": "Armbian Bookworm RPi4", "url": "https://dl.armbian.com/rpi4b/archive/Armbian_24.11.4_Rpi4b_bookworm_current_6.6.70.img.xz", "size": "900MB"},
        {"name": "OSMC RPi", "url": "https://ftp.fau.de/osmc/osmc/download/installers/diskimages/OSMC_TGT_rbp4_20240606.img.gz", "size": "400MB"},
    ],

    # specialized / custom
    "linux/specialized": [
        {"name": "Grml 2026.04 Full", "url": "https://download.grml.org/grml-full-2026.04-amd64.iso", "size": "1.2GB"},
        {"name": "Finnix 125 Recovery", "url": "https://www.finnix.org/releases/125/finnix-125.iso", "size": "500MB"},
        {"name": "ShredOS Disk Eraser", "url": "https://github.com/PartialVolume/shredos.x86_64/releases/latest/download/shredos_2023.04.01_26_x86-64.img", "size": "50MB"},
        {"name": "netboot.xyz iPXE", "url": "https://boot.netboot.xyz/ipxe/netboot.xyz.iso", "size": "2MB"},
    ],

    # office & productivity
    "linux/office": [
        {"name": "Ubuntu Budgie 26.04", "url": "https://cdimage.ubuntu.com/ubuntu-budgie/releases/26.04/release/ubuntu-budgie-26.04-desktop-amd64.iso", "size": "3.4GB"},
    ],

    # hardware specific
    "linux/hardware": [
        {"name": "Linux Mint Edge", "url": "https://ftp.linuxmint.com/stable/edge/linuxmint-edge-cinnamon-64bit.iso", "size": "2.7GB"},
    ],

    # live usb tools
    "linux/live-tools": [
        {"name": "Rufus Portable ISO", "url": "https://github.com/pbatard/rufus/releases/latest/download/rufus-4.5p.exe", "size": "2MB"},
        {"name": "balenaEtcher", "url": "https://github.com/balena-io/etcher/releases/latest/download/balenaEtcher-1.19.21-x64.AppImage", "size": "150MB"},
    ],

    # education & learning
    "linux/education": [
        {"name": "Sugar on a Stick", "url": "https://download.sugarlabs.org/releases/14.0/sugar-live-build.iso", "size": "1.3GB"},
        {"name": "Debian Edu 12", "url": "https://ftp.skolelinux.com/skolelinux/debian-edu-12+edu2-CD.iso", "size": "700MB"},
        {"name": "UberStudent 5.1", "url": "https://sourceforge.net/projects/uberstudent/files/UberStudent/5.1/UberStudent-5.1-Athena-amd64.iso/download", "size": "3.0GB"},
        {"name": "openSUSE Edu Li-f-e", "url": "https://download.opensuse.org/education/release/42.3/openSUSE-Edu-li-f-e-42.3-0-i586_x86_64.iso", "size": "4.7GB"},
    ],

    # scientific & data science
    "linux/scientific": [
        {"name": "Bio-Linux 8.0", "url": "https://nebc.nox.ac.uk/tools/bio-linux/bio-linux-8.0.iso", "size": "4.0GB"},
    ],

    # legacy / old stable
    "linux/legacy": [
        {"name": "Ubuntu 20.04.6 LTS (Focal)", "url": "https://releases.ubuntu.com/20.04.6/ubuntu-20.04.6-desktop-amd64.iso", "size": "3.8GB"},
        {"name": "Debian 11.11 Netinst", "url": "https://cdimage.debian.org/cdimage/archive/11.11.0/amd64/iso-cd/debian-11.11.0-amd64-netinst.iso", "size": "400MB"},
        {"name": "CentOS 7.9 Final DVD", "url": "https://vault.centos.org/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2207-02.iso", "size": "4.8GB"},
    ],

    # other distributions
    "linux/others": [
        {"name": "Clear Linux Latest", "url": "https://cdn.download.clearlinux.org/releases/current/clear/clear-live.iso", "size": "2.1GB"},
        {"name": "Q4OS 5.4 Trinity", "url": "https://sourceforge.net/projects/q4osinux/files/q4os-5.4-amd64.r1-trinity.iso/download", "size": "1.4GB"},
        {"name": "Elive 3.8", "url": "https://www.elivecd.org/download/stable/elive_3.8.40.iso", "size": "1.4GB"},
    ],

    # experimental
    "linux/experimental": [
        {"name": "Asahi Linux (Apple Silicon)", "url": "https://asahilinux.org/download/", "size": "2.5GB"},
        {"name": "Tuxedo OS", "url": "https://www.tuxedocomputers.com/en/TUXEDO-OS", "size": "3.2GB"},
        {"name": "BunsenLabs Lithium", "url": "https://sourceforge.net/projects/bunsen/files/BunsenLabs-Lithium-amd64.iso/download", "size": "1.6GB"},
    ],

    # alternative architectures
    "linux/alternative-arch": [
        {"name": "Alpine Linux ARM64", "url": "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/aarch64/alpine-standard-3.21.3-aarch64.iso", "size": "220MB"},
        {"name": "Void Linux ARM", "url": "https://repo-default.voidlinux.org/live/current/void-live-aarch64-20250201.iso", "size": "950MB"},
    ],

    # cloud
    "linux/cloud": [
        {"name": "RancherOS (Legacy)", "url": "https://github.com/rancher/os/releases/download/v1.5.8/rancheros.iso", "size": "170MB"},
        {"name": "Talos Linux", "url": "https://github.com/siderolabs/talos/releases/latest/download/talos-amd64.iso", "size": "110MB"},
    ],

    # multimedia
    "linux/multimedia": [
        {"name": "AV Linux MXE 2023", "url": "https://sourceforge.net/projects/avlinux/files/2023.11.19/AV_Linux_MXE_2023.11.19_x86_64.iso/download", "size": "3.1GB"},
        {"name": "Fedora Jam KDE", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Labs/x86_64/iso/Fedora-Jam_KDE-Live-x86_64-44-1.1.iso", "size": "2.9GB"},
        {"name": "Ubuntu Studio 26.04", "url": "https://cdimage.ubuntu.com/ubuntustudio/releases/26.04/release/ubuntustudio-26.04-dvd-amd64.iso", "size": "5.0GB"},
        {"name": "AV Linux MXE", "url": "https://sourceforge.net/projects/avlinux/files/latest/download", "size": "3.1GB"},
    ]
}

total = sum(len(v) for v in DB.values())
print(f"refactor complete: total {total} entries")
