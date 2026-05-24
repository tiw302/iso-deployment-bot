# database cleanup script

import os
import sys
import urllib.request
import urllib.error
import subprocess
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

# setup path to import distros from parent directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))
from distros import DB

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
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename or "." not in filename:
        filename = url.split("/")[-1].split("?")[0]
    if "." not in filename:
        filename += ".iso"
    if filename.endswith(".img"):
        filename = filename.replace(".img", ".img.iso")
    return filename

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

    print(f"\ncleanup finished.")
    print(f"total checked: {total_checked}")
    print(f"kept: {total_checked - removed_count}")
    print(f"removed: {removed_count}")
    
    # write back to distros.py (simplified write)
    distros_path = os.path.join(os.path.dirname(script_dir), 'distros.py')
    with open(distros_path, 'w') as f:
        f.write("# updated auto-cleanup\n\nDB: dict[str, list[dict]] = {\n")
        for cat, entries in new_db.items():
            f.write(f"    \"{cat}\": [\n")
            for e in entries:
                line = f"        {{\"name\": \"{e['name']}\", \"url\": \"{e['url']}\""
                if 'size' in e: line += f", \"size\": \"{e['size']}\""
                line += "},"
                f.write(line + "\n")
            f.write("    ],\n")
        f.write("}\n\n")
        f.write("total = sum(len(v) for v in DB.values())\n")
        f.write("print(f\"refactor complete: total {total} entries\")\n")

    # update web
    print("\nupdating web dashboard...")
    base_dir = os.path.dirname(script_dir)
    generate_script = os.path.join(base_dir, "src", "scripts", "generate_index.py")
    subprocess.run(["python3", generate_script])

if __name__ == "__main__":
    main()
