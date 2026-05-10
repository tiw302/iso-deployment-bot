# link checker for os-deployment-library (no dependencies version)

import os
import sys
import urllib.request
import urllib.error
import time
from concurrent.futures import ThreadPoolExecutor

# setup path to import distros from parent directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))
from distros import DB

c, g, r, y, w = '\033[96m', '\033[92m', '\033[91m', '\033[93m', '\033[0m'

def check_link(category, entry):
    name = entry.get('name', 'unknown')
    url = entry.get('url')
    
    if not url or url == '#':
        return 'missing', category, name, url

    try:
        req = urllib.request.Request(url, method='HEAD')
        req.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status < 400:
                return 'ok', category, name, url
            return f'error {response.status}', category, name, url
    except urllib.error.HTTPError as e:
        # Some servers return 403/405 for HEAD, try a GET with Range
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0')
            req.add_header('Range', 'bytes=0-0')
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status < 400:
                    return 'ok', category, name, url
                return f'error {response.status}', category, name, url
        except Exception as e2:
            return f'error {e.code}', category, name, url
    except Exception as e:
        return f'failed', category, name, url

def main():
    all_entries = []
    for cat, entries in DB.items():
        for entry in entries:
            all_entries.append((cat, entry))
    
    total = len(all_entries)
    print(f"{c}[ info ]{w} checking {total} links (using threads)...")
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_link, cat, entry) for cat, entry in all_entries]
        results = [f.result() for f in futures]
    
    end_time = time.time()
    
    broken = [res for res in results if res[0] != 'ok']
    
    print(f"\n{g}[ done ]{w} check completed in {end_time - start_time:.1f}s")
    print(f"{c}[ stats ]{w} total: {total} | ok: {total - len(broken)} | {r}broken: {len(broken)}{w}")
    
    if broken:
        print(f"\n{r}--- dead links report ---{w}")
        for status, cat, name, url in broken:
            print(f"{r}[ {status:10} ]{w} {cat} -> {name}")
            
        with open("broken_links.log", "w") as f:
            f.write(f"broken links report - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*50 + "\n")
            for status, cat, name, url in broken:
                f.write(f"[{status}] {cat} | {name}\nURL: {url}\n\n")
        print(f"\n{c}[ info ]{w} full report saved to broken_links.log")
    else:
        print(f"{g}[ ok ]{w} no broken links found!")

if __name__ == "__main__":
    main()
