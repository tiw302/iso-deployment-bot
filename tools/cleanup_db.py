# database cleanup script

import os
import sys
import urllib.request
import urllib.error
import subprocess

# setup path to import distros from parent directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(os.path.dirname(script_dir), "src"))
sys.path.append(os.path.join(os.path.dirname(script_dir), "src", "scripts"))
from distros import DB
from utils import resolve_filename

def get_drive_files():
    """get a set of filenames currently in gdrive."""
    files = set()
    try:
        remote_res = subprocess.run(["rclone", "listremotes"], capture_output=True, text=True)
        remotes = [r.strip().rstrip(':') for r in remote_res.stdout.strip().split('\n') if r.strip()]
        remote_name = remotes[0] if remotes else "gdrive"

        res = subprocess.run(
            ["rclone", "lsf", f"{remote_name}:os-deployment-library", "-R", "--files-only"],
            capture_output=True, text=True, timeout=60
        )
        if res.returncode == 0:
            for line in res.stdout.strip().split('\n'):
                files.add(os.path.basename(line))
    except Exception as e:
        print(f"warning: drive scan failed: {e}")
    return files

def is_link_working(url):
    """check if a link is still alive."""
    if not url or url == '#': return False
    try:
        req = urllib.request.Request(url, method='HEAD')
        req.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status < 400
    except:
        # try GET with range as fallback
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0')
            req.add_header('Range', 'bytes=0-0')
            with urllib.request.urlopen(req, timeout=5) as response:
                return response.status < 400
        except:
            return False

def get_expected_filename(url):
    return resolve_filename(url)

import json

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

def main():
    print("starting database cleanup...")

    drive_files = get_drive_files()
    print(f"found {len(drive_files)} files in gdrive.")

    new_db = {}
    removed_count = 0
    total_checked = 0

    # process categories
    for category, entries in DB.items():
        kept_entries = []
        for entry in entries:
            total_checked += 1
            filename = get_expected_filename(entry['url'])

            # criteria 1: is it in drive?
            in_drive = filename in drive_files

            if in_drive:
                kept_entries.append(entry)
                continue

            # criteria 2: is the link working?
            print(f"checking: {entry['name']}...", end='\r')
            if is_link_working(entry['url']):
                kept_entries.append(entry)
            else:
                removed_count += 1
                print(f"removing broken & unsynced: {entry['name']}          ")

        if kept_entries:
            new_db[category] = kept_entries

    print("\ncleanup finished.")
    print(f"total checked: {total_checked}")
    print(f"kept: {total_checked - removed_count}")
    print(f"removed: {removed_count}")

    # Reorganize and format categories to match refactor.py format
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

    sorted_keys = []
    for cat in category_order:
        if cat in new_db:
            sorted_keys.append(cat)
    for cat in sorted(new_db.keys()):
        if cat not in sorted_keys:
            sorted_keys.append(cat)

    # write back to distros.py
    distros_path = os.path.join(os.path.dirname(script_dir), 'src', 'distros.py')
    with open(distros_path, 'w') as f:
        f.write("# updated auto-cleanup\n\nDB: dict[str, list[dict]] = {\n")
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

    # update web
    print("\nupdating web dashboard...")
    base_dir = os.path.dirname(script_dir)
    generate_script = os.path.join(base_dir, "src", "scripts", "generate_index.py")
    subprocess.run(["python3", generate_script])

if __name__ == "__main__":
    main()
