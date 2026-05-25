# updated 2026-05

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
        {"name": "Ubuntu 24.04.2 Desktop", "url": "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-desktop-amd64.iso", "size": "5.7GB", "tags": ["lts", "desktop", "standard"], "docs": "https://ubuntu.com/tutorials", "notes": "Standard LTS version with GNOME Desktop environment."},
        {"name": "Ubuntu 24.04.2 Server", "url": "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-live-server-amd64.iso", "size": "2.6GB", "tags": ["lts", "server", "cloud-init"], "docs": "https://ubuntu.com/server/docs", "notes": "Highly recommended for cloud-init and virtualization templates."},
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
        {"name": "Debian 13 Trixie Netinst", "url": "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-13.4.0-amd64-netinst.iso", "size": "660MB", "tags": ["stable", "minimal", "netinst"], "docs": "https://www.debian.org/releases/trixie/", "notes": "Minimal network installer. Requires active internet connection during installation."},
    ],

    # debian derivatives
    "linux/debian-based": [
        {"name": "MX Linux 23.6 KDE", "url": "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6-kde_x64.iso/download", "size": "3.2GB"},
        {"name": "KDE Neon User Current", "url": "https://files.kde.org/neon/images/user/current/neon-user-current.iso", "size": "3.1GB"},
        {"name": "Feren OS 22.04", "url": "https://sourceforge.net/projects/ferenoslinux/files/22.04/ferenos-22.04-amd64.iso/download", "size": "3.1GB"},
        {"name": "Nitrux OS 3.8", "url": "https://sourceforge.net/projects/nitruxos/files/Release/ISO/Nitrux_OS_3.8.1-nx-desktop-amd64.iso/download", "size": "3.4GB"},
        {"name": "SparkyLinux 8 KDE", "url": "https://sourceforge.net/projects/sparkylinux/files/8.0/sparkylinux-8.0-x86_64-kde.iso/download", "size": "2.7GB"},
        {"name": "Nitrux OS latest", "url": "https://sourceforge.net/projects/nitruxos/files/Release/ISO/latest/download", "size": "3.4GB"},
        {"name": "MX Linux 23.6 XFCE", "url": "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6_x64.iso/download", "size": "2.7GB"},
        {"name": "antiX 23.2 Full", "url": "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.2/antiX-23.2_x64-full.iso/download", "size": "1.8GB"},
        {"name": "SparkyLinux 8 LXQt", "url": "https://sourceforge.net/projects/sparkylinux/files/8.0/sparkylinux-8.0-x86_64-lxqt.iso/download", "size": "2.0GB"},
    ],

    # arch family
    "linux/arch-family": [
        {"name": "Arch Linux latest", "url": "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso", "size": "1.1GB"},
        {"name": "Garuda Dr460nized latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/dr460nized/latest.iso", "size": "3.0GB"},
        {"name": "Garuda GNOME latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/gnome/latest.iso", "size": "3.0GB"},
        {"name": "CachyOS KDE latest", "url": "https://mirror.cachyos.org/ISO/kde/latest/cachyos-kde-linux-latest.iso", "size": "3.1GB"},
        {"name": "Garuda KDE Lite latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/kde-lite/latest.iso", "size": "2.8GB"},
        {"name": "Garuda XFCE latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/xfce/latest.iso", "size": "2.7GB"},
    ],

    # enterprise / rpm
    "linux/enterprise": [
        {"name": "Fedora 44 Workstation", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-44-1.1.iso", "size": "2.2GB"},
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
        {"name": "Garuda Gaming latest", "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/gaming/latest.iso", "size": "3.5GB"},
        {"name": "Fedora 44 Gaming Lab", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Labs/x86_64/iso/Fedora-Gaming-Live-x86_64-44-1.1.iso", "size": "3.4GB"},
    ],

    # security
    "linux/security": [
        {"name": "Kali Linux 2026.1 Installer", "url": "https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-installer-amd64.iso", "size": "4.4GB"},
        {"name": "Kali Linux 2026.1 Installer (KKU)", "url": "https://mirror.kku.ac.th/kali-images/kali-2026.1/kali-linux-2026.1-installer-amd64.iso", "size": "4.4GB"},
    ],

    # pentesting & red team
    "linux/pentesting": [
        {"name": "BackBox 9", "url": "https://releases.backbox.org/backbox-9-desktop-amd64.iso", "size": "3.0GB"},
    ],

    # forensic & digital investigation
    "linux/forensic": [
        {"name": "DEFT Zero 2018.2", "url": "https://sourceforge.net/projects/deft/files/DEFT-Zero/2018.2/deft-zero-2018.2.iso/download", "size": "2.2GB"},
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
        {"name": "MX Linux 23.6 Fluxbox", "url": "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6_fluxbox_x64.iso/download", "size": "2.1GB"},
        {"name": "Puppy Linux Latest", "url": "https://sourceforge.net/projects/puppylinux/files/latest/download", "size": "450MB"},
        {"name": "Porteus 5.0 KDE", "url": "https://sourceforge.net/projects/porteus/files/Porteus-v5.0-x86_64.iso/download", "size": "350MB"},
        {"name": "Slax 11.6", "url": "https://www.slax.org/download.php?type=x86_64&file=slax-64bit-11.6.0.iso", "size": "340MB"},
        {"name": "4MLinux 45.0", "url": "https://sourceforge.net/projects/linux4m/files/45.0/4MLinux-45.0-x86_64.iso/download", "size": "900MB"},
        {"name": "LXLE 22.04", "url": "https://sourceforge.net/projects/lxle/files/LXLE22043/lxle-22043-64bit.iso/download", "size": "1.8GB"},
    ],

    # minimal & diy
    "linux/minimal": [
        {"name": "Alpine Linux 3.21 Standard", "url": "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-standard-3.21.3-x86_64.iso", "size": "215MB", "tags": ["minimal", "security", "container"], "docs": "https://wiki.alpinelinux.org", "notes": "Extremely compact security-oriented distro. Ideal for minimal VM instances."},
        {"name": "Alpine Linux 3.21 Extended", "url": "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-extended-3.21.3-x86_64.iso", "size": "625MB"},
        {"name": "Alpine Virt", "url": "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-virt-3.21.3-x86_64.iso", "size": "210MB"},
    ],

    # homelab
    "homelab": [
        {"name": "VyOS 1.4", "url": "https://downloads.vyos.io/release/stream/1.4/VyOS-1.4-rolling-202412010026-amd64.iso", "size": "580MB"},
    ],

    # virtualization
    "homelab/virtualization": [
        {"name": "Proxmox VE 9.1", "url": "https://enterprise.proxmox.com/iso/proxmox-ve_9.1-1.iso", "size": "1.83GB", "tags": ["hypervisor", "homelab", "debian"], "docs": "https://pve.proxmox.com/pve-docs/", "notes": "Hypervisor management platform. Direct import: use Proxmox import command in details modal."},
        {"name": "Harvester HCI v1.4", "url": "https://releases.rancher.com/harvester/v1.4.0/harvester-v1.4.0-amd64.iso", "size": "4.6GB"},
    ],

    # nas
    "homelab/nas": [
        {"name": "OpenMediaVault 7.4", "url": "https://sourceforge.net/projects/openmediavault/files/7.4.7/openmediavault_7.4.7-amd64.iso/download", "size": "1.1GB"},
        {"name": "Rockstor 5.0", "url": "https://sourceforge.net/projects/rockstor/files/5.0.15-0/Rockstor-5.0.15-0-x86_64.iso/download", "size": "2.2GB"},
    ],

    # vintage / novelty / retro
    "specialized/vintage": [
        {"name": "KolibriOS Latest", "url": "https://kolibrios.org/download/kolibrios.iso", "size": "8MB"},
        {"name": "TinyCore Linux 16", "url": "http://tinycorelinux.net/16.x/x86_64/release/TinyCorePure64-current.iso", "size": "157MB"},
    ],

    # containers & cloud native
    "specialized/containers": [
        {"name": "Flatcar Container Linux", "url": "https://stable.release.flatcar-linux.net/amd64-usr/current/flatcar_production_iso_image.iso", "size": "500MB"},
    ],

    # recovery & rescue tools
    "recovery/tools": [
        {"name": "CloneZilla 3.2.0", "url": "https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/3.2.0-5/clonezilla-live-3.2.0-5-amd64.iso/download", "size": "490MB"},
        {"name": "Ultimate Boot CD 5.3.9", "url": "https://sourceforge.net/projects/ubcd/files/ubcd/5.3.9/ubcd539.iso/download", "size": "960MB"},
        {"name": "Hiren's BootCD PE x64", "url": "https://www.hirensbootcd.org/files/HBCD_PE_x64.iso", "size": "2.7GB"},
        {"name": "CloneZilla Latest", "url": "https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/latest/clonezilla-live-amd64.iso/download", "size": "490MB"},
    ],

    # backup & recovery
    "recovery/backup": [
        {"name": "qt-fsarchiver", "url": "https://sourceforge.net/projects/qt-fsarchiver/files/qt-fsarchiver-18.06.3-x86_64.iso/download", "size": "600MB"},
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
        {"name": "BlissOS 16.9.9 Official", "url": "https://sourceforge.net/projects/blissos-x86/files/Official/BlissOS16/Generic/BlissOS-16.9.9-x86_64-OFFICIAL.iso/download", "size": "2.4GB"},
        {"name": "Android-x86 9.0-r2", "url": "https://sourceforge.net/projects/android-x86/files/Release%209.0/android-x86_64-9.0-r2.iso/download", "size": "1.0GB"},
        {"name": "PrimeOS 2.1.0", "url": "https://sourceforge.net/projects/primeos/files/64-bit/PrimeOS_2.1.0_64.iso/download", "size": "1.6GB"},
    ],

    # bsd / alternative
    "alternative/bsd": [
        {"name": "NetBSD 10.1 amd64", "url": "https://ftp.netbsd.org/pub/NetBSD/NetBSD-10.1/images/NetBSD-10.1-amd64.iso", "size": "560MB"},
    ],

    # ai / machine learning
    "linux/ai-ml": [
        {"name": "Fedora AI Spin", "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Labs/x86_64/iso/Fedora-AI-Live-x86_64-44-1.1.iso", "size": "3.5GB"},
    ],

    # desktop environments
    "linux/desktop-env": [
        {"name": "GNOME OS Nightly Installer", "url": "https://os.gnome.org/download/latest/gnome_os_installer_nightly_x86_64.iso", "size": "4.0GB"},
        {"name": "Cutefish OS 0.8", "url": "https://sourceforge.net/projects/cutefishos/files/0.8/cutefish-os-0.8-amd64.iso/download", "size": "2.4GB"},
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
        {"name": "UberStudent 5.1", "url": "https://sourceforge.net/projects/uberstudent/files/UberStudent/5.1/UberStudent-5.1-Athena-amd64.iso/download", "size": "3.0GB"},
    ],

    # legacy / old stable
    "linux/legacy": [
        {"name": "Ubuntu 20.04.6 LTS (Focal)", "url": "https://releases.ubuntu.com/20.04.6/ubuntu-20.04.6-desktop-amd64.iso", "size": "3.8GB"},
        {"name": "Debian 11.11 Netinst", "url": "https://cdimage.debian.org/cdimage/archive/11.11.0/amd64/iso-cd/debian-11.11.0-amd64-netinst.iso", "size": "400MB"},
        {"name": "CentOS 7.9 Final DVD", "url": "https://vault.centos.org/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2207-02.iso", "size": "4.8GB"},
    ],

    # experimental
    "linux/experimental": [
        {"name": "Asahi Linux (Apple Silicon)", "url": "https://asahilinux.org/download/", "size": "2.5GB"},
        {"name": "Tuxedo OS", "url": "https://www.tuxedocomputers.com/en/TUXEDO-OS", "size": "3.2GB"},
    ],

    # alternative architectures
    "linux/alternative-arch": [
        {"name": "Alpine Linux ARM64", "url": "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/aarch64/alpine-standard-3.21.3-aarch64.iso", "size": "220MB"},
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

total = sum(len(v) for v in DB.values())
print(f"refactor complete: total {total} entries")
