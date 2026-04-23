# Updated 2026-04-23

DB: dict[str, list[dict]] = {

    # Arch Family    
    "linux/arch-family": [
        {"name": "Arch Linux (latest)",                    "url": "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso",                                                                         "size": "1.1GB"},
        {"name": "Manjaro KDE 24.2",                       "url": "https://download.manjaro.org/kde/24.2/manjaro-kde-24.2-260331-linux612.iso",                                                                 "size": "4.2GB"},
        {"name": "Manjaro GNOME 24.2",                     "url": "https://download.manjaro.org/gnome/24.2/manjaro-gnome-24.2-260331-linux612.iso",                                                             "size": "4.0GB"},
        {"name": "Manjaro Xfce 24.2",                      "url": "https://download.manjaro.org/xfce/24.2/manjaro-xfce-24.2-260331-linux612.iso",                                                               "size": "3.7GB"},
        {"name": "CachyOS KDE 250401",                     "url": "https://mirror.cachyos.org/ISO/kde/250401/cachyos-kde-linux-250401.iso",                                                                     "size": "3.1GB"},
        {"name": "CachyOS GNOME 250401",                   "url": "https://mirror.cachyos.org/ISO/gnome/250401/cachyos-gnome-linux-250401.iso",                                                                 "size": "3.0GB"},
        {"name": "CachyOS Desktop 250401",                 "url": "https://mirror.cachyos.org/ISO/plasma/250401/cachyos-desktop-linux-250401.iso",                                                              "size": "3.0GB"},
        {"name": "Artix Base OpenRC 20250301",             "url": "https://mirrors.dotsrc.org/artix-linux/iso/artix-base-openrc-20250301-x86_64.iso",                                                           "size": "1.4GB"},
        {"name": "Artix Base Runit 20250301",              "url": "https://mirrors.dotsrc.org/artix-linux/iso/artix-base-runit-20250301-x86_64.iso",                                                            "size": "1.4GB"},
        {"name": "Artix Plasma OpenRC 20250301",           "url": "https://mirrors.dotsrc.org/artix-linux/iso/artix-plasma-openrc-20250301-x86_64.iso",                                                         "size": "2.8GB"},
        {"name": "Artix Cinnamon OpenRC 20250301",         "url": "https://mirrors.dotsrc.org/artix-linux/iso/artix-cinnamon-openrc-20250301-x86_64.iso",                                                       "size": "2.6GB"},
        {"name": "Artix KDE OpenRC 20250301",              "url": "https://mirrors.dotsrc.org/artix-linux/iso/artix-kde-openrc-20250301-x86_64.iso",                                                            "size": "2.8GB"},
        {"name": "Artix GNOME OpenRC 20250301",            "url": "https://mirrors.dotsrc.org/artix-linux/iso/artix-gnome-openrc-20250301-x86_64.iso",                                                         "size": "2.6GB"},
        {"name": "EndeavourOS Gemini-Nova 25.04",          "url": "https://mirror.alpix.eu/endeavouros/iso/EndeavourOS_Gemini-Nova_25.04.iso",                                                                   "size": "3.0GB"},
        {"name": "Garuda KDE Lite (latest)",               "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/kde-lite/latest.iso",                                                                   "size": "2.8GB"},
        {"name": "Garuda Dr460nized (latest)",             "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/dr460nized/latest.iso",                                                                 "size": "3.0GB"},
        {"name": "Garuda GNOME (latest)",                  "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/gnome/latest.iso",                                                                      "size": "3.0GB"},
        {"name": "Garuda Xfce (latest)",                   "url": "https://iso.builds.garudalinux.org/iso/latest/garuda/xfce/latest.iso",                                                                       "size": "2.7GB"},
        {"name": "BlackArch Full 2025.01.01",              "url": "https://ftp.halifax.rwth-aachen.de/blackarch/iso/blackarch-linux-full-2025.01.01-x86_64.iso",                                                "size": "21GB"},
        {"name": "BlackArch Slim 2025.01.01",              "url": "https://ftp.halifax.rwth-aachen.de/blackarch/iso/blackarch-linux-slim-2025.01.01-x86_64.iso",                                                "size": "4.0GB"},
        {"name": "Mabox Linux 24.11",                      "url": "https://sourceforge.net/projects/mabox-linux/files/mabox-24.11-morpheus-amd64.iso/download",                                                 "size": "2.4GB"},
        {"name": "RebornOS 2024.12.31",                    "url": "https://github.com/RebornOS-Developers/reborn-iso-profiles/releases/latest/download/RebornOS-2024.12.31-x86_64.iso",                        "size": "3.5GB"},
        {"name": "Parabola GNU/Linux 2025.02 (netinstall)", "url": "https://redirector.parabolagnulinux.org/iso/2025.02/parabola-systemd-2025.02.01-netinstall-multilib-x86_64.iso",                            "size": "800MB"},
    ],

    # Ubuntu Noble (24.04 LTS)
    "linux/ubuntu-noble": [
        {"name": "Ubuntu 24.04.2 Desktop",                 "url": "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-desktop-amd64.iso",                                                                       "size": "5.7GB"},
        {"name": "Ubuntu 24.04.2 Server",                  "url": "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-live-server-amd64.iso",                                                                   "size": "2.6GB"},
        {"name": "Kubuntu 24.04.2",                        "url": "https://cdimage.ubuntu.com/kubuntu/releases/24.04.2/release/kubuntu-24.04.2-desktop-amd64.iso",                                              "size": "3.9GB"},
        {"name": "Xubuntu 24.04.2",                        "url": "https://cdimage.ubuntu.com/xubuntu/releases/24.04.2/release/xubuntu-24.04.2-desktop-amd64.iso",                                              "size": "3.2GB"},
        {"name": "Lubuntu 24.04.2",                        "url": "https://cdimage.ubuntu.com/lubuntu/releases/24.04.2/release/lubuntu-24.04.2-desktop-amd64.iso",                                              "size": "2.9GB"},
        {"name": "Ubuntu MATE 24.04.2",                    "url": "https://cdimage.ubuntu.com/ubuntu-mate/releases/24.04.2/release/ubuntu-mate-24.04.2-desktop-amd64.iso",                                      "size": "3.5GB"},
        {"name": "Ubuntu Budgie 24.04.2",                  "url": "https://cdimage.ubuntu.com/ubuntu-budgie/releases/24.04.2/release/ubuntu-budgie-24.04.2-desktop-amd64.iso",                                  "size": "3.3GB"},
        {"name": "Ubuntu Unity 24.04.2",                   "url": "https://cdimage.ubuntu.com/ubuntu-unity/releases/24.04.2/release/ubuntu-unity-24.04.2-desktop-amd64.iso",                                    "size": "3.4GB"},
        {"name": "Ubuntu Studio 24.04.2",                  "url": "https://cdimage.ubuntu.com/ubuntustudio/releases/24.04.2/release/ubuntustudio-24.04.2-dvd-amd64.iso",                                        "size": "4.9GB"},
        {"name": "Ubuntu Cinnamon 24.04.2",                "url": "https://cdimage.ubuntu.com/ubuntu-cinnamon/releases/24.04.2/release/ubuntu-cinnamon-24.04.2-desktop-amd64.iso",                              "size": "3.5GB"},
        {"name": "Edubuntu 24.04.2",                       "url": "https://cdimage.ubuntu.com/edubuntu/releases/24.04.2/release/edubuntu-24.04.2-desktop-amd64.iso",                                            "size": "4.8GB"},
        {"name": "Ubuntu Kylin 24.04.2",                   "url": "https://cdimage.ubuntu.com/ubuntu-kylin/releases/24.04.2/release/ukui-24.04.2-desktop-amd64.iso",                                            "size": "3.8GB"},
    ],

    # Ubuntu Jammy (22.04 LTS)
    "linux/ubuntu-jammy": [
        {"name": "Ubuntu 22.04.5 Desktop",                 "url": "https://releases.ubuntu.com/22.04.5/ubuntu-22.04.5-desktop-amd64.iso",                                                                       "size": "4.7GB"},
        {"name": "Ubuntu 22.04.5 Server",                  "url": "https://releases.ubuntu.com/22.04.5/ubuntu-22.04.5-live-server-amd64.iso",                                                                   "size": "2.1GB"},
        {"name": "Kubuntu 22.04.5",                        "url": "https://cdimage.ubuntu.com/kubuntu/releases/22.04.5/release/kubuntu-22.04.5-desktop-amd64.iso",                                              "size": "3.7GB"},
        {"name": "Xubuntu 22.04.5",                        "url": "https://cdimage.ubuntu.com/xubuntu/releases/22.04.5/release/xubuntu-22.04.5-desktop-amd64.iso",                                              "size": "3.0GB"},
        {"name": "Lubuntu 22.04.5",                        "url": "https://cdimage.ubuntu.com/lubuntu/releases/22.04.5/release/lubuntu-22.04.5-desktop-amd64.iso",                                              "size": "2.6GB"},
        {"name": "Ubuntu MATE 22.04.5",                    "url": "https://cdimage.ubuntu.com/ubuntu-mate/releases/22.04.5/release/ubuntu-mate-22.04.5-desktop-amd64.iso",                                      "size": "3.1GB"},
        {"name": "Ubuntu Budgie 22.04.5",                  "url": "https://cdimage.ubuntu.com/ubuntu-budgie/releases/22.04.5/release/ubuntu-budgie-22.04.5-desktop-amd64.iso",                                  "size": "3.0GB"},
        {"name": "Ubuntu Studio 22.04.5",                  "url": "https://cdimage.ubuntu.com/ubuntustudio/releases/22.04.5/release/ubuntustudio-22.04.5-dvd-amd64.iso",                                        "size": "4.7GB"},
        {"name": "Ubuntu Cinnamon 22.04.5",                "url": "https://cdimage.ubuntu.com/ubuntu-cinnamon/releases/22.04.5/release/ubuntu-cinnamon-22.04.5-desktop-amd64.iso",                              "size": "3.2GB"},
        {"name": "Edubuntu 22.04.5",                       "url": "https://cdimage.ubuntu.com/edubuntu/releases/22.04.5/release/edubuntu-22.04.5-desktop-amd64.iso",                                            "size": "4.5GB"},
    ],

    # Ubuntu Plucky (25.04)
    "linux/ubuntu-plucky": [
        {"name": "Ubuntu 25.04 Desktop",                   "url": "https://releases.ubuntu.com/25.04/ubuntu-25.04-desktop-amd64.iso",                                                                           "size": "5.8GB"},
        {"name": "Ubuntu 25.04 Server",                    "url": "https://releases.ubuntu.com/25.04/ubuntu-25.04-live-server-amd64.iso",                                                                       "size": "2.7GB"},
        {"name": "Kubuntu 25.04",                          "url": "https://cdimage.ubuntu.com/kubuntu/releases/25.04/release/kubuntu-25.04-desktop-amd64.iso",                                                  "size": "4.0GB"},
        {"name": "Xubuntu 25.04",                          "url": "https://cdimage.ubuntu.com/xubuntu/releases/25.04/release/xubuntu-25.04-desktop-amd64.iso",                                                  "size": "3.3GB"},
        {"name": "Lubuntu 25.04",                          "url": "https://cdimage.ubuntu.com/lubuntu/releases/25.04/release/lubuntu-25.04-desktop-amd64.iso",                                                  "size": "3.0GB"},
        {"name": "Ubuntu MATE 25.04",                      "url": "https://cdimage.ubuntu.com/ubuntu-mate/releases/25.04/release/ubuntu-mate-25.04-desktop-amd64.iso",                                          "size": "3.6GB"},
        {"name": "Ubuntu Budgie 25.04",                    "url": "https://cdimage.ubuntu.com/ubuntu-budgie/releases/25.04/release/ubuntu-budgie-25.04-desktop-amd64.iso",                                      "size": "3.4GB"},
        {"name": "Ubuntu Cinnamon 25.04",                  "url": "https://cdimage.ubuntu.com/ubuntu-cinnamon/releases/25.04/release/ubuntu-cinnamon-25.04-desktop-amd64.iso",                                  "size": "3.5GB"},
        {"name": "Ubuntu Studio 25.04",                    "url": "https://cdimage.ubuntu.com/ubuntustudio/releases/25.04/release/ubuntustudio-25.04-dvd-amd64.iso",                                            "size": "5.0GB"},
        {"name": "Edubuntu 25.04",                         "url": "https://cdimage.ubuntu.com/edubuntu/releases/25.04/release/edubuntu-25.04-desktop-amd64.iso",                                                "size": "4.9GB"},
    ],

    # Debian
    "linux/debian": [
        {"name": "Debian 12.10 DVD-1",                     "url": "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.10.0-amd64-DVD-1.iso",                                                  "size": "4.0GB"},
        {"name": "Debian 12.10 DVD-2",                     "url": "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.10.0-amd64-DVD-2.iso",                                                  "size": "4.0GB"},
        {"name": "Debian 12.10 DVD-3",                     "url": "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.10.0-amd64-DVD-3.iso",                                                  "size": "3.1GB"},
        {"name": "Debian 12.10 Netinstall",                "url": "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.10.0-amd64-netinst.iso",                                                 "size": "660MB"},
        {"name": "Debian 12.10 Live GNOME",                "url": "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-gnome.iso",                                     "size": "3.5GB"},
        {"name": "Debian 12.10 Live KDE",                  "url": "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-kde.iso",                                       "size": "3.6GB"},
        {"name": "Debian 12.10 Live Xfce",                 "url": "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-xfce.iso",                                      "size": "3.1GB"},
        {"name": "Debian 12.10 Live LXQt",                 "url": "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-lxqt.iso",                                      "size": "2.8GB"},
        {"name": "Debian 12.10 Live Cinnamon",             "url": "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-cinnamon.iso",                                  "size": "3.3GB"},
        {"name": "Debian 12.10 Live MATE",                 "url": "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-mate.iso",                                      "size": "3.2GB"},
        {"name": "Debian 12.10 Live Standard",             "url": "https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.10.0-amd64-standard.iso",                                  "size": "1.4GB"},
        {"name": "Debian 13 Trixie Netinstall (testing)",  "url": "https://cdimage.debian.org/cdimage/weekly-builds/amd64/iso-cd/debian-testing-amd64-netinst.iso",                                              "size": "670MB"},
    ],

    # Linux Mint
    "linux/mint": [
        {"name": "Linux Mint 22.1 Cinnamon",               "url": "https://ftp.linuxmint.com/stable/22.1/linuxmint-22.1-cinnamon-64bit.iso",                                                                    "size": "2.9GB"},
        {"name": "Linux Mint 22.1 MATE",                   "url": "https://ftp.linuxmint.com/stable/22.1/linuxmint-22.1-mate-64bit.iso",                                                                        "size": "2.7GB"},
        {"name": "Linux Mint 22.1 Xfce",                   "url": "https://ftp.linuxmint.com/stable/22.1/linuxmint-22.1-xfce-64bit.iso",                                                                        "size": "2.6GB"},
        {"name": "Linux Mint 21.3 Cinnamon",               "url": "https://ftp.linuxmint.com/stable/21.3/linuxmint-21.3-cinnamon-64bit.iso",                                                                    "size": "2.8GB"},
        {"name": "Linux Mint 21.3 MATE",                   "url": "https://ftp.linuxmint.com/stable/21.3/linuxmint-21.3-mate-64bit.iso",                                                                        "size": "2.6GB"},
        {"name": "Linux Mint 21.3 Xfce",                   "url": "https://ftp.linuxmint.com/stable/21.3/linuxmint-21.3-xfce-64bit.iso",                                                                        "size": "2.5GB"},
        {"name": "LMDE 7 Cinnamon",                        "url": "https://ftp.linuxmint.com/stable/lmde7/lmde-7-cinnamon-64bit.iso",                                                                           "size": "2.8GB"},
        {"name": "LMDE 7 MATE",                            "url": "https://ftp.linuxmint.com/stable/lmde7/lmde-7-mate-64bit.iso",                                                                               "size": "2.6GB"},
        {"name": "Linux Mint 22.1 Cinnamon (KKU mirror)",  "url": "https://mirror.kku.ac.th/linuxmint/iso/stable/22.1/linuxmint-22.1-cinnamon-64bit.iso",                                                       "size": "2.9GB"},
        {"name": "Linux Mint 22.1 MATE (KKU mirror)",      "url": "https://mirror.kku.ac.th/linuxmint/iso/stable/22.1/linuxmint-22.1-mate-64bit.iso",                                                           "size": "2.7GB"},
        {"name": "Linux Mint 22.1 Xfce (KKU mirror)",      "url": "https://mirror.kku.ac.th/linuxmint/iso/stable/22.1/linuxmint-22.1-xfce-64bit.iso",                                                           "size": "2.6GB"},
    ],

    # Debian-Based Derivatives
    "linux/debian-based": [
        {"name": "Pop!_OS 22.04 Intel/AMD",                "url": "https://iso.pop-os.org/22.04/amd64/intel/46/pop-os_22.04_amd64_intel_46.iso",                                                                "size": "2.6GB"},
        {"name": "Pop!_OS 22.04 NVIDIA",                   "url": "https://iso.pop-os.org/22.04/amd64/nvidia/46/pop-os_22.04_amd64_nvidia_46.iso",                                                              "size": "2.8GB"},
        {"name": "Zorin OS 17.3 Core",                     "url": "https://downloads.zorinos.com/17/Zorin-OS-17.3-Core-64-bit.iso",                                                                             "size": "3.8GB"},
        {"name": "Zorin OS 17.3 Lite",                     "url": "https://downloads.zorinos.com/17/Zorin-OS-17.3-Lite-64-bit.iso",                                                                             "size": "2.2GB"},
        {"name": "Zorin OS 17.3 Education",                "url": "https://downloads.zorinos.com/17/Zorin-OS-17.3-Education-64-bit.iso",                                                                         "size": "3.9GB"},
        {"name": "elementary OS 8.1",                      "url": "https://downloads.elementary.io/os-8.1-stable.20250301.iso",                                                                                  "size": "2.7GB"},
        {"name": "MX Linux 23.6 x64",                      "url": "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6_x64.iso/download",                                                    "size": "2.7GB"},
        {"name": "MX Linux 23.6 KDE x64",                  "url": "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6-kde_x64.iso/download",                                                "size": "3.2GB"},
        {"name": "antiX 23.2 Full x64",                    "url": "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.2/antiX-23.2_x64-full.iso/download",                                      "size": "1.8GB"},
        {"name": "SparkyLinux 8.0 LXQt",                   "url": "https://sourceforge.net/projects/sparkylinux/files/8.0/sparkylinux-8.0-x86_64-lxqt.iso/download",                                           "size": "2.0GB"},
        {"name": "SparkyLinux 8.0 KDE",                    "url": "https://sourceforge.net/projects/sparkylinux/files/8.0/sparkylinux-8.0-x86_64-kde.iso/download",                                             "size": "2.7GB"},
        {"name": "KDE Neon (current)",                     "url": "https://files.kde.org/neon/images/user/current/neon-user-current.iso",                                                                        "size": "3.1GB"},
        {"name": "Deepin 23.1",                            "url": "https://cdimage.deepin.com/releases/23.1/deepin-desktop-community-23.1-amd64.iso",                                                           "size": "4.2GB"},
        {"name": "Trisquel 11 (fully free)",               "url": "https://ftp.rediris.es/trisquel/iso/nabia/trisquel_11.0_amd64.iso",                                                                          "size": "3.9GB"},
        {"name": "PureOS 10 GNOME",                        "url": "https://downloads.puri.sm/pureOS/10.0/PureOS-10.0-gnome-live.iso",                                                                           "size": "2.6GB"},
        {"name": "GNOME OS nightly",                       "url": "https://os.gnome.org/download/latest/gnome_os_installer_nightly_x86_64.iso",                                                                 "size": "4.0GB"},
        {"name": "Feren OS 22.04",                         "url": "https://sourceforge.net/projects/ferenoslinux/files/22.04/ferenos-22.04-amd64.iso/download",                                                 "size": "3.1GB"},
        {"name": "Nitrux OS 3.8.1",                        "url": "https://sourceforge.net/projects/nitruxos/files/Release/ISO/Nitrux_OS_3.8.1-nx-desktop-amd64.iso/download",                                 "size": "3.4GB"},
        {"name": "BigLinux 2024-11-15",                    "url": "https://sourceforge.net/projects/biglinux/files/BigLinux_2024-11-15.iso/download",                                                           "size": "3.5GB"},
        {"name": "XeroLinux KDE 2025.03",                  "url": "https://sourceforge.net/projects/xerolinux/files/XeroLinux-KDE-2025.03.iso/download",                                                        "size": "3.2GB"},
        {"name": "SpiralLinux KDE 12",                     "url": "https://spirallinux.github.io/ISO/SpiralLinux_KDE_12.231101_x86-64.iso",                                                                     "size": "3.3GB"},
        {"name": "Rhino Linux 2024.1",                     "url": "https://sourceforge.net/projects/rhinolinux/files/rhino-linux-2024.1.iso/download",                                                          "size": "2.8GB"},
        {"name": "Q4OS 5.4 Trinity",                       "url": "https://sourceforge.net/projects/q4osinux/files/q4os-5.4-amd64.r1-trinity.iso/download",                                                    "size": "1.4GB"},
        {"name": "Voyager 24.04 Xfce",                     "url": "https://sourceforge.net/projects/linuxvoyager/files/voyager-24.04-amd64.iso/download",                                                       "size": "3.1GB"},
        {"name": "Hyperbola 0.4.1 (fully free)",           "url": "https://www.hyperbola.info/downloads/isos/hyperbola-0.4.1-x86_64.iso",                                                                       "size": "1.8GB"},
    ],

    # Enterprise / RPM
    "linux/enterprise": [
        {"name": "Fedora 43 Workstation",                  "url": "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-43-1.1.iso",           "size": "2.1GB"},
        {"name": "Fedora 43 Server DVD",                   "url": "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Server/x86_64/iso/Fedora-Server-dvd-x86_64-43-1.1.iso",                     "size": "2.4GB"},
        {"name": "Fedora 43 Everything Netinstall",        "url": "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Everything/x86_64/iso/Fedora-Everything-netinst-x86_64-43-1.1.iso",          "size": "780MB"},
        {"name": "AlmaLinux 9.5 DVD (KKU)",                "url": "https://mirror.kku.ac.th/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-dvd.iso",                                                           "size": "10.4GB"},
        {"name": "AlmaLinux 9.5 Minimal (KKU)",            "url": "https://mirror.kku.ac.th/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-minimal.iso",                                                       "size": "1.8GB"},
        {"name": "Rocky Linux 9.5 DVD (KKU)",              "url": "https://mirror.kku.ac.th/rocky/9.5/isos/x86_64/Rocky-9.5-x86_64-dvd.iso",                                                                   "size": "10.6GB"},
        {"name": "Rocky Linux 9.5 Minimal (KKU)",          "url": "https://mirror.kku.ac.th/rocky/9.5/isos/x86_64/Rocky-9.5-x86_64-minimal.iso",                                                               "size": "1.9GB"},
        {"name": "Oracle Linux 9.5 DVD",                   "url": "https://yum.oracle.com/ISOS/OracleLinux/OL9/u5/x86_64/OracleLinux-R9-U5-x86_64-dvd.iso",                                                    "size": "10.0GB"},
        {"name": "Oracle Linux 9.5 Boot",                  "url": "https://yum.oracle.com/ISOS/OracleLinux/OL9/u5/x86_64/OracleLinux-R9-U5-x86_64-boot.iso",                                                   "size": "960MB"},
        {"name": "CentOS Stream 9 DVD",                    "url": "https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso",                                         "size": "9.5GB"},
        {"name": "CentOS Stream 9 Boot",                   "url": "https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-boot.iso",                                         "size": "960MB"},
        {"name": "openSUSE Leap 15.6 DVD",                 "url": "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-DVD-x86_64-Media.iso",                                           "size": "4.7GB"},
        {"name": "openSUSE Leap 15.6 GNOME Live",          "url": "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-GNOME-Live-x86_64-Media.iso",                                    "size": "1.2GB"},
        {"name": "openSUSE Leap 15.6 KDE Live",            "url": "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-KDE-Live-x86_64-Media.iso",                                      "size": "1.3GB"},
        {"name": "openSUSE Tumbleweed DVD (rolling)",       "url": "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso",                                                    "size": "4.9GB"},
        {"name": "openSUSE Tumbleweed KDE Live",           "url": "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-KDE-Live-x86_64-Current.iso",                                               "size": "1.4GB"},
        {"name": "openSUSE Tumbleweed GNOME Live",         "url": "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-GNOME-Live-x86_64-Current.iso",                                             "size": "1.3GB"},
        {"name": "GeckoLinux Static KDE 999",              "url": "https://sourceforge.net/projects/geckolinux/files/Static/999.230801/GeckoLinux_STATIC_KDE.x86_64-999.230801.0.iso/download",                 "size": "2.0GB"},
        {"name": "EuroLinux 9.4 Desktop",                  "url": "https://fbi.cdn.euro-linux.com/iso/EuroLinux-9.4-x86_64-dvd.iso",                                                                           "size": "9.8GB"},
        {"name": "Springdale Linux 9.4 (Princeton)",       "url": "https://springdale.math.ias.edu/distributions/9/x86_64/iso/SDL9-9.4-20240515.x86_64.iso",                                                   "size": "9.5GB"},
    ],

    # Fedora Spins & Labs
    "linux/fedora-spins": [
        {"name": "Fedora 43 KDE Spin",                     "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-KDE-Live-x86_64-43-1.1.iso",                              "size": "2.6GB"},
        {"name": "Fedora 43 Xfce Spin",                    "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-Xfce-Live-x86_64-43-1.1.iso",                             "size": "1.7GB"},
        {"name": "Fedora 43 Cinnamon Spin",                "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-Cinnamon-Live-x86_64-43-1.1.iso",                         "size": "2.3GB"},
        {"name": "Fedora 43 LXDE Spin",                    "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-LXDE-Live-x86_64-43-1.1.iso",                             "size": "1.5GB"},
        {"name": "Fedora 43 LXQt Spin",                    "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-LXQt-Live-x86_64-43-1.1.iso",                             "size": "1.6GB"},
        {"name": "Fedora 43 MATE Compiz Spin",             "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-MATE_Compiz-Live-x86_64-43-1.1.iso",                      "size": "2.0GB"},
        {"name": "Fedora 43 Sway Spin",                    "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-Sway-Live-x86_64-43-1.1.iso",                             "size": "1.8GB"},
        {"name": "Fedora 43 i3 Spin",                      "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-i3-Live-x86_64-43-1.1.iso",                               "size": "1.7GB"},
        {"name": "Fedora 43 Budgie Spin",                  "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-Budgie-Live-x86_64-43-1.1.iso",                           "size": "2.1GB"},
        {"name": "Fedora 43 COSMIC Spin",                  "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-Cosmic-Live-x86_64-43-1.1.iso",                           "size": "2.2GB"},
        {"name": "Fedora 43 Lab: Scientific KDE",          "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Scientific_KDE-Live-x86_64-43-1.1.iso",                    "size": "3.7GB"},
        {"name": "Fedora 43 Lab: Security",                "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Security-Live-x86_64-43-1.1.iso",                          "size": "2.4GB"},
        {"name": "Fedora 43 Lab: Design Suite",            "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Design_suite-Live-x86_64-43-1.1.iso",                      "size": "2.8GB"},
        {"name": "Fedora 43 Lab: Robotics Suite",          "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Robotics_Suite-Live-x86_64-43-1.1.iso",                    "size": "3.1GB"},
        {"name": "Fedora 43 Lab: Gaming",                  "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Gaming-Live-x86_64-43-1.1.iso",                            "size": "3.4GB"},
        {"name": "Fedora 43 Lab: Jam KDE",                 "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Jam_KDE-Live-x86_64-43-1.1.iso",                           "size": "2.9GB"},
    ],

    # Immutable / Atomic Desktops
    "linux/immutable": [
        {"name": "Fedora Silverblue 43",                   "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Silverblue/x86_64/iso/Fedora-Silverblue-ostree-x86_64-43-1.1.iso",                "size": "2.3GB"},
        {"name": "Fedora Kinoite 43",                      "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Kinoite/x86_64/iso/Fedora-Kinoite-ostree-x86_64-43-1.1.iso",                      "size": "2.4GB"},
        {"name": "Fedora Sericea 43",                      "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Sericea/x86_64/iso/Fedora-Sericea-ostree-x86_64-43-1.1.iso",                      "size": "1.9GB"},
        {"name": "Fedora Onyx 43",                         "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Onyx/x86_64/iso/Fedora-Onyx-ostree-x86_64-43-1.1.iso",                            "size": "2.2GB"},
        {"name": "openSUSE MicroOS DVD",                   "url": "https://download.opensuse.org/distribution/microos/iso/openSUSE-MicroOS-DVD-x86_64-Current.iso",                                             "size": "1.8GB"},
        {"name": "Vanilla OS 2 Desktop",                   "url": "https://github.com/Vanilla-OS/os/releases/latest/download/vanillaos-2-desktop-amd64.iso",                                                   "size": "2.0GB"},
        {"name": "NixOS 24.11 GNOME",                      "url": "https://channels.nixos.org/nixos-24.11/latest-nixos-gnome-x86_64-linux.iso",                                                                "size": "2.4GB"},
        {"name": "NixOS 24.11 Plasma6",                    "url": "https://channels.nixos.org/nixos-24.11/latest-nixos-plasma6-x86_64-linux.iso",                                                              "size": "2.5GB"},
        {"name": "NixOS 24.11 Minimal",                    "url": "https://channels.nixos.org/nixos-24.11/latest-nixos-minimal-x86_64-linux.iso",                                                              "size": "1.0GB"},
        {"name": "Endless OS 6.0.0",                       "url": "https://images.endlessos.com/reimage/endless-eos6.0.0-amd64-amd64.200-base.iso",                                                            "size": "16.0GB"},
        {"name": "Bazzite (stable)",                       "url": "https://download.bazzite.gg/Bazzite-stable.iso",                                                                                             "size": "4.0GB"},
    ],

    # Rolling Distros
    "linux/rolling": [
        {"name": "Solus 4.6 Budgie",                       "url": "https://mirrors.rit.edu/solus/images/4.6/Solus-4.6-Budgie.iso",                                                                              "size": "2.0GB"},
        {"name": "Solus 4.6 GNOME",                        "url": "https://mirrors.rit.edu/solus/images/4.6/Solus-4.6-GNOME.iso",                                                                               "size": "2.0GB"},
        {"name": "Solus 4.6 Plasma",                       "url": "https://mirrors.rit.edu/solus/images/4.6/Solus-4.6-Plasma.iso",                                                                              "size": "2.1GB"},
        {"name": "Void Linux 20250201",                    "url": "https://repo-default.voidlinux.org/live/current/void-live-x86_64-20250201.iso",                                                              "size": "900MB"},
        {"name": "Void Linux musl 20250201",               "url": "https://repo-default.voidlinux.org/live/current/void-live-x86_64-musl-20250201.iso",                                                         "size": "900MB"},
        {"name": "Void Linux Xfce 20250201",               "url": "https://repo-default.voidlinux.org/live/current/void-live-x86_64-xfce-20250201.iso",                                                        "size": "1.1GB"},
        {"name": "Devuan 5.0.1 Desktop",                   "url": "https://files.devuan.org/devuan_excalibur/installer-iso/devuan_excalibur_5.0.1_amd64_desktop.iso",                                          "size": "3.2GB"},
        {"name": "Devuan 5.0.1 Minimal Live",              "url": "https://files.devuan.org/devuan_excalibur/installer-iso/devuan_excalibur_5.0.1_amd64_minimal-live.iso",                                     "size": "750MB"},
        {"name": "PCLinuxOS KDE 2024.12",                  "url": "https://ftp.nluug.nl/os/Linux/distr/pclinuxos/pclinuxos/live-cd/pclinuxos64-KDE-2024.12.iso",                                                "size": "3.5GB"},
        {"name": "Mageia 9 DVD",                           "url": "https://distrib-coffee.ipsl.jussieu.fr/pub/linux/Mageia/iso/9/Mageia-9-x86_64-DVD.iso",                                                     "size": "4.8GB"},
        {"name": "OpenMandriva 24.12 Plasma6",             "url": "https://sourceforge.net/projects/openmandriva/files/release/24.12/OpenMandriva-24.12-plasma6.x86_64.iso/download",                          "size": "2.4GB"},
        {"name": "Calculate Linux Desktop 25",             "url": "https://www.calculate-linux.org/downloads/en/cld/amd64/current/cld-amd64.iso",                                                               "size": "3.0GB"},
        {"name": "Siduction 2021.3.0 (Debian sid)",        "url": "https://sourceforge.net/projects/siduction/files/21.3.0/siduction-21.3.0-wintermute-kde-amd64-202112231901.iso/download",                    "size": "3.2GB"},
        {"name": "antiX 23.2 Runit x64",                   "url": "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.2/antiX-23.2-runit_x64-full.iso/download",                                "size": "1.8GB"},
        {"name": "Pisi Linux 2.1 (KDE)",                   "url": "https://sourceforge.net/projects/pisilinux/files/2.1/pisi-linux-2.1-plasma-x86_64.iso/download",                                             "size": "2.3GB"},
    ],

    # Minimal / DIY
    "linux/minimal": [
        {"name": "Alpine Linux 3.21.3 Standard",           "url": "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-standard-3.21.3-x86_64.iso",                                             "size": "215MB"},
        {"name": "Alpine Linux 3.21.3 Extended",           "url": "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-extended-3.21.3-x86_64.iso",                                             "size": "625MB"},
        {"name": "Alpine Linux 3.21.3 Virt",               "url": "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-virt-3.21.3-x86_64.iso",                                                 "size": "210MB"},
        {"name": "TinyCore Pure64 16.0",                   "url": "http://tinycorelinux.net/16.x/x86_64/release/CorePure64-16.0.iso",                                                                          "size": "17MB"},
        {"name": "TinyCore 16.x (32-bit)",                 "url": "http://tinycorelinux.net/16.x/x86/release/TinyCore-current.iso",                                                                            "size": "21MB"},
        {"name": "Slackware 15.0 Install DVD",             "url": "https://slackware.uk/slackware/slackware64-15.0/slackware64-15.0-install-dvd.iso",                                                          "size": "8.0GB"},
        {"name": "Gentoo Live GUI (amd64)",                "url": "https://gentoo.osuosl.org/releases/amd64/autobuilds/current-livegui-amd64/livegui-amd64.iso",                                               "size": "4.5GB"},
        {"name": "Clear Linux (live, latest)",             "url": "https://cdn.download.clearlinux.org/releases/current/clear/clear-live.iso",                                                                  "size": "2.1GB"},
        {"name": "Parabola GNU/Linux-libre 2025.02",       "url": "https://redirector.parabolagnulinux.org/iso/2025.02/parabola-systemd-2025.02.01-netinstall-multilib-x86_64.iso",                            "size": "800MB"},
        {"name": "Salix 15.0 Xfce",                        "url": "https://sourceforge.net/projects/salix/files/15.0/salix64-xfce-15.0.iso/download",                                                          "size": "1.6GB"},
        {"name": "Slax 11.6 (Debian-based)",               "url": "https://www.slax.org/download.php?type=x86_64&file=slax-64bit-11.6.0.iso",                                                                  "size": "340MB"},
        {"name": "4MLinux 45.0",                           "url": "https://sourceforge.net/projects/linux4m/files/45.0/4MLinux-45.0-x86_64.iso/download",                                                      "size": "900MB"},
        {"name": "ArchBang (Arch + Openbox)",              "url": "https://sourceforge.net/projects/archbang/files/archbang-1205-x86_64.iso/download",                                                          "size": "950MB"},
        {"name": "Crux 3.7 (source-based, minimal)",       "url": "https://crux.nu/files/releases/3.7/crux-3.7.iso",                                                                                            "size": "660MB"},
        {"name": "Adelie Linux 1.0 Beta4",                 "url": "https://distfiles.adelielinux.org/adelie/1.0/iso/beta4/adelie-live-x86_64-1.0-beta4-20210818.iso",                                           "size": "530MB"},
    ],

    # Lightweight
    "linux/lightweight": [
        {"name": "MX Linux 23.6 Fluxbox",                  "url": "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6_fluxbox_x64.iso/download",                                           "size": "2.1GB"},
        {"name": "antiX 23.1 Full x64",                    "url": "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.1/antiX-23.1_x64-full.iso/download",                                     "size": "1.6GB"},
        {"name": "antiX 23.1 Base x64",                    "url": "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.1/antiX-23.1_x64-base.iso/download",                                     "size": "1.0GB"},
        {"name": "antiX 23.1 Net x64",                     "url": "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23.1/antiX-23.1_x64-net.iso/download",                                      "size": "600MB"},
        {"name": "Puppy Linux FossaPup64 9.5",             "url": "https://sourceforge.net/projects/puppylinux/files/puppy-fossa/fossapup64-9.5.iso/download",                                                  "size": "450MB"},
        {"name": "Linux Lite 7.2",                         "url": "https://sourceforge.net/projects/linuxlite/files/7.2/linux-lite-7.2-64bit.iso/download",                                                    "size": "2.0GB"},
        {"name": "Bodhi Linux 7.0",                        "url": "https://sourceforge.net/projects/bodhilinux/files/7.0.0/bodhi-7.0.0-64.iso/download",                                                       "size": "1.1GB"},
        {"name": "LXLE 22.04.3",                           "url": "https://sourceforge.net/projects/lxle/files/LXLE22043/lxle-22043-64bit.iso/download",                                                       "size": "1.8GB"},
        {"name": "Porteus 5.0 x86_64",                     "url": "https://sourceforge.net/projects/porteus/files/Porteus-v5.0-x86_64.iso/download",                                                           "size": "350MB"},
        {"name": "SliTaz 5.0 (30MB)",                      "url": "https://mirror.slitaz.org/iso/5.0/slitaz-5.0.iso",                                                                                          "size": "30MB"},
        {"name": "Absolute Linux 15.0.19",                 "url": "https://sourceforge.net/projects/absolute-linux/files/Absolute-15.0.19/absolute-15.0.19.iso/download",                                      "size": "2.1GB"},
        {"name": "Peppermint OS 12",                       "url": "https://peppermintos.com/iso/Peppermint-12-20240201-amd64.iso",                                                                              "size": "1.8GB"},
        {"name": "KNOPPIX 9.1",                            "url": "https://ftp.knoppix.nl/os/Linux/distr/knoppix/KNOPPIX_V9.1CD-2021-01-25-EN.iso",                                                            "size": "3.7GB"},
        {"name": "Bunsenlabs Lithium 10.6",                "url": "https://sourceforge.net/projects/bunsen/files/BunsenLabs-Lithium-amd64.iso/download",                                                        "size": "1.6GB"},
        {"name": "Linux Mint Debian Edition 6 (Faye)",     "url": "https://ftp.linuxmint.com/stable/lmde6/lmde-6-cinnamon-64bit.iso",                                                                           "size": "2.7GB"},
        {"name": "Trisquel Mini 11 (LXDE, fully free)",    "url": "https://ftp.rediris.es/trisquel/iso/nabia/trisquelmini_11.0_amd64.iso",                                                                      "size": "1.2GB"},
    ],

    # Gaming
    "linux/gaming": [
        {"name": "Bazzite (stable, gaming)",               "url": "https://download.bazzite.gg/Bazzite-stable.iso",                                                                                             "size": "4.0GB"},
        {"name": "Fedora 43 Gaming Lab",                   "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Gaming-Live-x86_64-43-1.1.iso",                            "size": "3.4GB"},
        {"name": "Nobara 43 (gaming-patched Fedora)",       "url": "https://nobara-images.nobaraproject.org/Nobara-43-Official-2025-10-01.iso",                                                                  "size": "4.0GB"},
        {"name": "ChimeraOS (SteamOS-like, latest)",       "url": "https://chimeraos.org/images/latest/chimera-latest.iso",                                                                                     "size": "3.5GB"},
        {"name": "Drauger OS 7.6",                         "url": "https://draugeros.org/iso/drauger-os-7.6-amd64.iso",                                                                                         "size": "3.2GB"},
        {"name": "Lakka 5.0 Generic x86_64",               "url": "https://le-builds.lakka.tv/Generic.x86_64/Lakka-Generic.x86_64-5.0.iso",                                                                    "size": "550MB"},
        {"name": "Batocera Linux v40 x86_64",              "url": "https://mirrors.o2switch.fr/batocera/x86_64/stable/last/batocera-x86_64-40.img.gz",                                                          "size": "2.4GB"},
        {"name": "RetroPie x86 4.8",                       "url": "https://downloads.retropie.org.uk/RetroPie-x86/retropie-buster-4.8-x86.iso",                                                                "size": "2.2GB"},
        {"name": "Manjaro Gaming (KDE-based)",             "url": "https://download.manjaro.org/kde/24.2/manjaro-kde-24.2-260331-linux612.iso",                                                                 "size": "4.2GB"},
        {"name": "SteamOS 3.x (deck image reference)",     "url": "https://store.steampowered.com/steamos/download/?ver=steamdeck&snr=",                                                                        "size": "3.7GB"},
    ],

    # Security / Pentesting
    "linux/security": [
        {"name": "Kali Linux 2025.1 Installer",            "url": "https://cdimage.kali.org/kali-2025.1/kali-linux-2025.1-installer-amd64.iso",                                                                "size": "4.1GB"},
        {"name": "Kali Linux 2025.1 Everything",           "url": "https://cdimage.kali.org/kali-2025.1/kali-linux-2025.1-installer-everything-amd64.iso",                                                     "size": "13.1GB"},
        {"name": "Kali Linux 2025.1 Live",                 "url": "https://cdimage.kali.org/kali-2025.1/kali-linux-2025.1-live-amd64.iso",                                                                     "size": "3.9GB"},
        {"name": "Kali Linux 2025.1 (KKU mirror)",         "url": "https://mirror.kku.ac.th/kali-images/kali-2025.1/kali-linux-2025.1-installer-amd64.iso",                                                    "size": "4.1GB"},
        {"name": "Parrot Security 6.2",                    "url": "https://ftp.nluug.nl/os/Linux/distr/parrotsec/iso/6.2/Parrot-security-6.2_x64.iso",                                                         "size": "5.1GB"},
        {"name": "Parrot Home 6.2",                        "url": "https://ftp.nluug.nl/os/Linux/distr/parrotsec/iso/6.2/Parrot-home-6.2_x64.iso",                                                             "size": "2.7GB"},
        {"name": "BackBox 9",                              "url": "https://releases.backbox.org/backbox-9-desktop-amd64.iso",                                                                                   "size": "3.0GB"},
        {"name": "REMnux v7 (malware analysis)",           "url": "https://remnux.org/downloads/remnux-v7-focal-ova.iso",                                                                                       "size": "3.0GB"},
        {"name": "DEFT Zero 2018.2 (forensics)",           "url": "https://sourceforge.net/projects/deft/files/DEFT-Zero/2018.2/deft-zero-2018.2.iso/download",                                                "size": "2.2GB"},
        {"name": "Pentoo 2024.0 (Gentoo security)",        "url": "https://sourceforge.net/projects/pentoo/files/Pentoo/2024.0/pentoo-amd64-2024.0.iso/download",                                              "size": "6.5GB"},
        {"name": "BlackArch Slim 2025.01.01",              "url": "https://ftp.halifax.rwth-aachen.de/blackarch/iso/blackarch-linux-slim-2025.01.01-x86_64.iso",                                               "size": "4.0GB"},
        {"name": "Fedora 43 Security Lab",                 "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Security-Live-x86_64-43-1.1.iso",                         "size": "2.4GB"},
        {"name": "CAINE 14 (computer forensics)",          "url": "https://www.caine-live.net/caine14/caine14.0.iso",                                                                                           "size": "3.7GB"},
        {"name": "Tsurugi Linux 2024.1 (DFIR)",            "url": "https://sourceforge.net/projects/tsurugi-linux/files/2024.1/tsurugi-linux-2024.1-amd64.iso/download",                                       "size": "17.0GB"},
        {"name": "Whonix Workstation 17 (KVM)",            "url": "https://download.whonix.org/libvirt/17.2.3.7/Whonix-Workstation-XFCE-17.2.3.7.Intel_AMD64.qcow2.libvirt.xz",                               "size": "1.6GB"},
    ],

    # Privacy
    "linux/privacy": [
        {"name": "Tails 6.13",                             "url": "https://tails.net/torrents/files/tails-amd64-6.13.iso",                                                                                      "size": "1.4GB"},
        {"name": "Qubes OS 4.2.3",                         "url": "https://ftp.qubes-os.org/iso/Qubes-R4.2.3-x86_64.iso",                                                                                      "size": "6.5GB"},
        {"name": "Whonix 17.2.3.7 Xfce (OVA)",            "url": "https://download.whonix.org/ova/17.2.3.7/Whonix-Xfce-17.2.3.7.ova",                                                                         "size": "1.7GB"},
        {"name": "Kodachi 9 (privacy live)",               "url": "https://sourceforge.net/projects/linuxkodachi/files/kodachi-9-64.iso/download",                                                              "size": "4.0GB"},
        {"name": "Heads (QubesOS variant)",                "url": "https://github.com/heads-os/heads/releases/latest/download/heads-amd64.iso",                                                                 "size": "2.8GB"},
        {"name": "PlagueOS (live, airgap-focused)",        "url": "https://sourceforge.net/projects/plagueos/files/latest/download",                                                                            "size": "1.2GB"},
        {"name": "Alpine Linux 3.21.3 (privacy minimal)",  "url": "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-standard-3.21.3-x86_64.iso",                                             "size": "215MB"},
    ],

    # Education
    "linux/education": [
        {"name": "Edubuntu 24.04.2",                       "url": "https://cdimage.ubuntu.com/edubuntu/releases/24.04.2/release/edubuntu-24.04.2-desktop-amd64.iso",                                            "size": "4.8GB"},
        {"name": "Edubuntu 22.04.5",                       "url": "https://cdimage.ubuntu.com/edubuntu/releases/22.04.5/release/edubuntu-22.04.5-desktop-amd64.iso",                                            "size": "4.5GB"},
        {"name": "Debian Edu 12+edu2",                     "url": "https://ftp.skolelinux.com/skolelinux/debian-edu-12+edu2-CD.iso",                                                                            "size": "700MB"},
        {"name": "Sugar on a Stick 14.0",                  "url": "https://download.sugarlabs.org/releases/14.0/sugar-live-build.iso",                                                                          "size": "1.3GB"},
        {"name": "Zorin OS 17.3 Education",                "url": "https://downloads.zorinos.com/17/Zorin-OS-17.3-Education-64-bit.iso",                                                                         "size": "3.9GB"},
        {"name": "Fedora 43 Robotics Suite Lab",           "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Robotics_Suite-Live-x86_64-43-1.1.iso",                    "size": "3.1GB"},
        {"name": "openSUSE Education Li-f-e 42.3",        "url": "https://download.opensuse.org/education/release/42.3/openSUSE-Edu-li-f-e-42.3-0-i586_x86_64.iso",                                            "size": "4.7GB"},
        {"name": "UberStudent 5.1 Athena",                 "url": "https://sourceforge.net/projects/uberstudent/files/UberStudent/5.1/UberStudent-5.1-Athena-amd64.iso/download",                               "size": "3.0GB"},
    ],

    # Multimedia / Audio Production
    "linux/multimedia": [
        {"name": "Ubuntu Studio 24.04.2",                  "url": "https://cdimage.ubuntu.com/ubuntustudio/releases/24.04.2/release/ubuntustudio-24.04.2-dvd-amd64.iso",                                        "size": "4.9GB"},
        {"name": "Ubuntu Studio 22.04.5",                  "url": "https://cdimage.ubuntu.com/ubuntustudio/releases/22.04.5/release/ubuntustudio-22.04.5-dvd-amd64.iso",                                        "size": "4.7GB"},
        {"name": "AV Linux MXE 2023.11.19",                "url": "https://sourceforge.net/projects/avlinux/files/2023.11.19/AV_Linux_MXE_2023.11.19_x86_64.iso/download",                                     "size": "3.1GB"},
        {"name": "Fedora 43 Jam KDE (audio production)",   "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Jam_KDE-Live-x86_64-43-1.1.iso",                           "size": "2.9GB"},
        {"name": "KXStudio 14.04.5",                       "url": "https://downloads.sourceforge.net/project/kxstudio/Releases/KXStudio_14.04.5_amd64.iso",                                                    "size": "2.5GB"},
        {"name": "Fedora 43 Design Suite Lab",             "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Design_suite-Live-x86_64-43-1.1.iso",                      "size": "2.8GB"},
    ],

    # Server
    "linux/server": [
        {"name": "Ubuntu 24.04.2 Server (KKU)",            "url": "https://mirror.kku.ac.th/ubuntu-cd/24.04.2/ubuntu-24.04.2-live-server-amd64.iso",                                                            "size": "2.6GB"},
        {"name": "Ubuntu 22.04.5 Server (KKU)",            "url": "https://mirror.kku.ac.th/ubuntu-cd/22.04.5/ubuntu-22.04.5-live-server-amd64.iso",                                                            "size": "2.1GB"},
        {"name": "Ubuntu 25.04 Server",                    "url": "https://releases.ubuntu.com/25.04/ubuntu-25.04-live-server-amd64.iso",                                                                       "size": "2.7GB"},
        {"name": "AlmaLinux 9.5 DVD (KKU)",                "url": "https://mirror.kku.ac.th/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-dvd.iso",                                                           "size": "10.4GB"},
        {"name": "Rocky Linux 9.5 DVD (KKU)",              "url": "https://mirror.kku.ac.th/rocky/9.5/isos/x86_64/Rocky-9.5-x86_64-dvd.iso",                                                                   "size": "10.6GB"},
        {"name": "Fedora 43 Server DVD",                   "url": "https://download.fedoraproject.org/pub/fedora/linux/releases/43/Server/x86_64/iso/Fedora-Server-dvd-x86_64-43-1.1.iso",                     "size": "2.4GB"},
        {"name": "CentOS Stream 9 DVD",                    "url": "https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso",                                         "size": "9.5GB"},
        {"name": "Debian 12.10 Netinstall",                "url": "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.10.0-amd64-netinst.iso",                                                 "size": "660MB"},
        {"name": "Debian 11.11 Netinstall (LTS)",          "url": "https://cdimage.debian.org/cdimage/archive/11.11.0/amd64/iso-cd/debian-11.11.0-amd64-netinst.iso",                                           "size": "400MB"},
        {"name": "openSUSE Leap 15.6 DVD",                 "url": "https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-DVD-x86_64-Media.iso",                                           "size": "4.7GB"},
        {"name": "Oracle Linux 9.5 DVD",                   "url": "https://yum.oracle.com/ISOS/OracleLinux/OL9/u5/x86_64/OracleLinux-R9-U5-x86_64-dvd.iso",                                                    "size": "10.0GB"},
    ],

    # Scientific
    "linux/scientific": [
        {"name": "Fedora 43 Scientific KDE",               "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Labs/x86_64/iso/Fedora-Scientific_KDE-Live-x86_64-43-1.1.iso",                    "size": "3.7GB"},
        {"name": "Scientific Linux 7.9 Boot",              "url": "https://ftp.scientificlinux.org/linux/scientific/7.9/x86_64/iso/SL-7.9-x86_64-2021-01-26-boot.iso",                                         "size": "800MB"},
        {"name": "Scientific Linux 7.9 Everything DVD1",   "url": "https://ftp.scientificlinux.org/linux/scientific/7.9/x86_64/iso/SL-7.9-x86_64-2021-01-26-Everything-DVD1.iso",                              "size": "8.9GB"},
        {"name": "Bio-Linux 8.0 (bioinformatics)",         "url": "https://nebc.nox.ac.uk/tools/bio-linux/bio-linux-8.0.iso",                                                                                   "size": "4.0GB"},
    ],

    # Homelab: Virtualization
    "homelab/virtualization": [
        {"name": "Proxmox VE 8.3",                         "url": "https://enterprise.proxmox.com/iso/proxmox-ve_8.3-1.iso",                                                                                    "size": "1.3GB"},
        {"name": "XCP-ng 8.3.0",                           "url": "https://updates.xcp-ng.org/isos/8.3.0/xcp-ng-8.3.0.iso",                                                                                    "size": "1.0GB"},
        {"name": "VirtIO Windows Drivers (stable)",        "url": "https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso",                                               "size": "530MB"},
        {"name": "CloneZilla 3.2.0-5",                     "url": "https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/3.2.0-5/clonezilla-live-3.2.0-5-amd64.iso/download",              "size": "490MB"},
        {"name": "Harvester HCI v1.4.0",                   "url": "https://releases.rancher.com/harvester/v1.4.0/harvester-v1.4.0-amd64.iso",                                                                   "size": "4.6GB"},
        {"name": "oVirt 4.5.3 Node",                       "url": "https://resources.ovirt.org/pub/ovirt-4.5/iso/ovirt-node-ng-installer-4.5.3-2023060913.el8.iso",                                            "size": "1.5GB"},
        {"name": "DRBL 2.32.1 Live",                       "url": "https://sourceforge.net/projects/drbl/files/drbl_stable/2.32.1/drbl-live-stable-2.32.1-amd64.iso/download",                                  "size": "500MB"},
        {"name": "Proxmox Backup Server 3.2",              "url": "https://enterprise.proxmox.com/iso/proxmox-backup-server_3.2-1.iso",                                                                          "size": "1.1GB"},
    ],

    # Homelab: NAS
    "homelab/nas": [
        {"name": "TrueNAS SCALE 24.10.2",                  "url": "https://download.truenas.com/TrueNAS-SCALE-24.10.2/TrueNAS-SCALE-24.10.2.iso",                                                               "size": "2.3GB"},
        {"name": "TrueNAS CORE 13.0-U6.2 (FreeBSD)",       "url": "https://download.truenas.com/TrueNAS-CORE-13.0-U6.2/TrueNAS-CORE-13.0-U6.2.iso",                                                            "size": "1.2GB"},
        {"name": "OpenMediaVault 7.4.7",                   "url": "https://sourceforge.net/projects/openmediavault/files/7.4.7/openmediavault_7.4.7-amd64.iso/download",                                        "size": "1.1GB"},
        {"name": "Rockstor 5.0.15",                        "url": "https://sourceforge.net/projects/rockstor/files/5.0.15-0/Rockstor-5.0.15-0-x86_64.iso/download",                                            "size": "2.2GB"},
        {"name": "XigmaNAS 13.3.0",                        "url": "https://sourceforge.net/projects/xigmanas/files/XigmaNAS-13.3/XigmaNAS-x64-13.3.0.9.1.iso/download",                                        "size": "1.0GB"},
        {"name": "Amahi HDA7",                             "url": "https://sourceforge.net/projects/amahi/files/hda7.iso/download",                                                                              "size": "900MB"},
        {"name": "EasyNAS 1.0.0",                          "url": "https://sourceforge.net/projects/easynascloud/files/v1.0.0/easynascloud-1.0.0-amd64.iso/download",                                           "size": "1.4GB"},
    ],

    # Homelab: Networking / Firewall
    "homelab/networking": [
        {"name": "pfSense CE 2.7.2",                       "url": "https://frafiles.netgate.com/mirror/downloads/pfSense-CE-2.7.2-RELEASE-amd64.iso.gz",                                                       "size": "800MB"},
        {"name": "OPNsense 25.1 DVD",                      "url": "https://mirror.opnsense.org/releases/25.1/OPNsense-25.1-dvd-amd64.iso",                                                                      "size": "1.1GB"},
        {"name": "IPFire 2.29 Core190",                    "url": "https://downloads.ipfire.org/releases/ipfire-2.x/2.29-core190/ipfire-2.29.x86_64-full-core190.iso",                                          "size": "600MB"},
        {"name": "VyOS 1.4 Rolling",                       "url": "https://downloads.vyos.io/release/stream/1.4/VyOS-1.4-rolling-202412010026-amd64.iso",                                                       "size": "580MB"},
        {"name": "ClearOS 7.9 Core",                       "url": "https://sourceforge.net/projects/clearos/files/clearos-7.9-core.x86_64.iso/download",                                                       "size": "2.0GB"},
        {"name": "Untangle NG Firewall 17.0",              "url": "https://downloads.untangle.com/untangle-17.0-x86_64.iso",                                                                                    "size": "1.8GB"},
        {"name": "ZeroShell 3.9.5",                        "url": "https://zeroshell.org/download/ZeroShell-3.9.5-x86_64.iso",                                                                                  "size": "600MB"},
        {"name": "IPCop 2.1.9",                            "url": "https://sourceforge.net/projects/ipcop/files/IPCop-2.1.9-install-cd.i486.iso/download",                                                     "size": "130MB"},
        {"name": "OpenWrt 23.05.5 x86_64 (ext4)",          "url": "https://downloads.openwrt.org/releases/23.05.5/targets/x86/64/openwrt-23.05.5-x86-64-generic-ext4-combined.img.gz",                         "size": "130MB"},
    ],

    # Recovery / Rescue Tools
    "recovery/tools": [
        {"name": "SystemRescue 11.03",                     "url": "https://mirror.kku.ac.th/systemrescue/systemrescue-11.03-amd64.iso",                                                                         "size": "1.1GB"},
        {"name": "GParted Live 1.6.0-10",                  "url": "https://download.gparted.org/gparted-live-stable/1.6.0-10/gparted-live-1.6.0-10-amd64.iso",                                                 "size": "660MB"},
        {"name": "CloneZilla 3.2.0-5",                     "url": "https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/3.2.0-5/clonezilla-live-3.2.0-5-amd64.iso/download",              "size": "490MB"},
        {"name": "Rescuezilla 2.5.0",                      "url": "https://download.rescuezilla.com/rescuezilla-2.5.0-64bit.iso",                                                                               "size": "1.2GB"},
        {"name": "Ultimate Boot CD 5.3.9",                 "url": "https://sourceforge.net/projects/ubcd/files/ubcd/5.3.9/ubcd539.iso/download",                                                                "size": "960MB"},
        {"name": "qt-fsarchiver 18.06.3",                  "url": "https://sourceforge.net/projects/qt-fsarchiver/files/qt-fsarchiver-18.06.3-x86_64.iso/download",                                             "size": "600MB"},
        {"name": "Hiren's Boot CD PE x64",                 "url": "https://www.hirensbootcd.org/files/HBCD_PE_x64.iso",                                                                                         "size": "2.7GB"},
        {"name": "netboot.xyz (iPXE network boot)",        "url": "https://boot.netboot.xyz/ipxe/netboot.xyz.iso",                                                                                              "size": "2MB"},
        {"name": "ShredOS 2023.04 (disk erasure)",         "url": "https://github.com/PartialVolume/shredos.x86_64/releases/download/v2023.04.01_26_x86-64_0.38.4/shredos_2023.04.01_26_x86-64.img",          "size": "50MB"},
        {"name": "MemTest86 USB (free)",                   "url": "https://www.memtest86.com/downloads/memtest86-usb.zip",                                                                                       "size": "30MB"},
        {"name": "Finnix 125 (recovery live)",             "url": "https://www.finnix.org/releases/125/finnix-125.iso",                                                                                         "size": "500MB"},
        {"name": "DBAN 2.3.0 (disk nuke)",                 "url": "https://sourceforge.net/projects/dban/files/dban/2.3.0/dban-2.3.0_i586.iso/download",                                                       "size": "16MB"},
    ],

    # Android x86
    "android-x86": [
        {"name": "Android-x86 9.0-r2 (Pie)",               "url": "https://sourceforge.net/projects/android-x86/files/Release%209.0/android-x86_64-9.0-r2.iso/download",                                       "size": "1.0GB"},
        {"name": "BlissOS 16.9.9 x86_64 Official",         "url": "https://sourceforge.net/projects/blissos-x86/files/Official/BlissOS16/Generic/BlissOS-16.9.9-x86_64-OFFICIAL.iso/download",                 "size": "2.4GB"},
        {"name": "PrimeOS 2.1.0 (64-bit)",                 "url": "https://sourceforge.net/projects/primeos/files/64-bit/PrimeOS_2.1.0_64.iso/download",                                                        "size": "1.6GB"},
        {"name": "Phoenix OS 3.6.1 x64",                   "url": "https://sourceforge.net/projects/phoenix-os/files/Phoenix_OS_v3.6.1_x64.iso/download",                                                       "size": "2.0GB"},
    ],

    # ChromeOS
    "chromeos": [
        {"name": "ChromeOS Flex 14316.1.0 (stable)",       "url": "https://dl.google.com/chromeos-flex/channels/stable/chromeos_flex_14316.1.0_reven_recovery_stable-channel_mp-v2.bin.zip",                   "size": "1.8GB"},
        {"name": "FydeOS 17.1 x86_64 (ChromiumOS fork)",   "url": "https://sourceforge.net/projects/fydeos/files/FydeOS-for-PC_amd64-v17.1.iso/download",                                                      "size": "2.0GB"},
    ],

    # Alternative BSD
    "alternative/bsd": [
        {"name": "FreeBSD 14.2 DVD",                       "url": "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-amd64-dvd1.iso",                                     "size": "4.8GB"},
        {"name": "FreeBSD 14.2 Disc1",                     "url": "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-amd64-disc1.iso",                                    "size": "1.0GB"},
        {"name": "FreeBSD 14.2 Memstick",                  "url": "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-amd64-memstick.img",                                 "size": "1.1GB"},
        {"name": "FreeBSD 13.4 DVD (older stable)",        "url": "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/13.4/FreeBSD-13.4-RELEASE-amd64-dvd1.iso",                                     "size": "4.5GB"},
        {"name": "OpenBSD 7.6 amd64",                      "url": "https://cdn.openbsd.org/pub/OpenBSD/7.6/amd64/install76.iso",                                                                                "size": "650MB"},
        {"name": "NetBSD 10.1 amd64",                      "url": "https://ftp.netbsd.org/pub/NetBSD/NetBSD-10.1/images/NetBSD-10.1-amd64.iso",                                                                "size": "560MB"},
        {"name": "DragonFlyBSD 6.4.0",                     "url": "https://mirror.dragonflybsd.org/iso-images/dfly-x86_64-6.4.0_REL.iso",                                                                      "size": "1.8GB"},
        {"name": "Haiku r1beta5 x86_64",                   "url": "https://mirror.accum.se/mirror/haiku-os.org/haiku/r1beta5/haiku-r1beta5-x86_64-anyboot.iso",                                                 "size": "1.1GB"},
        {"name": "GhostBSD 24.10.1",                       "url": "https://ghostbsd.org/releases/amd64/24.10.1/GhostBSD-24.10.1.iso",                                                                          "size": "3.1GB"},
        {"name": "NomadBSD 20231013 i386",                 "url": "https://nomadbsd.org/download/nomadbsd-20231013.i386.img",                                                                                   "size": "2.7GB"},
        {"name": "NomadBSD 20231013 amd64",                "url": "https://nomadbsd.org/download/nomadbsd-20231013.amd64.img",                                                                                  "size": "2.8GB"},
        {"name": "helloSystem 0.8.2 (macOS-like BSD)",     "url": "https://github.com/helloSystem/ISO/releases/download/r0.8.2/hello-0.8.2_0.8.2-BSD.iso",                                                     "size": "2.5GB"},
        {"name": "MidnightBSD 3.2.0",                      "url": "https://www.midnightbsd.org/ftp/pub/MidnightBSD/MidnightBSD-3.2.0-RELEASE-amd64-disc1.iso",                                                 "size": "1.4GB"},
        {"name": "ReactOS 0.4.15 (Windows NT clone)",      "url": "https://iso.reactos.org/bootcd/reactos-0.4.15-release.iso",                                                                                  "size": "270MB"},
        {"name": "TrueNAS CORE 13.0-U6.2 (FreeBSD-based)", "url": "https://download.truenas.com/TrueNAS-CORE-13.0-U6.2/TrueNAS-CORE-13.0-U6.2.iso",                                                            "size": "1.2GB"},
    ],

    # Windows Evaluation
    "windows/eval": [
        {"name": "Windows 11 23H2 Enterprise Eval x64",    "url": "https://software-static.download.prss.microsoft.com/dbazure/8889691b-d735-4ef2-ad94-d2d0fdb44f01/22631.2428.231001-0608.23H2_NI_RELEASE_SVC_REFRESH_CLIENTENTERPRISE_VOL_X64FRE_EN-US.ISO", "size": "5.4GB"},
        {"name": "Windows 10 22H2 Enterprise Eval x64",    "url": "https://software-static.download.prss.microsoft.com/sg/download/details/44ddef8e-0c69-466c-adcc-37d80650945b/19045.2006.220908-0225.22H2_RELEASE_SVC_REFRESH_CLIENTENTERPRISE_VOL_X64FRE_EN-US.ISO", "size": "5.8GB"},
        {"name": "Windows Server 2022 Eval x64",           "url": "https://software-static.download.prss.microsoft.com/sg/download/details/20348.169.210806-2348.fe_release_svc_refresh_SERVER_EVAL_x64FRE_en-us.iso",                                          "size": "5.0GB"},
        {"name": "Windows Server 2019 Eval x64",           "url": "https://software-download.microsoft.com/download/pr/17763.253.190108-0006.rs5_release_svc_refresh_SERVER_EVAL_x64FRE_en-us.iso",                                                             "size": "4.7GB"},
    ],

    # Specialized: Containers / Cloud-Native
    "specialized/containers": [
        {"name": "RancherOS 1.5.8 (Docker-first, archived)", "url": "https://github.com/rancher/os/releases/download/v1.5.8/rancheros.iso",                                                                     "size": "170MB"},
        {"name": "k3OS 0.22.2 (k3s+OS, archived)",         "url": "https://github.com/rancher/k3os/releases/download/v0.22.2-k3s1r1/k3os-amd64.iso",                                                          "size": "310MB"},
        {"name": "Talos Linux v1.8.4 (Kubernetes OS)",      "url": "https://github.com/siderolabs/talos/releases/download/v1.8.4/talos-amd64.iso",                                                             "size": "110MB"},
        {"name": "Flatcar Container Linux (stable)",        "url": "https://stable.release.flatcar-linux.net/amd64-usr/current/flatcar_production_iso_image.iso",                                               "size": "500MB"},
        {"name": "Fedora CoreOS (stable, latest)",         "url": "https://builds.coreos.fedoraproject.org/prod/streams/stable/builds/latest/x86_64/fedora-coreos-latest-live.x86_64.iso",                     "size": "860MB"},
        {"name": "Harvester HCI v1.4.0 (Kubernetes HCI)",  "url": "https://releases.rancher.com/harvester/v1.4.0/harvester-v1.4.0-amd64.iso",                                                                   "size": "4.6GB"},
        {"name": "Garden Linux 1592.0 (SAP, OCI-ready)",   "url": "https://github.com/gardenlinux/gardenlinux/releases/download/1592.0/metal-amd64.iso",                                                        "size": "600MB"},
        {"name": "Bottlerocket OS 1.20 (AWS container)",   "url": "https://dl.fedoraproject.org/pub/alt/rawhide/Images/x86_64/Fedora-Cloud-Base-Generic-Rawhide.latest.x86_64.qcow2",                           "size": "400MB"},
    ],

    # Specialized: Vintage / Novelty
    "specialized/vintage": [
        {"name": "FreeDOS 1.3 LiveCD",                     "url": "https://www.freedos.org/download/download/FD13-LiveCD.iso",                                                                                  "size": "20MB"},
        {"name": "KolibriOS (tiny ASM OS)",                "url": "https://kolibrios.org/download/kolibrios.iso",                                                                                               "size": "8MB"},
        {"name": "MenuetOS 1.52 M64-136 (x86-64 ASM)",    "url": "https://menuetos.net/downloads/M64-136.zip",                                                                                                  "size": "5MB"},
        {"name": "TempleOS 5.03 Lite (archived)",          "url": "https://templeos.org/Downloads/TempleOSLite.ISO",                                                                                            "size": "25MB"},
        {"name": "Damn Small Linux 2024 (50MB)",           "url": "https://www.damnsmalllinux.org/2024/download/dsl-2024.06.01-x86_64.iso",                                                                    "size": "50MB"},
        {"name": "Tinycore Plus 16.0 (GUI included)",      "url": "http://tinycorelinux.net/16.x/x86_64/release/TinyCorePure64-current.iso",                                                                   "size": "157MB"},
        {"name": "Elive 3.8.40 (Enlightenment live)",      "url": "https://www.elivecd.org/download/stable/elive_3.8.40.iso",                                                                                  "size": "1.4GB"},
    ],

    # Wayland / Tiling WM
    "linux/wayland-tiling": [
        {"name": "Fedora 43 Sway Spin (Wayland tiling)",   "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-Sway-Live-x86_64-43-1.1.iso",                             "size": "1.8GB"},
        {"name": "Fedora 43 i3 Spin",                      "url": "https://dl.fedoraproject.org/pub/fedora/linux/releases/43/Spins/x86_64/iso/Fedora-i3-Live-x86_64-43-1.1.iso",                               "size": "1.7GB"},
        {"name": "ArcoLinux Plasma 25.01 (Arch+KDE)",      "url": "https://sourceforge.net/projects/arcolinux/files/ArcoLinux/ArcoLinux-plasma-25.01-x86_64.iso/download",                                     "size": "3.2GB"},
        {"name": "ArcoLinux XFCE 25.01",                   "url": "https://sourceforge.net/projects/arcolinux/files/ArcoLinux/ArcoLinux-xfce-25.01-x86_64.iso/download",                                       "size": "2.8GB"},
        {"name": "Regolith Linux 3.2 (Ubuntu+i3)",         "url": "https://github.com/regolith-linux/regolith-ubuntu-iso/releases/latest/download/regolith-ubuntu-3.2-amd64.iso",                             "size": "2.5GB"},
        {"name": "BlendOS 2024 (Arch immutable)",          "url": "https://github.com/blend-os/blendos/releases/latest/download/blendos-2024.iso",                                                             "size": "2.1GB"},
        {"name": "CutefishOS 0.8 (macOS-inspired)",        "url": "https://sourceforge.net/projects/cutefishos/files/0.8/cutefish-os-0.8-amd64.iso/download",                                                  "size": "2.4GB"},
    ],

    # RISC / Emulation Targets
    "specialized/risc-emulation": [
        {"name": "RISC OS 5.28 (Raspberry Pi, x86 VM)",    "url": "https://www.riscosopen.org/content/downloads/common/RISC_OS528.zip",                                                                         "size": "300MB"},
        {"name": "Plan 9 from Bell Labs (4th Edition)",     "url": "https://9p.io/plan9/download/plan9.iso.bz2",                                                                                                "size": "300MB"},
        {"name": "seL4 microkernel demo image",             "url": "https://sel4.systems/downloads/seL4-test-latest.tar.gz",                                                                                    "size": "20MB"},
        {"name": "Redox OS 0.8 (Rust OS, x86_64)",         "url": "https://static.redox-os.org/img/x86_64/redox_desktop_x86_64_2024-12-24_751_harddrive.img.zst",                                             "size": "300MB"},
        {"name": "HelenOS 0.12 (microkernel research OS)", "url": "https://helenos.org/downloads/helenos-0.12.1-amd64.iso",                                                                                     "size": "50MB"},
        {"name": "Genode OS Framework (sculpt 24.04)",      "url": "https://depot.genode.org/genodelabs/sculpt/24.04/sculpt-24-04.img",                                                                         "size": "180MB"},
    ],

    # ARM / Raspberry Pi
    "arm/raspberry-pi": [
        {"name": "Raspberry Pi OS Full (Bookworm, armhf)",  "url": "https://downloads.raspberrypi.com/raspios_full_armhf/images/raspios_full_armhf-latest/2024-11-19-raspios-bookworm-armhf-full.img.xz",       "size": "2.8GB"},
        {"name": "Ubuntu 24.04 Server for RPi (arm64)",    "url": "https://cdimage.ubuntu.com/ubuntu-server/noble/daily-preinstalled/current/noble-preinstalled-server-arm64+raspi.img.xz",                    "size": "1.5GB"},
        {"name": "Kali Linux 2025.1 for RPi4 (arm64)",     "url": "https://cdimage.kali.org/kali-2025.1/kali-linux-2025.1-raspberry-pi-arm64.img.xz",                                                          "size": "3.1GB"},
        {"name": "RetroPie 4.8 for RPi4/400",              "url": "https://github.com/RetroPie/RetroPie-Setup/releases/download/4.8/retropie-buster-4.8-rpi4_400.img.gz",                                      "size": "1.3GB"},
        {"name": "DietPi NativePC x86_64 (Bookworm)",      "url": "https://dietpi.com/downloads/images/DietPi_NativePC-BIOS_x86_64-Bookworm.img.xz",                                                           "size": "500MB"},
        {"name": "Armbian 24.11 for RPi4 (Bookworm)",      "url": "https://dl.armbian.com/rpi4b/archive/Armbian_24.11.4_Rpi4b_bookworm_current_6.6.70.img.xz",                                                 "size": "900MB"},
        {"name": "LibreELEC 12.0 (RPi4, Kodi)",           "url": "https://releases.libreelec.tv/LibreELEC-RPi4.aarch64-12.0.2.img.gz",                                                                        "size": "450MB"},
        {"name": "OSMC 2024.06-1 (RPi, Kodi)",            "url": "https://ftp.fau.de/osmc/osmc/download/installers/diskimages/OSMC_TGT_rbp4_20240606.img.gz",                                                  "size": "400MB"},
        {"name": "Volumio 3.x (RPi, audio OS)",            "url": "https://updates.volumio.org/pi/volumio/3.512/volumio-3.512-2024-03-13-pi.img.zip",                                                           "size": "900MB"},
    ],

}
