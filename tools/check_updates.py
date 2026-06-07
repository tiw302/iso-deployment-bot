# semi-automated version checker

import os
import sys
import re
import urllib.request
import json

# setup path to import distros from src
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(os.path.dirname(script_dir), "src"))
try:
    from distros import DB
except ImportError:
    print("error: could not import DB from src/distros.py")
    sys.exit(1)

def check_debian():
    # check latest release version of debian
    url = "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        match = re.search(r'debian-(\d+\.\d+\.\d+)-amd64-netinst\.iso', html)
        if match:
            return match.group(1)
    except Exception as e:
        print(f"error checking debian: {e}")
    return None

def check_ubuntu_releases(base_version):
    # check latest release version of ubuntu
    url = "https://releases.ubuntu.com/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(rf'href="({re.escape(base_version)}\.\d+)/"', html)
        if versions:
            return max(versions, key=lambda v: [int(x) for x in v.split('.')])
        if f'href="{base_version}/"' in html:
            return base_version
    except Exception as e:
        print(f"error checking ubuntu {base_version}: {e}")
    return None

def check_ubuntu_flavor(flavor):
    # check latest release version of an ubuntu flavor on cdimage
    url = f"https://cdimage.ubuntu.com/{flavor}/releases/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'href="(\d{2}\.\d{2}(?:\.\d+)?)/"', html)
        if versions:
            return max(versions, key=lambda v: [int(x) for x in v.split('.')])
    except Exception as e:
        print(f"error checking ubuntu flavor {flavor}: {e}")
    return None

def check_pop_os_version_helper(version_pref, start_build):
    # find the latest build number for pop!_os version
    latest_build = start_build
    gpu = "intel"
    while True:
        next_build = latest_build + 1
        url = f"https://iso.pop-os.org/{version_pref}/amd64/{gpu}/{next_build}/pop-os_{version_pref}_amd64_{gpu}_{next_build}.iso"
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req, timeout=5) as r:
                if r.status == 200:
                    latest_build = next_build
                else:
                    break
        except Exception:
            break
    return latest_build

def check_zorin():
    # check latest release version of zorin os
    url = "https://distro.ibiblio.org/zorinos/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        majors = re.findall(r'href="(\d+)/"', html)
        if majors:
            latest_major = max(majors, key=int)
            sub_url = f"https://distro.ibiblio.org/zorinos/{latest_major}/"
            req_sub = urllib.request.Request(sub_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req_sub, timeout=10) as r_sub:
                html_sub = r_sub.read().decode('utf-8')
            versions = re.findall(r'Zorin-OS-(\d+\.\d+(?:\.\d+)?)-Core-64-bit\.iso', html_sub)
            if versions:
                return latest_major, max(versions, key=lambda v: [int(x) for x in v.split('.')])
    except Exception as e:
        print(f"error checking zorin: {e}")
    return None

def check_arch():
    # check latest release version of arch linux
    url = "https://archlinux.org/releases/json/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode('utf-8'))
        if "releases" in data and len(data["releases"]) > 0:
            return data["releases"][0]["version"]
    except Exception as e:
        print(f"error checking arch linux: {e}")
    return None

def check_manjaro():
    # check latest release version of manjaro
    try:
        latest_ver = check_sourceforge_version("manjarolinux", "kde")
        if latest_ver:
            url = f"https://sourceforge.net/projects/manjarolinux/rss?path=/kde/{latest_ver}"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as r:
                xml = r.read().decode('utf-8')
            match = re.search(rf'/kde/{re.escape(latest_ver)}/(manjaro-kde-{re.escape(latest_ver)}-\d+-linux\d+)\.iso', xml)
            if match:
                return latest_ver, match.group(1)
    except Exception as e:
        print(f"error checking manjaro: {e}")
    return None

def check_fedora():
    # check latest release version of fedora
    url = "https://dl.fedoraproject.org/pub/fedora/linux/releases/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'href="(\d+)/"', html)
        if versions:
            return max(versions, key=int)
    except Exception as e:
        print(f"error checking fedora: {e}")
    return None

def get_fedora_iso_suffix(ver):
    # check suffix of fedora isos in the latest release directory
    url = f"https://dl.fedoraproject.org/pub/fedora/linux/releases/{ver}/Workstation/x86_64/iso/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        match = re.search(rf'Fedora-Workstation-Live-x86_64-{re.escape(ver)}-([\d\.]+)\.iso', html)
        if match:
            return match.group(1)
    except Exception as e:
        print(f"error getting fedora iso suffix for {ver}: {e}")
    return None

def check_opensuse_leap():
    # check latest release version of opensuse leap
    url = "https://download.opensuse.org/distribution/leap/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'href="(\d+\.\d+)/"', html)
        if versions:
            return max(versions, key=lambda v: [int(x) for x in v.split('.')])
    except Exception as e:
        print(f"error checking opensuse leap: {e}")
    return None

def check_openbsd():
    # check latest release version of openbsd
    url = "https://cdn.openbsd.org/pub/OpenBSD/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'href="(\d+\.\d+)/"', html)
        if versions:
            return max(versions, key=lambda v: [int(x) for x in v.split('.')])
    except Exception as e:
        print(f"error checking openbsd: {e}")
    return None

def check_netbsd():
    # check latest release version of netbsd
    url = "https://ftp.netbsd.org/pub/NetBSD/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'href="NetBSD-(\d+\.\d+(?:\.\d+)?)/"', html)
        if versions:
            return max(versions, key=lambda v: [int(x) for x in v.split('.')])
    except Exception as e:
        print(f"error checking netbsd: {e}")
    return None

