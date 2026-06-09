# updated auto-version-checker

DB: dict[str, list[dict]] = {

    # ubuntu
    "linux/ubuntu": [
        {"name": "Kubuntu 26.04", "url": "https://cdimage.ubuntu.com/kubuntu/releases/26.04/release/kubuntu-26.04-desktop-amd64.iso", "size": "4.0GB", "tags": ["kde", "desktop", "ubuntu"]},
        {"name": "Xubuntu 26.04", "url": "https://cdimage.ubuntu.com/xubuntu/releases/26.04/release/xubuntu-26.04-desktop-amd64.iso", "size": "3.3GB"},
        {"name": "Lubuntu 26.04", "url": "https://cdimage.ubuntu.com/lubuntu/releases/26.04/release/lubuntu-26.04-desktop-amd64.iso", "size": "3.0GB"},
        {"name": "Edubuntu 26.04", "url": "https://cdimage.ubuntu.com/edubuntu/releases/26.04/release/edubuntu-26.04-desktop-amd64.iso", "size": "4.9GB"},
    ],

    # ubuntu 24.04 noble
    "linux/ubuntu-noble": [
        {"name": "Ubuntu 24.04.4 Desktop", "url": "https://releases.ubuntu.com/24.04.4/ubuntu-24.04.4-desktop-amd64.iso", "size": "5.7GB", "tags": ["lts", "desktop", "standard"], "docs": "https://ubuntu.com/tutorials", "notes": "Standard LTS version with GNOME Desktop environment."},
        {"name": "Ubuntu 24.04.4 Server", "url": "https://releases.ubuntu.com/24.04.4/ubuntu-24.04.4-live-server-amd64.iso", "size": "2.6GB", "tags": ["lts", "server", "cloud-init"], "docs": "https://ubuntu.com/server/docs", "notes": "Highly recommended for cloud-init and virtualization templates."},
    ],

    # ubuntu 25.04 plucky
    "linux/ubuntu-plucky": [
        {"name": "Ubuntu 25.04 Desktop", "url": "https://old-releases.ubuntu.com/releases/25.04/ubuntu-25.04-desktop-amd64.iso", "size": "5.8GB"},
        {"name": "Ubuntu 25.04 Server", "url": "https://old-releases.ubuntu.com/releases/25.04/ubuntu-25.04-live-server-amd64.iso", "size": "2.7GB"},
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
        {"name": "Debian 13.5 Trixie Netinst", "url": "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-13.5.0-amd64-netinst.iso", "size": "660MB", "tags": ["stable", "minimal", "netinst"], "docs": "https://www.debian.org/releases/trixie/", "notes": "Minimal network installer. Requires active internet connection during installation."},
    ],

    # debian derivatives
    "linux/debian-based": [
        {"name": "MX Linux 25.2 KDE", "url": "https://sourceforge.net/projects/mx-linux/files/Final/MX-25.2/MX-25.2_KDE_x64.iso/download", "size": "3.2GB"},
        {"name": "KDE Neon User Current", "url": "https://files.kde.org/neon/images/user/current/neon-user-current.iso", "size": "3.1GB"},
        {"name": "Feren OS Latest", "url": "https://sourceforge.net/projects/ferenoslinux/files/latest/download", "size": "3.1GB"},
        {"name": "Nitrux OS Latest", "url": "https://sourceforge.net/projects/nitruxos/files/latest/download", "size": "3.4GB"},
        {"name": "SparkyLinux 8 KDE", "url": "https://sourceforge.net/projects/sparkylinux/files/8.0/sparkylinux-8.0-x86_64-kde.iso/download", "size": "2.7GB"},
        {"name": "MX Linux 25.2 XFCE", "url": "https://sourceforge.net/projects/mx-linux/files/Final/MX-25.2/MX-25.2_Xfce_x64.iso/download", "size": "2.7GB"},
        {"name": "antiX 23.2 Full", "url": "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.2/antiX-23.2_x64-full.iso/download", "size": "1.8GB"},
        {"name": "SparkyLinux 8 LXQt", "url": "https://sourceforge.net/projects/sparkylinux/files/8.0/sparkylinux-8.0-x86_64-lxqt.iso/download", "size": "2.0GB"},
    ],

    # linux mint
    "linux/mint": [
        {"name": "Linux Mint 22.3 Cinnamon", "url": "https://mirrors.kernel.org/linuxmint/stable/22.3/linuxmint-22.3-cinnamon-64bit.iso", "size": "2.8GB", "tags": ["lts", "desktop", "cinnamon", "ubuntu", "debian"], "docs": "https://linuxmint-user-guide.readthedocs.io", "notes": "The most popular Linux Mint edition with the Cinnamon desktop. Ideal for Windows switchers."},
        {"name": "Linux Mint 22.3 XFCE", "url": "https://mirrors.kernel.org/linuxmint/stable/22.3/linuxmint-22.3-xfce-64bit.iso", "size": "2.6GB", "tags": ["lts", "desktop", "xfce", "ubuntu", "debian"]},
        {"name": "Linux Mint 22.3 MATE", "url": "https://mirrors.kernel.org/linuxmint/stable/22.3/linuxmint-22.3-mate-64bit.iso", "size": "2.7GB", "tags": ["lts", "desktop", "mate", "ubuntu", "debian"]},
    ],

    # pop!_os
    "linux/pop-os": [
        {"name": "Pop!_OS 24.04 LTS", "url": "https://iso.pop-os.org/24.04/amd64/intel/6/pop-os_24.04_amd64_intel_6.iso", "size": "3.0GB", "tags": ["lts", "desktop", "cosmic", "ubuntu", "debian"], "docs": "https://support.system76.com", "notes": "Features the new COSMIC desktop. Great for developers and gamers."},
        {"name": "Pop!_OS 24.04 LTS (NVIDIA)", "url": "https://iso.pop-os.org/24.04/amd64/nvidia/6/pop-os_24.04_amd64_nvidia_6.iso", "size": "3.2GB", "tags": ["lts", "desktop", "nvidia", "ubuntu", "debian"]},
    ],

    # zorin os
    "linux/zorin": [
        {"name": "Zorin OS 18.1 Core", "url": "https://distro.ibiblio.org/zorinos/18/Zorin-OS-18.1-Core-64-bit.iso", "size": "3.4GB", "tags": ["lts", "desktop", "gnome", "ubuntu", "debian"], "docs": "https://help.zorin.com", "notes": "Designed to make Linux accessible to Windows and macOS users."},
    ],

    # arch family
    "linux/arch-family": [
        {"name": "Arch Linux latest", "url": "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso", "size": "1.1GB"},
        {"name": "Manjaro KDE", "url": "https://download.manjaro.org/kde/26.0.4/manjaro-kde-26.0.4-260327-linux618.iso", "size": "3.8GB", "tags": ["rolling", "desktop", "kde", "arch"], "docs": "https://wiki.manjaro.org", "notes": "Arch-based, user-friendly rolling release with hardware detection."},
        {"name": "Manjaro GNOME", "url": "https://download.manjaro.org/gnome/26.0.4/manjaro-gnome-26.0.4-260327-linux618.iso", "size": "3.5GB", "tags": ["rolling", "desktop", "gnome", "arch"]},
        {"name": "Manjaro XFCE", "url": "https://download.manjaro.org/xfce/26.0.4/manjaro-xfce-26.0.4-260327-linux618.iso", "size": "3.3GB", "tags": ["rolling", "desktop", "xfce", "arch"]},
        {"name": "EndeavourOS Endeavour", "url": "https://mirror.alpix.eu/endeavouros/iso/EndeavourOS_Titan-Neo-2026.04.27.iso", "size": "2.0GB", "tags": ["rolling", "desktop", "arch"], "docs": "https://discovery.endeavouros.com", "notes": "Terminal-centric Arch installer with a welcoming community."},
        {"name": "Garuda Dr460nized latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/dr460nized/latest.iso", "size": "3.0GB"},
        {"name": "Garuda GNOME latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/gnome/latest.iso", "size": "3.0GB"},
        {"name": "CachyOS KDE latest", "url": "https://mirror.cachyos.org/ISO/kde/latest/cachyos-kde-linux-latest.iso", "size": "3.1GB"},
        {"name": "Garuda KDE Lite latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/kde-lite/latest.iso", "size": "2.8GB"},
        {"name": "Garuda XFCE latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/xfce/latest.iso", "size": "2.7GB"},
    ],

    # enterprise / rpm
    "linux/enterprise": [
        {"name": "Fedora 44 Workstation", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-44-1.1.iso", "size": "2.2GB"},
        {"name": "Rocky Linux 9 Minimal", "url": "https://download.rockylinux.org/pub/rocky/9/isos/x86_64/Rocky-9-latest-x86_64-minimal.iso", "size": "1.8GB", "tags": ["server", "enterprise", "redhat"], "docs": "https://docs.rockylinux.org", "notes": "CentOS replacement. RHEL-compatible enterprise distribution."},
        {"name": "Rocky Linux 9 DVD", "url": "https://download.rockylinux.org/pub/rocky/9/isos/x86_64/Rocky-9-latest-x86_64-dvd.iso", "size": "10.0GB", "tags": ["server", "enterprise", "redhat"]},
        {"name": "AlmaLinux 9 Minimal", "url": "https://repo.almalinux.org/almalinux/9/isos/x86_64/AlmaLinux-9-latest-x86_64-minimal.iso", "size": "1.9GB", "tags": ["server", "enterprise", "redhat"], "docs": "https://wiki.almalinux.org", "notes": "Community-driven RHEL fork. Free and open forever."},
        {"name": "AlmaLinux 9 DVD", "url": "https://repo.almalinux.org/almalinux/9/isos/x86_64/AlmaLinux-9-latest-x86_64-dvd.iso", "size": "10.0GB", "tags": ["server", "enterprise", "redhat"]},
        {"name": "openSUSE Leap 15.6 DVD", "url": "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-DVD-x86_64-Media.iso", "size": "4.7GB"},
        {"name": "CentOS Stream 9 DVD", "url": "https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso", "size": "9.5GB"},
        {"name": "Oracle Linux 9.5 DVD", "url": "https://yum.oracle.com/ISOS/OracleLinux/OL9/u5/x86_64/OracleLinux-R9-U5-x86_64-dvd.iso", "size": "10.0GB"},
        {"name": "Fedora 44 Server", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Server/x86_64/iso/Fedora-Server-dvd-x86_64-44-1.1.iso", "size": "2.4GB"},
        {"name": "openSUSE Tumbleweed DVD", "url": "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso", "size": "4.9GB"},
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
        {"name": "Garuda Gaming latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/dr460nized-gaming/latest.iso", "size": "3.5GB"},
        {"name": "Fedora 44 Gaming Lab", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Labs/x86_64/iso/Fedora-Gaming-Live-x86_64-44-1.1.iso", "size": "3.4GB"},
    ],

    # security
    "linux/security": [
        {"name": "Kali Linux 2026.1 Installer", "url": "https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-installer-amd64.iso", "size": "4.4GB"},
    ],

    # pentesting & red team
    "linux/pentesting": [
        {"name": "BackBox 9", "url": "http://backbox.mirror.garr.it/backbox-9-desktop-amd64.iso", "size": "3.0GB"},
    ],

    # forensic & digital investigation
    "linux/forensic": [
        {"name": "DEFT Zero 2018.2", "url": "https://sourceforge.net/projects/deft/files/latest/download", "size": "2.2GB"},
    ],

    # privacy & security focused
    "linux/privacy": [
        {"name": "Qubes OS 4.2.3", "url": "https://ftp.qubes-os.org/iso/Qubes-R4.2.3-x86_64.iso", "size": "6.5GB"},
    ],

    # immutable / atomic desktops
    "linux/immutable": [
        {"name": "Fedora Silverblue 44", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Silverblue/x86_64/iso/Fedora-Silverblue-ostree-x86_64-44-1.1.iso", "size": "2.3GB"},
        {"name": "Fedora Kinoite 44", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Kinoite/x86_64/iso/Fedora-Kinoite-ostree-x86_64-44-1.1.iso", "size": "2.4GB"},
        {"name": "NixOS 24.11 GNOME", "url": "https://channels.nixos.org/nixos-24.11/latest-nixos-gnome-x86_64-linux.iso", "size": "2.4GB"},
        {"name": "NixOS 24.11 Plasma", "url": "https://channels.nixos.org/nixos-24.11/latest-nixos-plasma6-x86_64-linux.iso", "size": "2.5GB"},
    ],

    # rolling release
    "linux/rolling": [
        {"name": "openSUSE Tumbleweed KDE", "url": "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-KDE-Live-x86_64-Current.iso", "size": "1.4GB"},
        {"name": "openSUSE Tumbleweed GNOME", "url": "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-GNOME-Live-x86_64-Current.iso", "size": "1.3GB"},
    ],

    # lightweight
    "linux/lightweight": [
        {"name": "Puppy Linux FossaPup64 9.5", "url": "https://sourceforge.net/projects/puppylinux/files/puppy-fossa/fossapup64-9.5.iso/download", "size": "450MB"},
        {"name": "Linux Lite 7.2", "url": "https://sourceforge.net/projects/linuxlite/files/7.2/linux-lite-7.2-64bit.iso/download", "size": "2.0GB"},
        {"name": "Bodhi Linux 7.0", "url": "https://sourceforge.net/projects/bodhilinux/files/7.0.0/bodhi-7.0.0-64.iso/download", "size": "1.1GB"},
        {"name": "antiX 23.2 Base", "url": "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.2/antiX-23.2_x64-base.iso/download", "size": "1.0GB"},
        {"name": "MX Linux 25.2 Fluxbox", "url": "https://sourceforge.net/projects/mx-linux/files/Final/MX-25.2/MX-25.2_fluxbox_x64.iso/download", "size": "2.1GB"},
        {"name": "Puppy Linux Latest", "url": "https://sourceforge.net/projects/puppylinux/files/latest/download", "size": "450MB"},
        {"name": "Porteus 5.0 KDE", "url": "https://sourceforge.net/projects/porteus/files/latest/download", "size": "350MB"},
        {"name": "Slax 11.6", "url": "https://www.slax.org/download.php?type=x86_64&file=slax-64bit-11.6.0.iso", "size": "340MB"},
        {"name": "4MLinux 45.0", "url": "https://sourceforge.net/projects/linux4m/files/latest/download", "size": "900MB"},
        {"name": "LXLE 22.04", "url": "https://sourceforge.net/projects/lxle/files/latest/download", "size": "1.8GB"},
    ],

    # minimal & diy
    "linux/minimal": [
        {"name": "Alpine Linux 3.23.4 Standard", "url": "https://dl-cdn.alpinelinux.org/alpine/v3.23/releases/x86_64/alpine-standard-3.23.4-x86_64.iso", "size": "215MB", "tags": ["minimal", "security", "container"], "docs": "https://wiki.alpinelinux.org", "notes": "Extremely compact security-oriented distro. Ideal for minimal VM instances."},
        {"name": "Alpine Linux 3.23.4 Extended", "url": "https://dl-cdn.alpinelinux.org/alpine/v3.23/releases/x86_64/alpine-extended-3.23.4-x86_64.iso", "size": "625MB"},
        {"name": "Alpine Virt", "url": "https://dl-cdn.alpinelinux.org/alpine/v3.23/releases/x86_64/alpine-virt-3.23.4-x86_64.iso", "size": "210MB"},
        {"name": "Void Linux XFCE", "url": "https://repo-default.voidlinux.org/live/current/void-live-x86_64-musl-20250202-xfce.iso", "size": "850MB", "tags": ["rolling", "minimal", "independent"], "docs": "https://docs.voidlinux.org", "notes": "Independent rolling-release distro with runit init system and XBPS package manager."},
        {"name": "Void Linux Base", "url": "https://repo-default.voidlinux.org/live/current/void-live-x86_64-musl-20250202-base.iso", "size": "550MB", "tags": ["rolling", "minimal", "independent"]},
        {"name": "Gentoo Minimal Install", "url": "https://distfiles.gentoo.org/releases/amd64/autobuilds/current-install-amd64-minimal/install-amd64-minimal-20260531T160106Z.iso", "size": "700MB", "tags": ["source-based", "minimal", "rolling"], "docs": "https://wiki.gentoo.org/wiki/Handbook:AMD64", "notes": "Source-based meta-distribution. Maximum customization through compiling from source."},
    ],

    # homelab
    "homelab": [
        {"name": "VyOS 1.4", "url": "https://downloads.vyos.io/release/stream/1.4/VyOS-1.4-rolling-202412010026-amd64.iso", "size": "580MB"},
    ],

    # virtualization
    "homelab/virtualization": [
        {"name": "Proxmox VE 9.2-1", "url": "https://enterprise.proxmox.com/iso/proxmox-ve_9.2-1.iso", "size": "1.83GB", "tags": ["hypervisor", "homelab", "debian"], "docs": "https://pve.proxmox.com/pve-docs/", "notes": "Hypervisor management platform. Direct import: use Proxmox import command in details modal."},
        {"name": "Harvester HCI v1.8.0", "url": "https://releases.rancher.com/harvester/v1.8.0/harvester-v1.8.0-amd64.iso", "size": "4.6GB"},
    ],

    # firewall / router
    "homelab/firewall": [
        {"name": "OPNsense 26.1 DVD", "url": "https://mirror.ams1.nl.leaseweb.net/opnsense/releases/26.1/OPNsense-26.1-dvd-amd64.iso.bz2", "size": "1.4GB", "tags": ["firewall", "router", "bsd", "homelab"], "docs": "https://docs.opnsense.org", "notes": "Modern FreeBSD-based firewall platform. Feature-rich web GUI for routing, VPN, and IDS/IPS."},
    ],

    # nas
    "homelab/nas": [
        {"name": "TrueNAS SCALE", "url": "https://download.truenas.com/TrueNAS-SCALE-Fangtooth/25.04.0/TrueNAS-SCALE-25.04.0.iso", "size": "1.3GB", "tags": ["nas", "zfs", "homelab"], "docs": "https://www.truenas.com/docs/scale/", "notes": "Enterprise-grade ZFS NAS. Supports VMs, containers, and apps out of the box."},
        {"name": "OpenMediaVault 7.4", "url": "https://sourceforge.net/projects/openmediavault/files/latest/download", "size": "1.1GB"},
        {"name": "Rockstor 5.0", "url": "https://sourceforge.net/projects/rockstor/files/latest/download", "size": "2.2GB"},
    ],

    # vintage / novelty / retro
    "specialized/vintage": [
        {"name": "KolibriOS Latest", "url": "http://builds.kolibrios.org/en_US/latest-iso.7z", "size": "45MB"},
        {"name": "TinyCore Linux 16", "url": "http://tinycorelinux.net/16.x/x86_64/release/TinyCorePure64-current.iso", "size": "157MB"},
    ],

    # containers & cloud native
    "specialized/containers": [
        {"name": "Flatcar Container Linux", "url": "https://stable.release.flatcar-linux.net/amd64-usr/current/flatcar_production_iso_image.iso", "size": "500MB"},
    ],

    # recovery & rescue tools
    "recovery/tools": [
        {"name": "GParted Live 1.8.1", "url": "https://sourceforge.net/projects/gparted/files/gparted-live-stable/1.8.1-3/gparted-live-1.8.1-3-amd64.iso/download", "size": "560MB", "tags": ["recovery", "partitioning"], "docs": "https://gparted.org/documentation.php", "notes": "Industry-standard graphical partition editor. Essential homelab utility."},
        {"name": "CloneZilla 3.3.2-31", "url": "https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/3.3.2-31/clonezilla-live-3.3.2-31-amd64.iso/download", "size": "490MB"},
        {"name": "Ultimate Boot CD 5.3.9", "url": "https://sourceforge.net/projects/ubcd/files/latest/download", "size": "960MB"},
        {"name": "Hiren's BootCD PE x64", "url": "https://www.hirensbootcd.org/files/HBCD_PE_x64.iso", "size": "2.7GB"},
        {"name": "CloneZilla Latest", "url": "https://sourceforge.net/projects/clonezilla/files/latest/download", "size": "490MB"},
    ],

    # backup & recovery
    "recovery/backup": [
        {"name": "qt-fsarchiver", "url": "https://sourceforge.net/projects/qt-fsarchiver/files/latest/download", "size": "600MB"},
    ],

    # raspberry pi
    "arm/raspberry-pi": [
        {"name": "Ubuntu Server 24.04 RPi", "url": "https://cdimage.ubuntu.com/ubuntu-server/noble/daily-preinstalled/current/noble-preinstalled-server-arm64+raspi.img.xz", "size": "1.5GB"},
        {"name": "LibreELEC RPi4", "url": "https://releases.libreelec.tv/LibreELEC-RPi4.aarch64-12.0.2.img.gz", "size": "450MB"},
    ],

    # windows evaluation
    "windows/eval": [
        {"name": "Windows Server 2019 Eval", "url": "https://software-download.microsoft.com/download/pr/17763.253.190108-0006.rs5_release_svc_refresh_SERVER_EVAL_x64FRE_en-us.iso", "size": "4.7GB"},
    ],

    # android-x86
    "android-x86": [
        {"name": "BlissOS 16.9.9 Official", "url": "https://sourceforge.net/projects/blissos-x86/files/latest/download", "size": "2.4GB"},
        {"name": "Android-x86 9.0-r2", "url": "https://sourceforge.net/projects/android-x86/files/Release%209.0/android-x86_64-9.0-r2.iso/download", "size": "1.0GB"},
        {"name": "PrimeOS 2.1.0", "url": "https://sourceforge.net/projects/primeos/files/latest/download", "size": "1.6GB"},
    ],

    # bsd / alternative
    "alternative/bsd": [
        {"name": "FreeBSD 14.4 amd64 DVD", "url": "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.4/FreeBSD-14.4-RELEASE-amd64-dvd1.iso", "size": "4.2GB", "tags": ["bsd", "server", "stable"], "docs": "https://docs.freebsd.org", "notes": "Enterprise-class UNIX operating system. Known for advanced networking, security, and ZFS."},
        {"name": "FreeBSD 14.4 amd64 Bootonly", "url": "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.4/FreeBSD-14.4-RELEASE-amd64-bootonly.iso", "size": "420MB", "tags": ["bsd", "netinst"]},
        {"name": "OpenBSD 7.9 amd64", "url": "https://cdn.openbsd.org/pub/OpenBSD/7.9/amd64/install79.iso", "size": "600MB", "tags": ["bsd", "security"], "docs": "https://www.openbsd.org/faq/", "notes": "Security-focused BSD. Proactive security features, integrated cryptography, and clean code."},
        {"name": "NetBSD 10.1 amd64", "url": "https://ftp.netbsd.org/pub/NetBSD/NetBSD-10.1/images/NetBSD-10.1-amd64.iso", "size": "560MB"},
    ],

    # ai / machine learning
    "linux/ai-ml": [
        {"name": "Fedora AI Spin", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Labs/x86_64/iso/Fedora-AI-Live-x86_64-44-1.1.iso", "size": "3.5GB"},
    ],

    # desktop environments
    "linux/desktop-env": [
        {"name": "GNOME OS Nightly Installer", "url": "https://os.gnome.org/download/latest/gnome_os_installer_nightly_x86_64.iso", "size": "4.0GB"},
        {"name": "Cutefish OS 0.8", "url": "https://sourceforge.net/projects/cutefishos/files/latest/download", "size": "2.4GB"},
    ],

    # specialized / custom
    "linux/specialized": [
        {"name": "Grml 2026.04 Full", "url": "https://download.grml.org/grml-full-2026.04-amd64.iso", "size": "1.2GB"},
        {"name": "Finnix 125 Recovery", "url": "https://www.finnix.org/releases/125/finnix-125.iso", "size": "500MB"},
        {"name": "netboot.xyz iPXE", "url": "https://boot.netboot.xyz/ipxe/netboot.xyz.iso", "size": "2MB"},
    ],

    # office & productivity
    "linux/office": [
        {"name": "Ubuntu Budgie 26.04", "url": "https://cdimage.ubuntu.com/ubuntu-budgie/releases/26.04/release/ubuntu-budgie-26.04-desktop-amd64.iso", "size": "3.4GB"},
    ],

    # education & learning
    "linux/education": [
        {"name": "UberStudent 5.1", "url": "https://sourceforge.net/projects/uberstudent/files/latest/download", "size": "3.0GB"},
    ],

    # legacy / old stable
    "linux/legacy": [
        {"name": "Ubuntu 20.04.6 LTS (Focal)", "url": "https://releases.ubuntu.com/20.04.6/ubuntu-20.04.6-desktop-amd64.iso", "size": "3.8GB"},
        {"name": "Debian 11.11 Netinst", "url": "https://cdimage.debian.org/cdimage/archive/11.11.0/amd64/iso-cd/debian-11.11.0-amd64-netinst.iso", "size": "400MB"},
        {"name": "CentOS 7.9 Final DVD", "url": "https://vault.centos.org/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2207-02.iso", "size": "4.8GB"},
    ],

    # experimental
    "linux/experimental": [
        {"name": "Tuxedo OS", "url": "https://os.tuxedocomputers.com/TUXEDO-OS_current.iso", "size": "3.2GB"},
    ],

    # alternative architectures
    "linux/alternative-arch": [
        {"name": "Alpine Linux ARM64", "url": "https://dl-cdn.alpinelinux.org/alpine/v3.23/releases/aarch64/alpine-standard-3.23.4-aarch64.iso", "size": "373MB"},
    ],

    # cloud
    "linux/cloud": [
        {"name": "RancherOS (Legacy)", "url": "https://github.com/rancher/os/releases/download/v1.5.8/rancheros.iso", "size": "170MB"},
    ],

    # multimedia
    "linux/multimedia": [
        {"name": "Fedora Jam KDE", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Labs/x86_64/iso/Fedora-Jam_KDE-Live-x86_64-44-1.1.iso", "size": "2.9GB"},
    ]
}

if __name__ == '__main__':
    total = sum(len(v) for v in DB.values())
    print(f"refactor complete: total {total} entries")
