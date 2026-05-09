# updated 2026-05-09

import os
import subprocess
import sys
import hashlib
import json
from urllib.parse import urlparse
from urllib.request import Request, urlopen

# setup path to import distros from parent directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))
from distros import DB

c, g, r, y, w = '\033[96m', '\033[92m', '\033[91m', '\033[93m', '\033[0m'
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

def discord_notify(message: str, color: int = 0x3498db):
    """send notification to discord webhook."""
    if not DISCORD_WEBHOOK:
        return
    
    payload = {
        "embeds": [{
            "description": message,
            "color": color
        }]
    }
    
    try:
        req = Request(DISCORD_WEBHOOK, data=json.dumps(payload).encode('utf-8'))
        req.add_header('Content-Type', 'application/json')
        req.add_header('User-Agent', 'Mozilla/5.0')
        with urlopen(req) as res:
            pass
    except Exception as e:
        print(f"{r}[ discord error ]{w} {e}")

def get_remote_name() -> str:
    """dynamically determine the remote name from rclone config."""
    try:
        result = subprocess.run(["rclone", "listremotes"], capture_output=True, text=True, check=True)
        remotes = [r.strip().rstrip(':') for r in result.stdout.strip().split('\n') if r.strip()]
        if remotes:
            return remotes[0]
    except Exception:
        pass
    return "gdrive" # fallback default

def calculate_sha256(file_path: str) -> str:
    """calculate sha256 checksum of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

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
    """download one iso entry, upload to gdrive, then remove the local file."""
    url          = entry["url"]
    display_name = entry["name"]
    size         = entry.get("size", "?")
    expected_sha = entry.get("sha256")
    remote_name  = get_remote_name()

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

    discord_notify(f"**fetching**: {display_name} ({size}) in `{category}`", 0x3498db)
    
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
        subprocess.run(cmd, check=True, timeout=3600)
        
        # checksum verification
        if expected_sha:
            print(f"{c}[ verify ]{w} checking sha256...")
            actual_sha = calculate_sha256(local_file)
            if actual_sha.lower() != expected_sha.lower():
                raise ValueError(f"checksum mismatch! expected {expected_sha}, got {actual_sha}")
            print(f"{g}[ verify ]{w} hash matches.")

        print(f"{c}[ sync ]{w} uploading -> {remote_name}:{remote_folder}/{category}/")
        subprocess.run([
            "rclone", "move", "-P",
            local_file,
            f"{remote_name}:{remote_folder}/{category}/",
        ], check=True, timeout=7200)
        
        print(f"{g}[ ok ]{w} {display_name} secured.")
        discord_notify(f"**secured**: {display_name} ({size})\ndestination: `{category}`", 0x2ecc71)

    except Exception as e:
        error_msg = f"**error**: {display_name}\n`{e}`"
        print(f"{r}[ error ]{w} {display_name}: {e}")
        discord_notify(error_msg, 0xe74c3c)
        raise
    finally:
        if os.path.exists(local_file):
            os.remove(local_file)
        try:
            os.rmdir(local_dir)
        except OSError:
            pass

if __name__ == "__main__":
    current_remote = get_remote_name()
    total_isos = sum(len(v) for v in DB.values())
    cats_count = len(DB)
    
    print(f"{c}[ info ]{w} {total_isos} isos across {cats_count} categories")
    print(f"{c}[ info ]{w} remote: {current_remote}:{remote_folder}")
    print()

    for cat, entries in DB.items():
        print(f"{y}-- {cat} ({len(entries)}) --{w}")
        for entry in entries:
            dl(entry, cat)

    print(f"\n{g}[ done ]{w} all entries processed.")
    discord_notify(f"**sync session complete**\ntotal isos processed: {total_isos}", 0x9b59b6)
