# fetch_checksums.py
#
# best-effort checksum discovery tool.
# scans upstream download directories to find and extract sha256 hashes for the database.

import os
import sys
import json
import urllib.request
import urllib.error

# add src to python path to import db
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(os.path.dirname(script_dir), "src")
# sys.path.append(src_dir)

try:
    from os_deployment_library.distros import DB
    from os_deployment_library.scripts.utils import CATEGORY_ORDER
except ImportError:
    print("Error: Could not import DB from src/distros.py")
    sys.exit(1)

def guess_checksum_urls(iso_url):
    """generate potential checksum urls based on the iso url."""
    base_url = iso_url.rsplit('/', 1)[0]
    filename = iso_url.rsplit('/', 1)[1]

    guesses = [
        f"{iso_url}.sha256",
        f"{iso_url}.sha256sum",
        f"{iso_url}.sha512",
        f"{base_url}/SHA256SUMS",
        f"{base_url}/sha256sum.txt",
        f"{base_url}/CHECKSUM",
        f"{base_url}/CHECKSUMS",
    ]
    return guesses

def fetch_checksum(iso_url):
    """best-effort attempt to find a checksum for an iso."""
    guesses = guess_checksum_urls(iso_url)

    for url in guesses:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    content = response.read().decode('utf-8', errors='ignore')
                    # look for the filename in the checksum file
                    iso_filename = iso_url.rsplit('/', 1)[1]
                    for line in content.splitlines():
                        if iso_filename in line:
                            # typically format is "hash  filename"
                            parts = line.split()
                            if len(parts) >= 1:
                                return {
                                    "hash": parts[0],
                                    "source": url
                                }
                    # if it's a direct file like .iso.sha256, it might just contain the hash
                    if url.endswith(('.sha256', '.sha512')) and len(content.split()) == 1:
                        return {
                            "hash": content.strip(),
                            "source": url
                        }
        except urllib.error.URLError:
            continue
        except Exception:
            continue

    return None

def main():
    print("Starting best-effort checksum discovery...")
    results = {}
    total = sum(len(entries) for entries in DB.values())
    processed = 0
    found = 0
    updated_any = False

    for category, entries in DB.items():
        for entry in entries:
            processed += 1
            name = entry.get('name')
            url = entry.get('url')

            # skip sourceforge download urls as they redirect
            if "sourceforge.net" in url:
                print(f"[{processed}/{total}] Skipping {name} (SourceForge URL)")
                continue

            print(f"[{processed}/{total}] Checking {name}...")
            checksum_info = fetch_checksum(url)

            if checksum_info:
                print(f"  -> Found hash: {checksum_info['hash'][:16]}... from {checksum_info['source']}")
                results[name] = checksum_info
                found += 1

                # update checksum in the database
                entry["sha256"] = checksum_info["hash"]
                updated_any = True
            else:
                print("  -> No standard checksum file found.")

    # save results to report file
    output_path = os.path.join(script_dir, "checksums_report.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)

    print(f"\nFinished. Found checksums for {found} out of {total} distros.")
    print(f"Report saved to {output_path}")

    if updated_any:
        # write updated database back to distros.json
        print("\nwriting updates back to src/os_deployment_library/distros.json...")
        distros_json_path = os.path.join(os.path.dirname(script_dir), 'src', 'os_deployment_library', 'distros.json')

        # reorganize categories by category_order
        sorted_keys = []
        for cat in CATEGORY_ORDER:
            if cat in DB:
                sorted_keys.append(cat)
        for cat in sorted(DB.keys()):
            if cat not in sorted_keys:
                sorted_keys.append(cat)

        # rebuild ordered db dictionary
        ordered_db = {}
        for key in sorted_keys:
            ordered_db[key] = []
            for entry in DB[key]:
                # sort keys in each entry to keep name, url, size first
                ordered_entry = {}
                for k in ["name", "url", "size"]:
                    if k in entry:
                        ordered_entry[k] = entry[k]
                for k in entry:
                    if k not in ordered_entry:
                        ordered_entry[k] = entry[k]
                ordered_db[key].append(ordered_entry)

        with open(distros_json_path, 'w', encoding='utf-8') as f:
            json.dump(ordered_db, f, indent=4)

        # update web dashboard
        print("updating web dashboard...")
        base_dir = os.path.dirname(script_dir)
        generate_script = os.path.join(base_dir, "src", "os_deployment_library", "scripts", "generate_index.py")
        import subprocess
        env = os.environ.copy()
        env["PYTHONPATH"] = os.path.join(base_dir, "src")
        subprocess.run([sys.executable, generate_script], env=env)

if __name__ == "__main__":
    main()
