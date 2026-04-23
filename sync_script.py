# Updated 2026-04-23

import os
import subprocess
from urllib.parse import urlparse

from distros import DB

c, g, r, y, w = '\033[96m', '\033[92m', '\033[91m', '\033[93m', '\033[0m'
remote_name   = "gdrive"
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
    "software-download.microsoft.com",
]

def is_single_stream(url: str) -> bool:
    host = urlparse(url).netloc.lower()
    return any(h in host for h in SINGLE_STREAM_HOSTS)

def dl(entry: dict, category: str):
    """Download one ISO entry, upload to GDrive, then remove the local file."""
    url          = entry["url"]
    display_name = entry["name"]
    size         = entry.get("size", "?")

    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename or "." not in filename:
        filename = url.split("/")[-1].split("?")[0]
    if "." not in filename:
        filename += ".iso"
    if filename.endswith(".img"):
        filename = filename.replace(".img", ".img.iso")

    local_dir  = f"./temp/{category}"
    local_file = os.path.join(local_dir, filename)
    remote_path = f"{remote_name}:{remote_folder}/{category}/{filename}"

    print(f"\n{c}[ check  ]{w} {display_name}  ({size})")

    check = subprocess.run(["rclone", "lsf", remote_path], capture_output=True)
    if check.returncode == 0 and filename in check.stdout.decode():
        print(f"{y}[ skip   ]{w} already in library.")
        return

    os.makedirs(local_dir, exist_ok=True)
    print(f"{c}[ fetch  ]{w} downloading...")

    aria_common = [
        "--retry-wait=10", "--max-tries=5",
        "--file-allocation=none",
        "--check-certificate=false",
        "--allow-overwrite=true",
        "--auto-file-renaming=false",
        "--dir", local_dir, "-o", filename, url,
    ]
    if is_single_stream(url):
        cmd = ["aria2c", "-x", "1",  "-s", "1"]  + aria_common
    else:
        cmd = ["aria2c", "-x", "16", "-s", "16"] + aria_common

    try:
        subprocess.run(cmd, check=True)
        print(f"{c}[ sync ]{w} uploading → gdrive:{remote_folder}/{category}/")
        subprocess.run([
            "rclone", "move", "-P",
            local_file,
            f"{remote_name}:{remote_folder}/{category}/",
        ], check=True)
        print(f"{g}[ ok ]{w} {display_name} secured.")

    except Exception as e:
        print(f"{r}[ error ]{w} {display_name}: {e}")
    finally:
        if os.path.exists(local_file):
            os.remove(local_file)
        try:
            os.rmdir(local_dir)
        except OSError:
            pass

if __name__ == "__main__":
    total = sum(len(v) for v in DB.values())
    cats  = len(DB)
    print(f"{c}[ info ]{w} {total} ISOs across {cats} categories")
    print(f"{c}[ info ]{w} Remote: {remote_name}:{remote_folder}")
    print()

    for cat, entries in DB.items():
        print(f"{y}── {cat} ({len(entries)}) ──{w}")
        for entry in entries:
            dl(entry, cat)

    print(f"\n{g}[ done ]{w} All entries processed.")