def check_proxmox():
    # check latest release version of proxmox
    url = "https://enterprise.proxmox.com/iso/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'proxmox-ve_(\d+\.\d+-\d+)\.iso', html)
        if versions:
            def sort_key(v):
                parts = re.split(r'[.-]', v)
                return [int(p) for p in parts]
            return max(versions, key=sort_key)
    except Exception as e:
        print(f"error checking proxmox: {e}")
    return None

def check_freebsd():
    # check latest release version of freebsd
    url = "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'href="(\d+\.\d+)/"', html)
        if versions:
            return max(versions, key=lambda v: [int(x) for x in v.split('.')])
    except Exception as e:
        print(f"error checking freebsd: {e}")
    return None

def check_alpine():
    # check latest release version of alpine linux
    url = "https://dl-cdn.alpinelinux.org/alpine/latest-stable/releases/x86_64/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'alpine-standard-(\d+\.\d+\.\d+)-x86_64\.iso', html)
        if versions:
            return max(versions, key=lambda v: [int(x) for x in v.split('.')])
    except Exception as e:
        print(f"error checking alpine: {e}")
    return None

def check_mint():
    # check latest release version of linux mint
    url = "https://mirrors.kernel.org/linuxmint/stable/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'href="(\d+\.\d+(?:\.\d+)?)/"', html)
        if versions:
            return max(versions, key=lambda v: [int(x) for x in v.split('.')])
    except Exception as e:
        print(f"error checking linux mint: {e}")
    return None

def check_kali():
    # check latest release version of kali linux
    url = "https://cdimage.kali.org/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'href="kali-(\d{4}\.\d+)/"', html)
        if versions:
            return max(versions, key=lambda v: [int(x) for x in v.split('.')])
    except Exception as e:
        print(f"error checking kali: {e}")
    return None

def check_nixos():
    # check latest release version of nixos
    url = "https://channels.nixos.org/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'href="nixos-(\d{2}\.\d{2})/"', html)
        if versions:
            return max(versions, key=lambda v: [int(x) for x in v.split('.')])
    except Exception as e:
        print(f"error checking nixos: {e}")
    return None

def check_almalinux(major_version):
    # check latest release version of almalinux
    url = "https://repo.almalinux.org/almalinux/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(rf'href="({re.escape(major_version)}\.\d+)/"', html)
        if versions:
            return max(versions, key=lambda v: [int(x) for x in v.split('.')])
    except Exception as e:
        print(f"error checking almalinux: {e}")
    return None

def check_rocky(major_version):
    # check latest release version of rocky linux
    url = "https://download.rockylinux.org/pub/rocky/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(rf'href="({re.escape(major_version)}\.\d+)/"', html)
        if versions:
            return max(versions, key=lambda v: [int(x) for x in v.split('.')])
    except Exception as e:
        print(f"error checking rocky: {e}")
    return None

def check_void_linux():
    # check latest release version of void linux
    url = "https://repo-default.voidlinux.org/live/current/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        dates = re.findall(r'void-live-x86_64-musl-(\d+)-xfce\.iso', html)
        if dates:
            return max(dates, key=int)
    except Exception as e:
        print(f"error checking void linux: {e}")
    return None

def check_gentoo():
    # check latest release version of gentoo
    url = "https://distfiles.gentoo.org/releases/amd64/autobuilds/current-install-amd64-minimal/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'install-amd64-minimal-(\d+T\d+Z)\.iso', html)
        if versions:
            return max(versions)
    except Exception as e:
        print(f"error checking gentoo: {e}")
    return None

def check_vyos():
    # check latest release version of vyos
    url = "https://downloads.vyos.io/release/stream/1.4/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'VyOS-1.4-rolling-(\d+)-amd64\.iso', html)
        if versions:
            return max(versions)
    except Exception as e:
        print(f"error checking vyos: {e}")
    return None

def check_flatcar():
    # check latest stable version of flatcar
    url = "https://stable.release.flatcar-linux.net/amd64-usr/current/version.txt"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            text = r.read().decode('utf-8')
        match = re.search(r'FLATCAR_VERSION=([\d\.]+)', text)
        if match:
            return match.group(1)
    except Exception as e:
        print(f"error checking flatcar: {e}")
    return None

def check_opnsense():
    # check latest release version of opnsense
    url = "https://mirror.ams1.nl.leaseweb.net/opnsense/releases/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'href="(\d+\.\d+)/"', html)
        if versions:
            return max(versions, key=lambda v: [int(x) for x in v.split('.')])
    except Exception as e:
        print(f"error checking opnsense: {e}")
    return None

def check_github_latest_release(repo):
    # check latest release tag from github releases
    url = f"https://github.com/{repo}/releases"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        tags = re.findall(rf'href="/{re.escape(repo)}/releases/tag/v?([\d\.]+)"', html)
        if tags:
            unique_tags = list(set(tags))
            def sort_key(v):
                return [int(x) for x in v.split('.') if x.isdigit()]
            return max(unique_tags, key=sort_key)
    except Exception as e:
        print(f"error checking github release for {repo}: {e}")
    return None

def check_finnix():
    # check latest release version of finnix
    url = "https://www.finnix.org/releases/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'finnix-(\d+)\.iso', html)
        if versions:
            return max(versions, key=int)
    except Exception as e:
        print(f"error checking finnix: {e}")
    return None

def check_tinycore():
    # check latest release version of tinycore
    url = "http://tinycorelinux.net/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'href="(\d+)\.x/"', html)
        if versions:
            return max(versions, key=int)
    except Exception as e:
        print(f"error checking tinycore: {e}")
    return None

