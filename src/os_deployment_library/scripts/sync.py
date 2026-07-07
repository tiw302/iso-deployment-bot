# sync.py
#
# core synchronization script for the os deployment library.
# downloads missing iso files via aria2 and uploads them to google drive via rclone.

import os
import subprocess
import hashlib
import json
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import urllib.error

# setup path to import distros from parent dir
script_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(script_dir))
from os_deployment_library.distros import DB
from os_deployment_library.scripts.utils import resolve_filename

c, g, r, y, w = '\033[96m', '\033[92m', '\033[91m', '\033[93m', '\033[0m'
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

def discord_notify(message: str, color: int = 0x3498db):
    """send notification to discord webhook"""
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
        # set 10s timeout to prevent blocking if webhook hangs
        with urlopen(req, timeout=10) as res:
            pass
    except urllib.error.URLError as e:
        print(f"{r}[ discord error ]{w} {e}")

def get_remote_name() -> str:
    """get remote name from rclone config"""
    try:
        result = subprocess.run(["rclone", "listremotes"], capture_output=True, text=True, check=True)
        remotes = [r.strip().rstrip(':') for r in result.stdout.strip().split('\n') if r.strip()]
        if remotes:
            return remotes[0]
    except Exception:
        pass
    return "gdrive" # fallback default

def calculate_sha256(file_path: str) -> str:
    """calc sha256 checksum of a file"""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # read in 64kb chunks for better performance with large isos
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def get_existing_files(remote_name: str) -> set:
    """pre-fetch all file paths in the remote folder to avoid O(N) rclone checks"""
    try:
        print(f"{c}[ info ]{w} pre-fetching existing files from {remote_name}:{remote_folder}...")
        res = subprocess.run(
            ["rclone", "lsf", f"{remote_name}:{remote_folder}", "-R", "--files-only"],
            capture_output=True, text=True, timeout=120
        )
        if res.returncode == 0:
            # map files by category/filename path
            files = {line.strip() for line in res.stdout.strip().split('\n') if line.strip()}
            print(f"{g}[ info ]{w} found {len(files)} existing files in storage.")
            return files
    except Exception as e:
        print(f"{y}[ warning ]{w} failed to pre-fetch drive file list: {e}")
    return set()

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

def remove_empty_parents(path: str, stop_at_dir: str = "./temp"):
    """recursively remove empty parent directories up to stop_at_dir."""
    path = os.path.abspath(path)
    stop_at_dir = os.path.abspath(stop_at_dir)
    # prevent walking up beyond stop_at_dir
    if not path.startswith(stop_at_dir):
        return
    while path != stop_at_dir and os.path.isdir(path):
        try:
            os.rmdir(path)
            path = os.path.dirname(path)
        except OSError:
            break

def dl(entry: dict, category: str, existing_files: set, remote_name: str):
    """download one iso, upload to gdrive, then delete local file"""
    url          = entry["url"]
    display_name = entry["name"]
    size         = entry.get("size", "?")
    expected_sha = entry.get("sha256")

    filename = resolve_filename(url)

    local_dir  = f"./temp/{category}"
    local_file = os.path.join(local_dir, filename)

    print(f"\n{c}[ check  ]{w} {display_name}  ({size})")

    # check if file exists in our pre-fetched set
    remote_rel_path = f"{category}/{filename}"
    if remote_rel_path in existing_files:
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

        # verify checksum
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

    except (subprocess.CalledProcessError, ValueError, OSError) as e:
        error_msg = f"**error**: {display_name}\n`{e}`"
        print(f"{r}[ error ]{w} {display_name}: {e}")
        discord_notify(error_msg, 0xe74c3c)
    finally:
        if os.path.exists(local_file):
            os.remove(local_file)
        # remove left-over aria2 control files to clean temp directory
        aria_control = local_file + ".aria2"
        if os.path.exists(aria_control):
            try:
                os.remove(aria_control)
            except OSError:
                pass
        remove_empty_parents(local_dir)

if __name__ == "__main__":
    current_remote = get_remote_name()
    existing_files = get_existing_files(current_remote)
    total_isos = sum(len(v) for v in DB.values())
    cats_count = len(DB)

    print(f"{c}[ info ]{w} {total_isos} isos across {cats_count} categories")
    print(f"{c}[ info ]{w} remote: {current_remote}:{remote_folder}")
    print()

    for cat, entries in DB.items():
        print(f"{y}-- {cat} ({len(entries)}) --{w}")
        for entry in entries:
            dl(entry, cat, existing_files, current_remote)

    print(f"\n{g}[ done ]{w} all entries processed.")
    discord_notify(f"**sync session complete**\ntotal isos processed: {total_isos}", 0x9b59b6)
