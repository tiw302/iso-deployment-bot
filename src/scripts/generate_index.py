# automated gdrive library generator

import os
import sys
import datetime
import subprocess
import re
import json
import time

# import inventory database from parent dir
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))
try:
    from distros import DB
except ImportError:
    DB = {}
from utils import resolve_filename

GDRIVE_LIBRARY_URL = "https://drive.google.com/drive/folders/1B64Y44QVMlgoVm49PRk2_UvPXRzXNZ8e?usp=sharing"

ASCII_ART = r"""
#  ██████  ███████        ██      ██ ███████  ██████    ██████   ███████ ██    ██  /\_/\
# ██    ██ ██             ██      ██ ██    ██ ██   ██  ██    ██  ██   ██  ██  ██  ( o.o )
# ██    ██ ███████  █████ ██      ██ ███████  ██████   ████████  ██████    ████    > ^ <
# ██    ██       ██       ██      ██ ██    ██ ██   ██  ██    ██  ██   ██    ██    /     \
#  ██████  ███████        ███████ ██ ███████  ██    ██ ██    ██  ██    ██   ██   (___/___)
"""

COPY_ICON = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>'

def clean_filename(filename):
    name = os.path.splitext(filename)[0]
    if name.endswith('.img'): name = name[:-4]
    name = name.replace('-', ' ').replace('_', ' ').replace('.', ' ')
    name = re.sub(r'\b(amd64|x86_64|64bit|dvd|iso)\b', '', name, flags=re.IGNORECASE)
    name = ' '.join(name.split()).title()
    return name

def format_size(size_bytes):
    try:
        size = float(size_bytes)
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
    except:
        return "?.? GB"
    return "?.? GB"

def get_drive_content():
    library = {}
    total_bytes = 0
    try:
        remote_res = subprocess.run(["rclone", "listremotes"], capture_output=True, text=True)
        remotes = [r.strip().rstrip(':') for r in remote_res.stdout.strip().split('\n') if r.strip()]
        remote_name = remotes[0] if remotes else "gdrive"
        res = subprocess.run(
            ["rclone", "lsf", f"{remote_name}:os-deployment-library", "-R", "--format", "pis", "--files-only"],
            capture_output=True, text=True, timeout=120
        )
        if res.returncode == 0:
            for line in res.stdout.strip().split('\n'):
                if ';' not in line: continue
                parts = line.split(';')
                if len(parts) < 3: continue
                path, file_id, size = parts[0], parts[1], parts[2]
                if not any(path.lower().endswith(ext) for ext in ['.iso', '.img', '.gz', '.xz', '.zip', '.bin', '.bz2', '.7z']):
                    continue
                try:
                    bytes_val = int(size)
                    total_bytes += bytes_val
                except ValueError:
                    bytes_val = 0
                category = os.path.dirname(path)
                if not category: category = "unsorted"
                filename = os.path.basename(path)
                pretty_name = clean_filename(filename)
                db_item = None
                for cat_items in DB.values():
                    for item in cat_items:
                        if resolve_filename(item.get('url', '')) == filename:
                            pretty_name = item.get('name')
                            db_item = item
                            break
                if category not in library:
                    library[category] = []
                library_item = {
                    "name": pretty_name,
                    "filename": filename,
                    "size": format_size(size),
                    "bytes": bytes_val,
                    "id": file_id
                }
                if db_item:
                    library_item["db_item"] = db_item
                library[category].append(library_item)
    except Exception as e:
        print(f"error scanning drive: {e}")
    return library, total_bytes