def check_sourceforge_version(project, folder):
    # check latest release version of a sourceforge project folder
    url = f"https://sourceforge.net/projects/{project}/rss?path=/{folder}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            xml = r.read().decode('utf-8')
        pattern = rf'/{re.escape(folder)}/([^/]+)/'
        matches = re.findall(pattern, xml)
        if matches:
            filtered_matches = [
                m for m in matches 
                if not any(x in m.lower() for x in ["pre", "beta", "rc", "alpha", "test", "unstable"])
            ]
            if not filtered_matches:
                filtered_matches = matches
            unique_matches = list(set(filtered_matches))
            def sort_key(v):
                parts = re.split(r'[.-]', v)
                return [int(p) for p in parts if p.isdigit()]
            return max(unique_matches, key=sort_key)
    except Exception as e:
        print(f"error checking sourceforge {project}: {e}")
    return None

def check_endeavouros():
    # check latest release version of endeavouros
    url = "https://mirror.alpix.eu/endeavouros/iso/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
        versions = re.findall(r'EndeavourOS_(.*?)\.iso', html)
        if versions:
            return max(versions)
    except Exception as e:
        print(f"error checking endeavouros: {e}")
    return None

def write_back_db(new_db):
    # write updated database back to src/distros.py preserving structure
    category_order = [
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
        "linux/ai-ml", "linux/developer", "linux/desktop-env", "linux/embedded", "linux/specialized", "linux/office", "linux/hardware", "linux/live-tools", "linux/education", "linux/scientific", "linux/legacy", "linux/others", "linux/experimental", "linux/alternative-arch", "linux/cloud", "linux/multimedia"
    ]
    
    category_names = {
        "linux/ubuntu": "ubuntu",
        "linux/ubuntu-noble": "ubuntu 24.04 noble",
        "linux/ubuntu-plucky": "ubuntu 25.04 plucky",
        "linux/ubuntu-jammy": "ubuntu 22.04 jammy",
        "linux/debian": "debian",
        "linux/debian-based": "debian derivatives",
        "linux/mint": "linux mint",
        "linux/pop-os": "pop!_os",
        "linux/zorin": "zorin os",
        "linux/arch-family": "arch family",
        "linux/enterprise": "enterprise / rpm",
        "linux/server": "server",
        "linux/server-cloud": "server & cloud",
        "linux/fedora-spins": "fedora spins & labs",
        "linux/gaming": "gaming",
        "linux/security": "security",
        "linux/pentesting": "pentesting & red team",
        "linux/forensic": "forensic & digital investigation",
        "linux/privacy": "privacy & security focused",
        "linux/immutable": "immutable / atomic desktops",
        "linux/wayland-tiling": "wayland / tiling wm",
        "linux/rolling": "rolling release",
        "linux/lightweight": "lightweight",
        "linux/minimal": "minimal & diy",
        "homelab": "homelab",
        "homelab/virtualization": "virtualization",
        "homelab/firewall": "firewall / router",
        "homelab/nas": "nas",
        "specialized/vintage": "vintage / novelty / retro",
        "specialized/containers": "containers & cloud native",
        "specialized/risc-emulation": "risc / emulation / research",
        "recovery/tools": "recovery & rescue tools",
        "recovery/backup": "backup & recovery",
        "arm/raspberry-pi": "raspberry pi",
        "arm/sbc": "arm / sbc",
        "windows/eval": "windows evaluation",
        "android-x86": "android-x86",
        "chromeos": "chromeos",
        "alternative/bsd": "bsd / alternative",
        "linux/ai-ml": "ai / machine learning",
        "linux/developer": "developer tools",
        "linux/desktop-env": "desktop environments",
        "linux/embedded": "embedded & iot",
        "linux/specialized": "specialized / custom",
        "linux/office": "office & productivity",
        "linux/hardware": "hardware specific",
        "linux/live-tools": "live usb tools",
        "linux/education": "education & learning",
        "linux/scientific": "scientific & data science",
        "linux/legacy": "legacy / old stable",
        "linux/others": "other distributions",
        "linux/experimental": "experimental",
        "linux/alternative-arch": "alternative architectures",
        "linux/cloud": "cloud",
        "linux/multimedia": "multimedia"
    }

    def format_val(val):
        if isinstance(val, str):
            return json.dumps(val)
        elif isinstance(val, bool):
            return "True" if val else "False"
        elif val is None:
            return "None"
        elif isinstance(val, (int, float)):
            return str(val)
        elif isinstance(val, list):
            return "[" + ", ".join(format_val(x) for x in val) + "]"
        elif isinstance(val, dict):
            return "{" + ", ".join(f"{format_val(k)}: {format_val(v)}" for k, v in val.items()) + "}"
        else:
            return repr(val)

    sorted_keys = []
    for cat in category_order:
        if cat in new_db:
            sorted_keys.append(cat)
    for cat in sorted(new_db.keys()):
        if cat not in sorted_keys:
            sorted_keys.append(cat)

    distros_path = os.path.join(os.path.dirname(script_dir), 'src', 'distros.py')
    with open(distros_path, 'w') as f:
        f.write("# updated auto-version-checker\n\nDB: dict[str, list[dict]] = {\n")
        for idx, cat in enumerate(sorted_keys):
            comment_name = category_names.get(cat, cat.replace('linux/', '').replace('-', ' ').lower())
            f.write(f"\n    # {comment_name}\n")
            f.write(f"    \"{cat}\": [\n")
            for e in new_db[cat]:
                ordered_keys = []
                keys = list(e.keys())
                for k in ["name", "url", "size"]:
                    if k in keys:
                        ordered_keys.append(k)
                        keys.remove(k)
                ordered_keys.extend(keys)
                
                parts = []
                for k in ordered_keys:
                    parts.append(f'"{k}": {format_val(e[k])}')
                line = "        {" + ", ".join(parts) + "},"
                f.write(line + "\n")
            f.write("    ]")
            if idx < len(sorted_keys) - 1:
                f.write(",\n")
            else:
                f.write("\n")
        f.write("}\n\n")
        f.write("if __name__ == '__main__':\n")
        f.write("    total = sum(len(v) for v in DB.values())\n")
        f.write("    print(f\"refactor complete: total {total} entries\")\n")

