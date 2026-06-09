import os
import sys
import json
import urllib.request
import urllib.error
from urllib.parse import urlparse

# Add src to python path to import DB
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(os.path.dirname(script_dir), "src")
# sys.path.append(src_dir)

try:
    from os_deployment_library.distros import DB
except ImportError:
    print("Error: Could not import DB from src/distros.py")
    sys.exit(1)

def guess_checksum_urls(iso_url):
    """Generate potential checksum URLs based on the ISO URL."""
    parsed = urlparse(iso_url)
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
    """Best-effort attempt to find a checksum for an ISO."""
    guesses = guess_checksum_urls(iso_url)

    for url in guesses:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    content = response.read().decode('utf-8', errors='ignore')
                    # Look for the filename in the checksum file
                    iso_filename = iso_url.rsplit('/', 1)[1]
                    for line in content.splitlines():
                        if iso_filename in line:
                            # Typically format is "hash  filename"
                            parts = line.split()
                            if len(parts) >= 1:
                                return {
                                    "hash": parts[0],
                                    "source": url
                                }
                    # If it's a direct file like .iso.sha256, it might just contain the hash
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

    for category, entries in DB.items():
        for entry in entries:
            processed += 1
            name = entry.get('name')
            url = entry.get('url')

            # Skip sourceforge download URLs as they redirect
            if "sourceforge.net" in url:
                print(f"[{processed}/{total}] Skipping {name} (SourceForge URL)")
                continue

            print(f"[{processed}/{total}] Checking {name}...")
            checksum_info = fetch_checksum(url)

            if checksum_info:
                print(f"  -> Found hash: {checksum_info['hash'][:16]}... from {checksum_info['source']}")
                results[name] = checksum_info
                found += 1
            else:
                print("  -> No standard checksum file found.")

    # Save results
    output_path = os.path.join(script_dir, "checksums_report.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)

    print(f"\nFinished. Found checksums for {found} out of {total} distros.")
    print(f"Report saved to {output_path}")

if __name__ == "__main__":
    main()
