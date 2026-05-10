# fetch top distros from distrowatch

import urllib.request
import re
import os
import json

def fetch_top_distros(limit=100):
    print(f"fetching top {limit} distros from distrowatch...")
    url = "https://distrowatch.com/dwres.php?resource=popularity"
    
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
        # simpler regex to catch distro names from the ranking table
        # pattern matches: <td class="phr2"><a href="distro_name">Distro Name</a></td>
        matches = re.findall(r'<td class="phr2"><a href="([^"]+)">([^<]+)</a></td>', html)
        
        top_list = []
        for i, (slug, name) in enumerate(matches[:limit]):
            # DistroWatch links look like distrowatch.com/ubuntu
            # We can point to their info page or try to guess their site.
            # Pointing to DistroWatch info page is safer as it contains all official links.
            top_list.append({
                "rank": i + 1,
                "name": name,
                "url": f"https://distrowatch.com/table.php?distribution={slug}",
                "description": f"ranked #{i+1} on distrowatch"
            })
            
        return top_list
    except Exception as e:
        print(f"error fetching from distrowatch: {e}")
        # fallback curated list if scraping fails
        return [
            {"rank": 1, "name": "MX Linux", "url": "https://mxlinux.org/"},
            {"rank": 2, "name": "Linux Mint", "url": "https://linuxmint.com/"},
            {"rank": 3, "name": "EndeavourOS", "url": "https://endeavouros.com/"},
            {"rank": 4, "name": "Debian", "url": "https://www.debian.org/"},
            {"rank": 5, "name": "Ubuntu", "url": "https://ubuntu.com/"},
            {"rank": 6, "name": "Fedora", "url": "https://getfedora.org/"},
            {"rank": 7, "name": "Manjaro", "url": "https://manjaro.org/"},
            {"rank": 8, "name": "Pop!_OS", "url": "https://pop.system76.com/"},
            {"rank": 9, "name": "openSUSE", "url": "https://www.opensuse.org/"},
            {"rank": 10, "name": "Zorin OS", "url": "https://zorin.com/os/"}
        ]

if __name__ == "__main__":
    top_distros = fetch_top_distros(100)
    output_path = os.path.join(os.path.dirname(__file__), "top_distros.json")
    with open(output_path, "w") as f:
        json.dump(top_distros, f, indent=4)
    print(f"saved {len(top_distros)} distros to {output_path}")