def main():
    # main execution flow
    print("checking for distribution updates...")
    updates = []
    
    # 1. check debian stable netinst
    latest_debian = check_debian()
    if latest_debian:
        debian_entries = DB.get("linux/debian", [])
        for entry in debian_entries:
            if "Netinst" in entry["name"]:
                url = entry["url"]
                if latest_debian not in url and latest_debian not in entry["name"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/debian",
                        "current": entry["name"],
                        "latest": f"Debian {latest_debian} Netinst",
                        "url": f"https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-{latest_debian}-amd64-netinst.iso"
                    })
                    
    # 2. check ubuntu noble, jammy, plucky, and future
    for version_prefix, cat in [("26.04", "linux/ubuntu"), ("25.04", "linux/ubuntu-plucky"), ("24.04", "linux/ubuntu-noble"), ("22.04", "linux/ubuntu-jammy"), ("26.04", "linux/server")]:
        latest_ub = check_ubuntu_releases(version_prefix)
        if latest_ub:
            entries = DB.get(cat, [])
            for entry in entries:
                if "Desktop" in entry["name"] or "Server" in entry["name"]:
                    if latest_ub not in entry["url"] and latest_ub not in entry["name"]:
                        role = "Desktop" if "Desktop" in entry["name"] else "Server"
                        iso_suffix = "desktop-amd64.iso" if role == "Desktop" else "live-server-amd64.iso"
                        updates.append({
                            "name": entry["name"],
                            "category": cat,
                            "current": entry["name"],
                            "latest": f"Ubuntu {latest_ub} {role}",
                            "url": f"https://releases.ubuntu.com/{latest_ub}/ubuntu-{latest_ub}-{iso_suffix}"
                        })

    # 3. check ubuntu flavors
    for flavor, cat, name_keyword in [
        ("kubuntu", "linux/ubuntu", "Kubuntu"),
        ("xubuntu", "linux/ubuntu", "Xubuntu"),
        ("lubuntu", "linux/ubuntu", "Lubuntu"),
        ("edubuntu", "linux/ubuntu", "Edubuntu"),
        ("ubuntu-budgie", "linux/office", "Ubuntu Budgie"),
        ("kubuntu", "linux/ubuntu-jammy", "Kubuntu"),
        ("xubuntu", "linux/ubuntu-jammy", "Xubuntu"),
    ]:
        latest_f = check_ubuntu_flavor(flavor)
        if latest_f:
            entries = DB.get(cat, [])
            for entry in entries:
                if name_keyword in entry["name"]:
                    match_pref = re.search(r'\d{2}\.\d{2}', entry["name"])
                    if match_pref:
                        pref = match_pref.group(0)
                        if latest_f.startswith(pref):
                            if latest_f not in entry["url"] and latest_f not in entry["name"]:
                                updates.append({
                                    "name": entry["name"],
                                    "category": cat,
                                    "current": entry["name"],
                                    "latest": f"{name_keyword} {latest_f}",
                                    "url": f"https://cdimage.ubuntu.com/{flavor}/releases/{latest_f}/release/{flavor}-{latest_f}-desktop-amd64.iso"
                                })

    # 4. check pop!_os
    pop_entries = DB.get("linux/pop-os", [])
    for entry in pop_entries:
        if "Pop!_OS" in entry["name"]:
            match_url = re.search(r'/(\d{2}\.\d{2})/amd64/(intel|nvidia)/(\d+)/', entry["url"])
            if match_url:
                version_pref = match_url.group(1)
                gpu = match_url.group(2)
                current_build = int(match_url.group(3))
                latest_build = check_pop_os_version_helper(version_pref, current_build)
                if latest_build > current_build:
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/pop-os",
                        "current": entry["name"],
                        "latest": f"Pop!_OS {version_pref} LTS ({gpu.upper()} build {latest_build})",
                        "url": f"https://iso.pop-os.org/{version_pref}/amd64/{gpu}/{latest_build}/pop-os_{version_pref}_amd64_{gpu}_{latest_build}.iso"
                    })

    # probe new pop!_os version releases (e.g. 25.04, 26.04)
    for next_ver in ["25.04", "26.04"]:
        ver_already_exists = any(next_ver in entry["url"] for entry in pop_entries)
        if not ver_already_exists:
            url_probe = f"https://iso.pop-os.org/{next_ver}/amd64/intel/1/pop-os_{next_ver}_amd64_intel_1.iso"
            req = urllib.request.Request(url_probe, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
            try:
                with urllib.request.urlopen(req, timeout=5) as r:
                    if r.status == 200:
                        latest_build = check_pop_os_version_helper(next_ver, 1)
                        updates.append({
                            "name": f"Pop!_OS {next_ver} LTS",
                            "category": "linux/pop-os",
                            "current": "(new distribution release)",
                            "latest": f"Pop!_OS {next_ver} LTS (Intel build {latest_build})",
                            "url": f"https://iso.pop-os.org/{next_ver}/amd64/intel/{latest_build}/pop-os_{next_ver}_amd64_intel_{latest_build}.iso"
                        })
                        updates.append({
                            "name": f"Pop!_OS {next_ver} LTS (NVIDIA)",
                            "category": "linux/pop-os",
                            "current": "(new distribution release)",
                            "latest": f"Pop!_OS {next_ver} LTS (NVIDIA build {latest_build})",
                            "url": f"https://iso.pop-os.org/{next_ver}/amd64/nvidia/{latest_build}/pop-os_{next_ver}_amd64_nvidia_{latest_build}.iso"
                        })
            except Exception:
                pass

    # 5. check zorin os
    zorin_info = check_zorin()
    if zorin_info:
        latest_major, latest_ver = zorin_info
        zorin_entries = DB.get("linux/zorin", [])
        for entry in zorin_entries:
            if "Zorin OS" in entry["name"]:
                if latest_ver not in entry["url"] and latest_ver not in entry["name"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/zorin",
                        "current": entry["name"],
                        "latest": f"Zorin OS {latest_ver} Core",
                        "url": f"https://distro.ibiblio.org/zorinos/{latest_major}/Zorin-OS-{latest_ver}-Core-64-bit.iso"
                    })

    # 6. check manjaro
    manjaro_info = check_manjaro()
    if manjaro_info:
        latest_ver, latest_file_prefix = manjaro_info
        manjaro_entries = DB.get("linux/arch-family", [])
        for entry in manjaro_entries:
            if "Manjaro" in entry["name"]:
                if latest_ver not in entry["url"]:
                    flavor = "kde" if "KDE" in entry["name"] else ("gnome" if "GNOME" in entry["name"] else "xfce")
                    flavor_file = latest_file_prefix.replace("-kde-", f"-{flavor}-")
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/arch-family",
                        "current": entry["name"],
                        "latest": f"Manjaro {flavor.upper()} {latest_ver}",
                        "url": f"https://download.manjaro.org/{flavor}/{latest_ver}/{flavor_file}.iso"
                    })

    # 7. check endeavouros
    latest_eos = check_endeavouros()
    if latest_eos:
        eos_entries = DB.get("linux/arch-family", [])
        for entry in eos_entries:
            if "EndeavourOS" in entry["name"]:
                if latest_eos not in entry["url"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/arch-family",
                        "current": entry["name"],
                        "latest": f"EndeavourOS {latest_eos.replace('_', ' ')}",
                        "url": f"https://mirror.alpix.eu/endeavouros/iso/EndeavourOS_{latest_eos}.iso"
                    })

    # 8. check fedora and its spins/labs/atomic variants
    latest_fedora = check_fedora()
    if latest_fedora:
        suffix = get_fedora_iso_suffix(latest_fedora)
        if suffix:
            for cat in ["linux/enterprise", "linux/fedora-spins", "linux/gaming", "linux/immutable", "linux/ai-ml", "linux/multimedia"]:
                entries = DB.get(cat, [])
                for entry in entries:
                    if "Fedora" in entry["name"] and "Legacy" not in entry["name"]:
                        if latest_fedora not in entry["url"]:
                            if "Workstation" in entry["name"]:
                                subpath = f"Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-{latest_fedora}-{suffix}.iso"
                                new_name = f"Fedora {latest_fedora} Workstation"
                            elif "Server" in entry["name"]:
                                subpath = f"Server/x86_64/iso/Fedora-Server-dvd-x86_64-{latest_fedora}-{suffix}.iso"
                                new_name = f"Fedora {latest_fedora} Server"
                            elif "Silverblue" in entry["name"]:
                                subpath = f"Silverblue/x86_64/iso/Fedora-Silverblue-ostree-x86_64-{latest_fedora}-{suffix}.iso"
                                new_name = f"Fedora Silverblue {latest_fedora}"
                            elif "Kinoite" in entry["name"]:
                                subpath = f"Kinoite/x86_64/iso/Fedora-Kinoite-ostree-x86_64-{latest_fedora}-{suffix}.iso"
                                new_name = f"Fedora Kinoite {latest_fedora}"
                            elif "Spin" in entry["name"] or "Spin" in entry.get("tags", []) or cat == "linux/fedora-spins":
                                flavor = "KDE" if "KDE" in entry["name"] else ("Xfce" if "XFCE" in entry["name"] else ("Cinnamon" if "Cinnamon" in entry["name"] else ("Sway" if "Sway" in entry["name"] else ("i3" if "i3" in entry["name"] else "Budgie"))))
                                subpath = f"Spins/x86_64/iso/Fedora-{flavor}-Live-x86_64-{latest_fedora}-{suffix}.iso"
                                new_name = f"Fedora {latest_fedora} {flavor} Spin"
                            else:
                                if "Scientific" in entry["name"]:
                                    lab = "Scientific_KDE"
                                    new_name = f"Fedora {latest_fedora} Scientific KDE"
                                elif "Security" in entry["name"]:
                                    lab = "Security"
                                    new_name = f"Fedora {latest_fedora} Security Lab"
                                elif "Design" in entry["name"]:
                                    lab = "Design_suite"
                                    new_name = f"Fedora {latest_fedora} Design Suite"
                                elif "Gaming" in entry["name"]:
                                    lab = "Gaming"
                                    new_name = f"Fedora {latest_fedora} Gaming Lab"
                                elif "AI" in entry["name"]:
                                    lab = "AI"
                                    new_name = f"Fedora {latest_fedora} AI Spin"
                                else:
                                    lab = "Jam_KDE"
                                    new_name = f"Fedora {latest_fedora} Jam KDE"
                                subpath = f"Labs/x86_64/iso/Fedora-{lab}-Live-x86_64-{latest_fedora}-{suffix}.iso"
                            
                            updates.append({
                                "name": entry["name"],
                                "category": cat,
                                "current": entry["name"],
                                "latest": new_name,
                                "url": f"https://dl.fedoraproject.org/pub/fedora/linux/releases/{latest_fedora}/{subpath}"
                            })

    # 9. check opensuse leap
    latest_leap = check_opensuse_leap()
    if latest_leap:
        leap_entries = DB.get("linux/enterprise", [])
        for entry in leap_entries:
            if "openSUSE Leap" in entry["name"]:
                if latest_leap not in entry["url"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/enterprise",
                        "current": entry["name"],
                        "latest": f"openSUSE Leap {latest_leap} DVD",
                        "url": f"https://download.opensuse.org/distribution/leap/{latest_leap}/iso/openSUSE-Leap-{latest_leap}-DVD-x86_64-Media.iso"
                    })

    # 10. check proxmox ve
    latest_pve = check_proxmox()
    if latest_pve:
        pve_entries = DB.get("homelab/virtualization", [])
        for entry in pve_entries:
            if "Proxmox VE" in entry["name"]:
                if latest_pve not in entry["url"] and latest_pve not in entry["name"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "homelab/virtualization",
                        "current": entry["name"],
                        "latest": f"Proxmox VE {latest_pve}",
                        "url": f"https://enterprise.proxmox.com/iso/proxmox-ve_{latest_pve}.iso"
                    })

    # 11. check freebsd
    latest_bsd = check_freebsd()
    if latest_bsd:
        bsd_entries = DB.get("alternative/bsd", [])
        for entry in bsd_entries:
            if "FreeBSD" in entry["name"]:
                if latest_bsd not in entry["url"] and latest_bsd not in entry["name"]:
                    flavor = "dvd1" if "DVD" in entry["name"] else "bootonly"
                    suffix_name = "amd64 DVD" if flavor == "dvd1" else "amd64 Bootonly"
                    updates.append({
                        "name": entry["name"],
                        "category": "alternative/bsd",
                        "current": entry["name"],
                        "latest": f"FreeBSD {latest_bsd} {suffix_name}",
                        "url": f"https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/{latest_bsd}/FreeBSD-{latest_bsd}-RELEASE-amd64-{flavor}.iso"
                    })

    # 12. check openbsd
    latest_obsd = check_openbsd()
    if latest_obsd:
        obsd_entries = DB.get("alternative/bsd", [])
        for entry in obsd_entries:
            if "OpenBSD" in entry["name"]:
                if latest_obsd not in entry["url"]:
                    ver_nodot = latest_obsd.replace(".", "")
                    updates.append({
                        "name": entry["name"],
                        "category": "alternative/bsd",
                        "current": entry["name"],
                        "latest": f"OpenBSD {latest_obsd} amd64",
                        "url": f"https://cdn.openbsd.org/pub/OpenBSD/{latest_obsd}/amd64/install{ver_nodot}.iso"
                    })

    # 13. check netbsd
    latest_nbsd = check_netbsd()
    if latest_nbsd:
        nbsd_entries = DB.get("alternative/bsd", [])
        for entry in nbsd_entries:
            if "NetBSD" in entry["name"]:
                if latest_nbsd not in entry["url"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "alternative/bsd",
                        "current": entry["name"],
                        "latest": f"NetBSD {latest_nbsd} amd64",
                        "url": f"https://ftp.netbsd.org/pub/NetBSD/NetBSD-{latest_nbsd}/images/NetBSD-{latest_nbsd}-amd64.iso"
                    })

    # 14. check alpine linux
    latest_alpine = check_alpine()
    if latest_alpine:
        alpine_entries = DB.get("linux/minimal", []) + DB.get("linux/alternative-arch", [])
        for entry in alpine_entries:
            if "Alpine Linux" in entry["name"] or "Alpine Virt" in entry["name"]:
                if latest_alpine not in entry["url"] and latest_alpine not in entry["name"]:
                    branch = "v" + ".".join(latest_alpine.split(".")[:2])
                    if "ARM64" in entry["name"]:
                        arch = "aarch64"
                        flavor_suffix = "aarch64"
                    elif "Virt" in entry["name"]:
                        arch = "x86_64"
                        flavor_suffix = f"virt-{latest_alpine}-x86_64"
                    elif "Extended" in entry["name"]:
                        arch = "x86_64"
                        flavor_suffix = f"extended-{latest_alpine}-x86_64"
                    else:
                        arch = "x86_64"
                        flavor_suffix = f"standard-{latest_alpine}-x86_64"
                    
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/minimal" if "ARM64" not in entry["name"] else "linux/alternative-arch",
                        "current": entry["name"],
                        "latest": f"Alpine Linux {latest_alpine} Standard" if "Standard" in entry["name"] else entry["name"].replace("3.21.3", latest_alpine).replace("3.21", latest_alpine),
                        "url": f"https://dl-cdn.alpinelinux.org/alpine/{branch}/releases/{arch}/alpine-{flavor_suffix}.iso"
                    })

    # 15. check linux mint
    latest_mint = check_mint()
    if latest_mint:
        mint_entries = DB.get("linux/mint", [])
        for entry in mint_entries:
            if "Cinnamon" in entry["name"] or "XFCE" in entry["name"] or "MATE" in entry["name"]:
                if latest_mint not in entry["url"] and latest_mint not in entry["name"]:
                    role = "Cinnamon" if "Cinnamon" in entry["name"] else ("XFCE" if "XFCE" in entry["name"] else "MATE")
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/mint",
                        "current": entry["name"],
                        "latest": f"Linux Mint {latest_mint} {role}",
                        "url": f"https://mirrors.kernel.org/linuxmint/stable/{latest_mint}/linuxmint-{latest_mint}-{role.lower()}-64bit.iso"
                    })

    # 16. check kali linux
    latest_kali = check_kali()
    if latest_kali:
        kali_entries = DB.get("linux/security", [])
        for entry in kali_entries:
            if "Kali" in entry["name"] and "Installer" in entry["name"]:
                if latest_kali not in entry["url"] and latest_kali not in entry["name"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/security",
                        "current": entry["name"],
                        "latest": f"Kali Linux {latest_kali} Installer",
                        "url": f"https://cdimage.kali.org/kali-{latest_kali}/kali-linux-{latest_kali}-installer-amd64.iso"
                    })

    # 17. check nixos
    latest_nixos = check_nixos()
    if latest_nixos:
        nixos_entries = DB.get("linux/immutable", [])
        for entry in nixos_entries:
            if "NixOS" in entry["name"]:
                if latest_nixos not in entry["url"] and latest_nixos not in entry["name"]:
                    flavor = "gnome" if "GNOME" in entry["name"] else "plasma6"
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/immutable",
                        "current": entry["name"],
                        "latest": f"NixOS {latest_nixos} {flavor.upper()}",
                        "url": f"https://channels.nixos.org/nixos-{latest_nixos}/latest-nixos-{flavor}-x86_64-linux.iso"
                    })

    # 18. check almalinux 9
    latest_alma9 = check_almalinux("9")
    if latest_alma9:
        alma_entries = DB.get("linux/enterprise", [])
        for entry in alma_entries:
            if "AlmaLinux" in entry["name"] and "9" in entry["name"]:
                if latest_alma9 not in entry["url"] and latest_alma9 not in entry["name"]:
                    flavor = "minimal" if "Minimal" in entry["name"] else "dvd"
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/enterprise",
                        "current": entry["name"],
                        "latest": f"AlmaLinux {latest_alma9} Minimal" if flavor == "minimal" else f"AlmaLinux {latest_alma9} DVD",
                        "url": f"https://repo.almalinux.org/almalinux/{latest_alma9}/isos/x86_64/AlmaLinux-{latest_alma9}-latest-x86_64-{flavor}.iso"
                    })

    # 19. check rocky linux 9
    latest_rocky9 = check_rocky("9")
    if latest_rocky9:
        rocky_entries = DB.get("linux/enterprise", [])
        for entry in rocky_entries:
            if "Rocky Linux" in entry["name"] and "9" in entry["name"]:
                if latest_rocky9 not in entry["url"] and latest_rocky9 not in entry["name"]:
                    flavor = "minimal" if "Minimal" in entry["name"] else "dvd"
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/enterprise",
                        "current": entry["name"],
                        "latest": f"Rocky Linux {latest_rocky9} Minimal" if flavor == "minimal" else f"Rocky Linux {latest_rocky9} DVD",
                        "url": f"https://download.rockylinux.org/pub/rocky/{latest_rocky9}/isos/x86_64/Rocky-{latest_rocky9}-latest-x86_64-{flavor}.iso"
                    })

    # 20. check void linux
    latest_void = check_void_linux()
    if latest_void:
        void_entries = DB.get("linux/minimal", [])
        for entry in void_entries:
            if "Void Linux" in entry["name"]:
                if latest_void not in entry["url"]:
                    flavor = "xfce" if "XFCE" in entry["name"] else "base"
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/minimal",
                        "current": entry["name"],
                        "latest": f"Void Linux {flavor.upper()}",
                        "url": f"https://repo-default.voidlinux.org/live/current/void-live-x86_64-musl-{latest_void}-{flavor}.iso"
                    })

    # 21. check gentoo
    latest_gentoo = check_gentoo()
    if latest_gentoo:
        gentoo_entries = DB.get("linux/minimal", [])
        for entry in gentoo_entries:
            if "Gentoo Minimal Install" in entry["name"]:
                if latest_gentoo not in entry["url"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/minimal",
                        "current": entry["name"],
                        "latest": "Gentoo Minimal Install",
                        "url": f"https://distfiles.gentoo.org/releases/amd64/autobuilds/current-install-amd64-minimal/install-amd64-minimal-{latest_gentoo}.iso"
                    })

    # 22. check vyos
    latest_vyos = check_vyos()
    if latest_vyos:
        vyos_entries = DB.get("homelab", [])
        for entry in vyos_entries:
            if "VyOS" in entry["name"]:
                if latest_vyos not in entry["url"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "homelab",
                        "current": entry["name"],
                        "latest": f"VyOS 1.4 rolling {latest_vyos}",
                        "url": f"https://downloads.vyos.io/release/stream/1.4/VyOS-1.4-rolling-{latest_vyos}-amd64.iso"
                    })

    # 23. check opnsense
    latest_opn = check_opnsense()
    if latest_opn:
        opn_entries = DB.get("homelab/firewall", [])
        for entry in opn_entries:
            if "OPNsense" in entry["name"]:
                if latest_opn not in entry["url"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "homelab/firewall",
                        "current": entry["name"],
                        "latest": f"OPNsense {latest_opn} DVD",
                        "url": f"https://mirror.ams1.nl.leaseweb.net/opnsense/releases/{latest_opn}/OPNsense-{latest_opn}-dvd-amd64.iso.bz2"
                    })

    # 24. check harvester hci
    latest_harvester = check_github_latest_release("harvester/harvester")
    if latest_harvester:
        harvester_entries = DB.get("homelab/virtualization", [])
        for entry in harvester_entries:
            if "Harvester HCI" in entry["name"]:
                if latest_harvester not in entry["url"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "homelab/virtualization",
                        "current": entry["name"],
                        "latest": f"Harvester HCI v{latest_harvester}",
                        "url": f"https://releases.rancher.com/harvester/v{latest_harvester}/harvester-v{latest_harvester}-amd64.iso"
                    })

    # 25. check finnix
    latest_finnix = check_finnix()
    if latest_finnix:
        finnix_entries = DB.get("linux/specialized", [])
        for entry in finnix_entries:
            if "Finnix" in entry["name"]:
                if latest_finnix not in entry["url"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/specialized",
                        "current": entry["name"],
                        "latest": f"Finnix {latest_finnix} Recovery",
                        "url": f"https://www.finnix.org/releases/{latest_finnix}/finnix-{latest_finnix}.iso"
                    })

    # 26. check tinycore
    latest_tc = check_tinycore()
    if latest_tc:
        tc_entries = DB.get("specialized/vintage", [])
        for entry in tc_entries:
            if "TinyCore Linux" in entry["name"]:
                if f"{latest_tc}.x" not in entry["url"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "specialized/vintage",
                        "current": entry["name"],
                        "latest": f"TinyCore Linux {latest_tc}",
                        "url": f"http://tinycorelinux.net/{latest_tc}.x/x86_64/release/TinyCorePure64-current.iso"
                    })

    # 27. check clonezilla
    latest_clonezilla = check_sourceforge_version("clonezilla", "clonezilla_live_stable")
    if latest_clonezilla:
        clonezilla_entries = DB.get("recovery/tools", [])
        for entry in clonezilla_entries:
            if "CloneZilla" in entry["name"] and "Latest" not in entry["name"]:
                if latest_clonezilla not in entry["url"] and latest_clonezilla not in entry["name"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "recovery/tools",
                        "current": entry["name"],
                        "latest": f"CloneZilla {latest_clonezilla}",
                        "url": f"https://sourceforge.net/projects/clonezilla/files/clonezilla_live_stable/{latest_clonezilla}/clonezilla-live-{latest_clonezilla}-amd64.iso/download"
                    })

    # 28. check gparted
    latest_gparted = check_sourceforge_version("gparted", "gparted-live-stable")
    if latest_gparted:
        gparted_entries = DB.get("recovery/tools", [])
        for entry in gparted_entries:
            if "GParted" in entry["name"]:
                if latest_gparted not in entry["url"] and latest_gparted not in entry["name"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "recovery/tools",
                        "current": entry["name"],
                        "latest": f"GParted Live {latest_gparted}",
                        "url": f"https://sourceforge.net/projects/gparted/files/gparted-live-stable/{latest_gparted}/gparted-live-{latest_gparted}-amd64.iso/download"
                    })

    # 29. check linux lite
    latest_lite = check_sourceforge_version("linuxlite", "")
    if latest_lite and re.match(r'^\d+\.\d+$', latest_lite):
        lite_entries = DB.get("linux/lightweight", [])
        for entry in lite_entries:
            if "Linux Lite" in entry["name"]:
                if latest_lite not in entry["url"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/lightweight",
                        "current": entry["name"],
                        "latest": f"Linux Lite {latest_lite}",
                        "url": f"https://sourceforge.net/projects/linuxlite/files/{latest_lite}/linux-lite-{latest_lite}-64bit.iso/download"
                    })

    # 30. check bodhi linux
    latest_bodhi = check_sourceforge_version("bodhilinux", "")
    if latest_bodhi and re.match(r'^\d+\.\d+\.\d+$', latest_bodhi):
        bodhi_entries = DB.get("linux/lightweight", [])
        for entry in bodhi_entries:
            if "Bodhi Linux" in entry["name"]:
                if latest_bodhi not in entry["url"]:
                    updates.append({
                        "name": entry["name"],
                        "category": "linux/lightweight",
                        "current": entry["name"],
                        "latest": f"Bodhi Linux {latest_bodhi}",
                        "url": f"https://sourceforge.net/projects/bodhilinux/files/{latest_bodhi}/bodhi-{latest_bodhi}-64.iso/download"
                    })

    # report updates
    report_path = os.path.join(os.path.dirname(script_dir), "updates_report.txt")
    if updates:
        print(f"\ndiscovered {len(updates)} updates!")
        with open(report_path, "w") as f:
            f.write("[✓] upstream os updates discovered:\n")
            f.write("="*40 + "\n")
            for up in updates:
                line = f"- {up['name']} in `{up['category']}`\n  current: {up['current']}\n  latest:  {up['latest']}\n  new url: {up['url']}\n"
                print(line)
                f.write(line + "\n")
    else:
        print("\nall checked distributions are up to date.")
        if os.path.exists(report_path):
            try:
                os.remove(report_path)
            except OSError:
                pass

    # write changes back to distros.py if requested
    if len(sys.argv) > 1 and sys.argv[1] in ["--write", "-w"] and updates:
        for up in updates:
            cat = up["category"]
            curr_name = up["current"]
            found = False
            for entry in DB.get(cat, []):
                if entry["name"] == curr_name:
                    entry["name"] = up["latest"]
                    entry["url"] = up["url"]
                    found = True
                    break
            if not found:
                if curr_name == "(new distribution release)":
                    DB.setdefault(cat, []).append({
                        "name": up["latest"],
                        "url": up["url"],
                        "size": "unknown"
                    })
        
        print("\nwriting updates back to src/distros.py...")
        write_back_db(DB)
        print("successfully updated src/distros.py!")
        
        # update web dashboard
        print("updating web dashboard...")
        import subprocess
        base_dir = os.path.dirname(script_dir)
        generate_script = os.path.join(base_dir, "src", "scripts", "generate_index.py")
        subprocess.run([sys.executable, generate_script])

if __name__ == "__main__":
    # execution hook
    main()