OS_DESCRIPTIONS = [
    ('ubuntu', 'A popular, easy-to-use Linux distribution with a large community, suitable for both Desktop and Server.'),
    ('debian', 'A highly stable and secure Linux distribution, serving as the upstream for Ubuntu.'),
    ('alpine', 'A security-oriented, lightweight Linux distribution. Widely used for Docker containers.'),
    ('proxmox', 'An enterprise-grade open-source virtualization management platform (Hypervisor).'),
    ('vyos', 'An open-source network operating system used for enterprise routers, firewalls, and VPNs.'),
    ('kali', 'A Linux distribution designed for digital forensics, hacking, and penetration testing.'),
    ('fedora', 'A cutting-edge Linux distribution sponsored by Red Hat.'),
    ('arch', 'A flexible, rolling-release Linux distribution for advanced users who want full control.'),
    ('garuda', 'An Arch-based Linux distribution optimized for gaming with a highly customized UI.'),
    ('windows', "Microsoft's proprietary operating system for general use and servers."),
    ('centos', 'An enterprise-class Linux distribution known for its extreme stability.'),
    ('netbsd', 'A highly portable UNIX-like operating system that runs on almost any hardware architecture.'),
    ('pfsense', 'An open-source firewall and router software distribution based on FreeBSD.'),
    ('opnsense', 'An open-source, easy-to-use FreeBSD-based firewall and routing platform.'),
    ('openmediavault', 'A Network Attached Storage (NAS) solution based on Debian Linux.'),
    ('rockstor', 'A NAS and Private Cloud storage solution based on Linux and BTRFS.'),
    ('clonezilla', 'A powerful partition and disk imaging/cloning program.'),
    ('puppylinux', 'An extremely lightweight Linux distribution that can run entirely in RAM.'),
    ('qubes', 'A security-oriented OS that uses Xen virtualization to isolate applications into separate VMs.')
]

def get_lib_description(name):
    name_lower = name.lower()
    for keyword, desc in OS_DESCRIPTIONS:
        if keyword in name_lower:
            return desc
    return 'A bootable operating system or software image ready for deployment.'

