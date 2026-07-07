# cleanup_db.py
#
# database maintenance and validation tool.
# removes dead links, verifies url health concurrently, and formats the database.

import os
import urllib.request
import urllib.error
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

# setup path to import distros from parent directory
script_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.join(os.path.dirname(script_dir), "src"))
# sys.path.append(os.path.join(os.path.dirname(script_dir), "src", "scripts"))
import json
from os_deployment_library.distros import DB
from os_deployment_library.scripts.utils import resolve_filename, CATEGORY_ORDER

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
    except Exception:
        # try GET with range as fallback
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0')
            req.add_header('Range', 'bytes=0-0')
            with urllib.request.urlopen(req, timeout=5) as response:
                return response.status < 400
        except Exception:
            return False

def get_expected_filename(url):
    return resolve_filename(url)



def main():
    print("starting database cleanup...")

    drive_files = get_drive_files()
    print(f"found {len(drive_files)} files in gdrive.")

    # first collect all entries to check
    entries_to_check = []
    kept_by_drive = {}
    total_checked = 0

    for category, entries in DB.items():
        kept_by_drive[category] = []
        for entry in entries:
            total_checked += 1
            filename = get_expected_filename(entry['url'])
            if filename in drive_files:
                kept_by_drive[category].append(entry)
            else:
                entries_to_check.append((category, entry))

    print(f"checking {len(entries_to_check)} links in parallel...")

    def check_entry(item):
        category, entry = item
        working = is_link_working(entry['url'])
        return category, entry, working

    kept_by_link = {}
    removed_count = 0

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_entry, entries_to_check)
        for category, entry, working in results:
            if working:
                if category not in kept_by_link:
                    kept_by_link[category] = []
                kept_by_link[category].append(entry)
            else:
                removed_count += 1
                print(f"removing broken & unsynced: {entry['name']}          ")

    new_db = {}
    for category in DB.keys():
        entries = kept_by_drive.get(category, []) + kept_by_link.get(category, [])
        if entries:
            new_db[category] = entries

    print("\ncleanup finished.")
    print(f"total checked: {total_checked}")
    print(f"kept: {total_checked - removed_count}")
    print(f"removed: {removed_count}")

    # reorganize categories by CATEGORY_ORDER
    sorted_keys = []
    for cat in CATEGORY_ORDER:
        if cat in new_db:
            sorted_keys.append(cat)
    for cat in sorted(new_db.keys()):
        if cat not in sorted_keys:
            sorted_keys.append(cat)

    # rebuild ordered DB dictionary
    ordered_db = {}
    for key in sorted_keys:
        ordered_db[key] = []
        for entry in new_db[key]:
            # sort keys in each entry to keep name, url, size first
            ordered_entry = {}
            for k in ["name", "url", "size"]:
                if k in entry:
                    ordered_entry[k] = entry[k]
            for k in entry:
                if k not in ordered_entry:
                    ordered_entry[k] = entry[k]
            ordered_db[key].append(ordered_entry)

    # write back to distros.json
    distros_json_path = os.path.join(os.path.dirname(script_dir), 'src', 'os_deployment_library', 'distros.json')
    with open(distros_json_path, 'w', encoding='utf-8') as f:
        json.dump(ordered_db, f, indent=4)

    # update web
    print("\nupdating web dashboard...")
    base_dir = os.path.dirname(script_dir)
    generate_script = os.path.join(base_dir, "src", "os_deployment_library", "scripts", "generate_index.py")
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.join(base_dir, "src")
    subprocess.run([sys.executable, generate_script], env=env)

if __name__ == "__main__":
    main()