OS_DETAILS = {
    'ubuntu': {
        'developer': 'Canonical Ltd. / Ubuntu Community',
        'type': 'Linux (Debian-based)',
        'default_user': 'ubuntu (or installer setup)',
        'docs': 'https://help.ubuntu.com',
        'notes': 'Highly recommended for both virtualization templates and cloud-init deployments.'
    },
    'debian': {
        'developer': 'The Debian Project',
        'type': 'Linux (Independent/Upstream)',
        'default_user': 'root / user (defined during setup)',
        'docs': 'https://www.debian.org/doc/',
        'notes': 'The bedrock of stability. Excellent choice for production servers and Proxmox LXC containers.'
    },
    'alpine': {
        'developer': 'Alpine Linux Development Team',
        'type': 'Linux (Lightweight/musl/busybox)',
        'default_user': 'root (no password by default)',
        'docs': 'https://wiki.alpinelinux.org',
        'notes': 'Extremely compact security-oriented distro. Ideal for Docker base images and minimal VM instances.'
    },
    'proxmox': {
        'developer': 'Proxmox Server Solutions GmbH',
        'type': 'Hypervisor OS (Debian-based)',
        'default_user': 'root (password defined during setup)',
        'docs': 'https://pve.proxmox.com/pve-docs/',
        'notes': 'Enterprise-grade virtualization manager. Use to build clusters and manage LXC/KVM hypervisors.'
    },
    'vyos': {
        'developer': 'VyOS Project / Sentrium',
        'type': 'Router OS (Debian-based)',
        'default_user': 'vyos / vyos',
        'docs': 'https://docs.vyos.io',
        'notes': 'Software-defined network routing and firewall platform. Managed completely via command-line interface.'
    },
    'kali': {
        'developer': 'Offensive Security',
        'type': 'Linux (Debian-based, Security)',
        'default_user': 'kali / kali',
        'docs': 'https://www.kali.org/docs/',
        'notes': 'Pre-loaded with hundreds of penetration testing and forensic tools. Use with responsibility.'
    },
    'fedora': {
        'developer': 'Red Hat / Fedora Project',
        'type': 'Linux (Red Hat family)',
        'default_user': 'fedora (or setup defined)',
        'docs': 'https://docs.fedoraproject.org',
        'notes': 'Upstream source for Red Hat Enterprise Linux. Showcases the latest Linux technologies and features.'
    },
    'arch': {
        'developer': 'Arch Linux Team',
        'type': 'Linux (Independent, Rolling)',
        'default_user': 'root (no password on live media)',
        'docs': 'https://wiki.archlinux.org',
        'notes': 'Features a rolling release cycle. Relies on user-centric configuration and Pacman package manager.'
    },
    'garuda': {
        'developer': 'Garuda Linux Team',
        'type': 'Linux (Arch-based)',
        'default_user': 'garuda / garuda',
        'docs': 'https://wiki.garudalinux.org',
        'notes': 'Optimized for gaming and desktop performance. Includes BTRFS filesystem integration by default.'
    },
    'windows': {
        'developer': 'Microsoft Corporation',
        'type': 'Proprietary OS',
        'default_user': 'Administrator / Administrator (defined during setup)',
        'docs': 'https://learn.microsoft.com/en-us/windows/',
        'notes': 'Used for Active Directory, IIS hosting, and enterprise application testing.'
    },
    'centos': {
        'developer': 'Red Hat / CentOS Project',
        'type': 'Linux (Red Hat family)',
        'default_user': 'root (defined during setup)',
        'docs': 'https://www.centos.org/docs/',
        'notes': 'CentOS Stream serves as the rolling development branch of Red Hat Enterprise Linux (RHEL).'
    },
    'pfsense': {
        'developer': 'Rubicon Communications, LLC (Netgate)',
        'type': 'Firewall/Router OS (FreeBSD-based)',
        'default_user': 'admin / pfsense',
        'docs': 'https://docs.netgate.com/pfsense/',
        'notes': 'Open-source stateful packet filtering firewall, routing, and VPN platform.'
    },
    'opnsense': {
        'developer': 'Deciso B.V.',
        'type': 'Firewall/Router OS (FreeBSD-based)',
        'default_user': 'root / opnsense',
        'docs': 'https://docs.opnsense.org',
        'notes': 'Modern fork of pfSense. Features a clean, bootstrap-based web GUI and robust routing engine.'
    },
    'openmediavault': {
        'developer': 'Volker Theile / OMV Community',
        'type': 'NAS OS (Debian-based)',
        'default_user': 'admin / openmediavault (WebGUI), root (defined in CLI setup)',
        'docs': 'https://docs.openmediavault.org',
        'notes': 'Network attached storage solution. Features software RAID, SMB/CIFS, SSH, FTP, and Docker/Portainer support.'
    },
    'rockstor': {
        'developer': 'RockStor Inc.',
        'type': 'NAS/Private Cloud OS (openSUSE-based)',
        'default_user': 'admin (WebGUI setup), root (defined in CLI)',
        'docs': 'https://rockstor.com/docs/',
        'notes': 'BTRFS-powered private cloud and NAS storage manager. Uses docker containers called "Rock-ons".'
    },
    'clonezilla': {
        'developer': 'Steven Shiau / NCHC',
        'type': 'Live Backup Utility (Debian-based)',
        'default_user': 'user / live (automatic login)',
        'docs': 'https://clonezilla.org/fine-print-index.php',
        'notes': 'Partition and disk imaging tool. Supports bare-metal backup and restoration over multicast network.'
    },
    'puppylinux': {
        'developer': 'Puppy Linux Community',
        'type': 'Linux (Lightweight)',
        'default_user': 'root (automatic)',
        'docs': 'https://wikka.puppylinux.com',
        'notes': 'Loads completely into RAM. Extremely fast and lightweight, running smoothly on legacy hardware.'
    },
    'qubes': {
        'developer': 'The Qubes OS Project',
        'type': 'Security-oriented Hypervisor (Xen-based)',
        'default_user': 'user (defined during setup)',
        'docs': 'https://www.qubes-os.org/doc/',
        'notes': 'Implements security-by-isolation. Isolates networking, USB controllers, and apps into distinct VMs.'
    }
}

def get_lib_details(name, desc, db_item=None):
    name_lower = name.lower()
    details = {
        'name': name,
        'developer': 'Community / Open Source',
        'type': 'Operating System Image',
        'default_user': 'Configured during installation',
        'docs': 'https://www.google.com',
        'notes': 'Standard bootable media for physical or virtual machines.',
        'description': desc
    }
    for keyword, specs in OS_DETAILS.items():
        if keyword in name_lower:
            details.update(specs)
            break

    if db_item:
        for key in ['developer', 'type', 'default_user', 'docs', 'notes', 'description', 'sha256', 'tags', 'filename']:
            if key in db_item:
                details[key] = db_item[key]

    return json.dumps(details).replace('"', '&quot;')

def load_massive_distros():
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    path = os.path.join(root_dir, "tools", "massive_distros_categorized.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def infer_tags(name, category, filename="", description=""):
    tags = set()
    name_lower = name.lower()
    cat_lower = category.lower()
    file_lower = filename.lower()
    desc_lower = description.lower()

    # combine all text fields to check for keywords
    text = f"{name_lower} {cat_lower} {file_lower} {desc_lower}"

    # 1. check os family and upstream base
    if "ubuntu" in text:
        tags.add("ubuntu")
        tags.add("debian")
    if "debian" in text:
        tags.add("debian")
    if "fedora" in text:
        tags.add("fedora")
        tags.add("redhat")
    if "arch" in text:
        tags.add("arch")
    if "suse" in text or "tumbleweed" in text or "leap" in text:
        tags.add("opensuse")
    if "alpine" in text:
        tags.add("alpine")
        tags.add("minimal")
    if "windows" in text:
        tags.add("windows")
    if "kali" in text:
        tags.add("kali")
        tags.add("debian")
        tags.add("security")
    if "proxmox" in text or "pve" in text:
        tags.add("proxmox")
        tags.add("hypervisor")
        tags.add("debian")
    if "vyos" in text:
        tags.add("vyos")
        tags.add("router")
        tags.add("debian")
    if "gentoo" in text:
        tags.add("gentoo")
    if "slackware" in text:
        tags.add("slackware")
    if "mint" in text:
        tags.add("mint")
        tags.add("ubuntu")
        tags.add("debian")
    if "pop os" in text or "pop-os" in text or "pop_os" in text or "popos" in text:
        tags.add("pop-os")
        tags.add("ubuntu")
        tags.add("debian")
    if "neon" in text:
        tags.add("neon")
        tags.add("kde")
        tags.add("ubuntu")
        tags.add("debian")
    if "mx" in text or "antix" in text:
        tags.add("mx-linux")
        tags.add("debian")
    if "sparky" in text:
        tags.add("sparky")
        tags.add("debian")
    if "feren" in text:
        tags.add("feren")
        tags.add("ubuntu")
        tags.add("debian")
    if "nitrux" in text:
        tags.add("nitrux")
        tags.add("debian")
    if "garuda" in text:
        tags.add("garuda")
        tags.add("arch")
    if "cachy" in text:
        tags.add("cachyos")
        tags.add("arch")
    if "manjaro" in text:
        tags.add("manjaro")
        tags.add("arch")
    if "centos" in text:
        tags.add("centos")
        tags.add("redhat")
    if "oracle" in text:
        tags.add("oracle-linux")
        tags.add("redhat")
    if "rocky" in text:
        tags.add("rocky-linux")
        tags.add("redhat")
    if "alma" in text:
        tags.add("almalinux")
        tags.add("redhat")
    if "red hat" in text or "rhel" in text:
        tags.add("rhel")
        tags.add("redhat")
    if "nixos" in text:
        tags.add("nixos")
        tags.add("immutable")
    if "flatcar" in text:
        tags.add("flatcar")
        tags.add("container")
    if "rancher" in text:
        tags.add("rancher")
        tags.add("container")
    if "pfsense" in text:
        tags.add("pfsense")
        tags.add("router")
        tags.add("bsd")
    if "opnsense" in text:
        tags.add("opnsense")
        tags.add("router")
        tags.add("bsd")
    if "openmediavault" in text or "omv" in text:
        tags.add("openmediavault")
        tags.add("nas")
        tags.add("debian")
    if "rockstor" in text:
        tags.add("rockstor")
        tags.add("nas")
    if "clonezilla" in text:
        tags.add("clonezilla")
        tags.add("recovery")
    if "hiren" in text:
        tags.add("hirens-boot")
        tags.add("recovery")
        tags.add("windows")
    if "ubcd" in text or "ultimate boot" in text:
        tags.add("ubcd")
        tags.add("recovery")
    if "puppy" in text:
        tags.add("puppy-linux")
        tags.add("minimal")
    if "porteus" in text:
        tags.add("porteus")
        tags.add("minimal")
    if "slax" in text:
        tags.add("slax")
        tags.add("minimal")
    if "tinycore" in text:
        tags.add("tinycore")
        tags.add("minimal")
        tags.add("vintage")
    if "kolibri" in text:
        tags.add("kolibrios")
        tags.add("vintage")
    if "bliss" in text:
        tags.add("blissos")
        tags.add("android")
    if "primeos" in text:
        tags.add("primeos")
        tags.add("android")
    if "android" in text:
        tags.add("android")
    if "freebsd" in text:
        tags.add("freebsd")
        tags.add("bsd")
    if "openbsd" in text:
        tags.add("openbsd")
        tags.add("bsd")
    if "netbsd" in text:
        tags.add("netbsd")
        tags.add("bsd")
    if "bsd" in text:
        tags.add("bsd")
    if "backbox" in text:
        tags.add("backbox")
        tags.add("security")
        tags.add("ubuntu")
        tags.add("debian")
    if "deft" in text:
        tags.add("deft")
        tags.add("security")
    if "qubes" in text:
        tags.add("qubes")
        tags.add("security")
        tags.add("hypervisor")
    if "harvester" in text:
        tags.add("harvester")
        tags.add("hypervisor")
    if "finnix" in text:
        tags.add("finnix")
        tags.add("recovery")
    if "grml" in text:
        tags.add("grml")
        tags.add("recovery")
    if "netboot" in text:
        tags.add("netboot")
    if "asahi" in text:
        tags.add("asahi")
        tags.add("arch")
        tags.add("arm")
    if "tuxedo" in text:
        tags.add("tuxedo-os")
        tags.add("ubuntu")
        tags.add("debian")

    # 2. check desktop environment or window manager
    if "kde" in text or "plasma" in text or "kubuntu" in text or "neon" in text:
        tags.add("kde")
    if "gnome" in text:
        tags.add("gnome")
    if "xfce" in text or "xubuntu" in text:
        tags.add("xfce")
    if "cinnamon" in text:
        tags.add("cinnamon")
    if "lubuntu" in text or "lxde" in text or "lxqt" in text:
        tags.add("lxqt")
    if "mate" in text:
        tags.add("mate")
    if "sway" in text:
        tags.add("sway")
    if "i3" in text:
        tags.add("i3")
    if "fluxbox" in text:
        tags.add("fluxbox")
    if "budgie" in text:
        tags.add("budgie")
    if "cutefish" in text:
        tags.add("cutefish")
    if "deepin" in text or "dde" in text:
        tags.add("deepin")

    # 3. check cpu architecture
    if "arm64" in text or "aarch64" in text or "arm" in text:
        tags.add("arm64")
    elif "amd64" in text or "x86_64" in text or "x64" in text or "64bit" in text:
        tags.add("x86_64")

    # 4. check environment or role
    if "server" in text:
        tags.add("server")
    if "desktop" in text or "workstation" in text or "live" in text:
        tags.add("desktop")
    if "live" in text:
        tags.add("live")
    if "netinst" in text or "netinstall" in text:
        tags.add("netinst")
    if "lts" in text:
        tags.add("lts")
    if "nvidia" in text:
        tags.add("nvidia")

    # 5. check category specific labels
    if "minimal" in text or "lightweight" in text:
        tags.add("minimal")
    if "virtualization" in text or "hypervisor" in text or "virt" in text:
        tags.add("hypervisor")
    if "nas" in text or "storage" in text:
        tags.add("nas")
    if "security" in text or "pentesting" in text or "forensic" in text or "privacy" in text:
        tags.add("security")
    if "recovery" in text or "backup" in text:
        tags.add("recovery")
    if "gaming" in text:
        tags.add("gaming")
    if "immutable" in text or "atomic" in text:
        tags.add("immutable")
    if "containers" in text or "container" in text:
        tags.add("container")
    if "raspberry-pi" in text or "rpi" in text or "raspi" in text:
        tags.add("rpi")
        tags.add("arm64")
    if "vintage" in text or "legacy" in text:
        tags.add("legacy")
    if "multimedia" in text or "studio" in text:
        tags.add("multimedia")
        tags.add("desktop")
    if "office" in text:
        tags.add("desktop")
    if "eval" in text:
        tags.add("evaluation")

    return sorted(list(tags))

def generate_html():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(os.path.dirname(script_dir))
    output_path = os.path.join(root_dir, "web", "index.html")
    library, total_bytes = get_drive_content()
    massive_dict = load_massive_distros()
    total_isos = sum(len(v) for v in library.values())
    massive_total = sum(len(v) for v in massive_dict.values())
    last_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # generate storage visualizer chart
    chart_lines = []
    if total_bytes > 0:
        cat_sizes = {}
        for cat, items in library.items():
            cat_sizes[cat] = sum(item.get("bytes", 0) for item in items)

        # Sort by size descending
        sorted_cats = sorted(cat_sizes.items(), key=lambda x: x[1], reverse=True)

        for cat, size in sorted_cats:
            percentage = (size / total_bytes) * 100
            bar_width = 30
            filled_chars = int(round((percentage / 100) * bar_width))
            bar = "█" * filled_chars + "░" * (bar_width - filled_chars)
            cat_display = cat.replace('/', ' > ').lower()
            chart_lines.append(f"  {cat_display:<26} [{bar}] {format_size(size):>8} ({percentage:.1f}%)")
    else:
        chart_lines.append("  no mirrored files found in storage.")
    storage_chart = "\n".join(chart_lines)

    template_path = os.path.join(root_dir, "src", "templates", "index_template.html")
    with open(template_path, "r") as f:
        html_template = f.read()

    # generate library section
    lib_sections = ""
    lib_nav = f'<button onclick="filterContent(\'lib\', \'all\')" class="filter-pill lib-pill active" data-target="all">all_files ({total_isos})</button>'
    # predefined logical category order
    lib_cat_order = [
        "linux/ubuntu", "linux/ubuntu-noble", "linux/ubuntu-plucky", "linux/ubuntu-jammy",
        "linux/debian", "linux/debian-based", "linux/mint", "linux/pop-os", "linux/zorin",
        "linux/arch-family",
        "linux/enterprise", "linux/server", "linux/server-cloud", "linux/fedora-spins",
        "linux/gaming",
        "linux/security", "linux/pentesting", "linux/forensic", "linux/privacy",
        "linux/immutable", "linux/wayland-tiling", "linux/rolling",
        "linux/lightweight", "linux/minimal",
        "homelab", "homelab/virtualization", "homelab/firewall", "homelab/nas",
        "specialized/vintage", "specialized/containers", "specialized/risc-emulation",
        "recovery/tools", "recovery/backup",
        "arm/raspberry-pi", "arm/sbc",
        "windows/eval",
        "android-x86", "chromeos",
        "alternative/bsd",
        "linux/ai-ml", "linux/developer", "linux/desktop-env", "linux/embedded", "linux/specialized",
        "linux/office", "linux/hardware", "linux/live-tools", "linux/education", "linux/scientific",
        "linux/legacy", "linux/others", "linux/experimental", "linux/alternative-arch", "linux/cloud",
        "linux/multimedia"
    ]

    def lib_cat_sort_key(cat):
        cat_lower = cat.lower()
        for idx, ordered_cat in enumerate(lib_cat_order):
            if cat_lower == ordered_cat.lower() or cat_lower.startswith(ordered_cat.lower() + "/"):
                return idx
        return 1000 + len(cat)

    sorted_lib_cats = sorted(library.keys(), key=lib_cat_sort_key)
    for i, cat in enumerate(sorted_lib_cats):
        items = library[cat]
        cat_id = f"lib_cat_{i}"
        cat_display = cat.replace('/', ' > ').lower()
        lib_nav += f'<button onclick="filterContent(\'lib\', \'{cat_id}\')" class="filter-pill lib-pill" data-target="{cat_id}">{cat_display} ({len(items)})</button>'
        cards = ""
        for item in items:
            gdrive_url = f"https://drive.google.com/uc?export=download&id={item['id']}"
            db_item = item.get("db_item")
            if not db_item:
                db_item = {}
            else:
                db_item = db_item.copy()
            db_item["filename"] = item["filename"]

            desc = get_lib_description(item["name"])
            if "description" in db_item:
                desc = db_item["description"]

            # infer tags if not set in db
            if "tags" not in db_item:
                db_item["tags"] = infer_tags(item["name"], cat, item["filename"], desc)
            details_json = get_lib_details(item["name"], desc, db_item)

            tags_html = ""
            if "tags" in db_item and db_item["tags"]:
                tags_list = db_item["tags"]
                tags_html = '<div class="iso-tags">' + "".join([f'<span class="tag-badge tag-{t.lower()}">{t}</span>' for t in tags_list]) + '</div>'

            cards += f'<div class="iso-card secured" data-name="{item["name"].lower()}" data-details="{details_json}"><div class="iso-info"><div class="iso-name">{item["name"]} <span class="status-secured">✓</span></div><div class="iso-size">{item["size"]}</div>{tags_html}<div class="iso-desc">{desc}</div></div><div class="iso-actions"><button class="btn-copy" data-url="{gdrive_url}" title="Copy Link">{COPY_ICON}</button><a href="{gdrive_url}" target="_blank" class="btn-download btn-gdrive-dl">download</a></div></div>'
        lib_sections += f'<section class="category-section library-section" id="{cat_id}"><div class="category-title">{cat_display} ({len(items)})</div><div class="grid">{cards}</div></section>'

    # generate discovery section
    disc_sections = ""
    disc_nav = f'<button onclick="filterContent(\'disc\', \'all\')" class="filter-pill disc-pill active" data-target="all">all_distros ({massive_total})</button>'

    disc_cat_order = [
        "ubuntu family", "debian family", "arch family", "red hat / enterprise",
        "suse / opensuse", "gentoo / source", "slackware based",
        "server / cloud / nas", "security / recovery", "lightweight / minimal",
        "gaming / multimedia", "mobile / android", "independent / unique",
        "bsd / alternative"
    ]

    def disc_cat_sort_key(cat):
        cat_lower = cat.lower()
        if "others / niche" in cat_lower or "niche" in cat_lower:
            return 99999
        for idx, ordered_cat in enumerate(disc_cat_order):
            if ordered_cat in cat_lower:
                return idx
        return 1000 + len(cat)

    sorted_disc_cats = sorted(massive_dict.keys(), key=disc_cat_sort_key)
    for i, cat in enumerate(sorted_disc_cats):
        distros = massive_dict[cat]
        cat_id = f"disc_cat_{i}"
        disc_nav += f'<button onclick="filterContent(\'disc\', \'{cat_id}\')" class="filter-pill disc-pill" data-target="{cat_id}">{cat.lower()} ({len(distros)})</button>'
        disc_cards = ""
        for distro in distros:
            desc = distro.get("description", "Wikipedia encyclopedia entry for " + distro["name"])
            desc = desc.replace('"', '&quot;')
            # infer tags for discovery cards
            disc_tags = infer_tags(distro["name"], cat, "", desc)

            details_json = get_lib_details(distro["name"], desc)
            try:
                import json as pyjson
                details_dict = pyjson.loads(details_json.replace('&quot;', '"'))
                details_dict['docs'] = distro['url']
                details_dict['type'] = 'Linux (Discovery Archive)'
                details_dict['tags'] = disc_tags
                details_json = pyjson.dumps(details_dict).replace('"', '&quot;')
            except:
                pass

            tags_html = ""
            if disc_tags:
                tags_html = '<div class="iso-tags">' + "".join([f'<span class="tag-badge tag-{t.lower()}">{t}</span>' for t in disc_tags]) + '</div>'

            disc_cards += f'<div class="iso-card discovery-card" data-name="{distro["name"].lower()}" data-details="{details_json}"><div class="iso-info"><div class="iso-name">{distro["name"]}</div><div class="iso-size">encyclopedia</div>{tags_html}<div class="iso-desc">{desc}</div></div><div class="iso-actions"><button class="btn-copy" data-url="{distro["url"]}" title="Copy Link">{COPY_ICON}</button><a href="{distro["url"]}" target="_blank" class="btn-download btn-source-dl">wiki</a></div></div>'
        disc_sections += f'<section class="category-section discovery-section" id="{cat_id}"><div class="category-title">{cat.lower()} ({len(distros)})</div><div class="grid discovery-grid">{disc_cards}</div></section>'

    final_html = html_template.replace("ASCII_ART_PLACEHOLDER", ASCII_ART) \
                             .replace("{{total_isos}}", str(total_isos)) \
                             .replace("{{massive_count}}", str(massive_total)) \
                             .replace("{{total_size}}", format_size(total_bytes)) \
                             .replace("{{gdrive_url}}", GDRIVE_LIBRARY_URL) \
                             .replace("{{library_nav}}", lib_nav) \
                             .replace("{{library_sections}}", lib_sections) \
                             .replace("{{discovery_nav}}", disc_nav) \
                             .replace("{{discovery_sections}}", disc_sections) \
                             .replace("{{timestamp}}", str(int(time.time()))) \
                             .replace("{{storage_chart}}", storage_chart) \
                             .replace("{{last_updated}}", last_updated)

    with open(output_path, "w") as f:
        f.write(final_html)
    print(f"dashboard regenerated: {total_isos} library files ({format_size(total_bytes)}) + {massive_total} discovery entries.")

if __name__ == "__main__":
    generate_html()
