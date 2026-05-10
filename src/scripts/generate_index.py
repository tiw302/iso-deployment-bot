# automated gdrive library generator (zero-config) with unified interaction

import os
import sys
import datetime
import subprocess
import re
import json
from urllib.parse import urlparse

# setup path to import distros from parent directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))
try:
    from distros import DB
except ImportError:
    DB = {}

GDRIVE_LIBRARY_URL = "https://drive.google.com/drive/folders/1B64Y44QVMlgoVm49PRk2_UvPXRzXNZ8e?usp=sharing"

ASCII_ART = r"""
  _      _____  _   _ _    _ __   __  _____  _____  _____   _____  ____  
 | |    |_   _|| \ | |\ \  / /\ \ / / |  _  ||  ___||  __ \ |_   _|/ ___| 
 | |      | |  |  \| | \ \/ /  \ V /  | | | || |___ | |__) |  | |  \___ \ 
 | |___  _| |_ | |\  |  |  |    | |   | |_| ||  ___||  _  /  _| |_  ___) |
 |_____||_____||_| \_|  |__|    |_|   |_____||_|    |_| \_\ |_____||____/ 
                                                                           
"""

def clean_filename(filename):
    name = os.path.splitext(filename)[0]
    if name.endswith('.img'): name = name[:-4]
    name = name.replace('-', ' ').replace('_', ' ').replace('.', ' ')
    name = re.sub(r'\b(amd64|x86_64|64bit|dvd|iso)\b', '', name, flags=re.IGNORECASE)
    name = ' '.join(name.split()).title()
    return name

def format_size(size_bytes):
    try:
        size = float(size_bytes)
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
    except:
        return "?.? GB"
    return "?.? GB"

def get_drive_content():
    library = {}
    try:
        remote_res = subprocess.run(["rclone", "listremotes"], capture_output=True, text=True)
        remotes = [r.strip().rstrip(':') for r in remote_res.stdout.strip().split('\n') if r.strip()]
        remote_name = remotes[0] if remotes else "gdrive"
        res = subprocess.run(
            ["rclone", "lsf", f"{remote_name}:os-deployment-library", "-R", "--format", "pis", "--files-only"],
            capture_output=True, text=True, timeout=120
        )
        if res.returncode == 0:
            for line in res.stdout.strip().split('\n'):
                if ';' not in line: continue
                parts = line.split(';')
                if len(parts) < 3: continue
                path, file_id, size = parts[0], parts[1], parts[2]
                if not any(path.lower().endswith(ext) for ext in ['.iso', '.img', '.gz', '.xz', '.zip', '.bin']):
                    continue
                category = os.path.dirname(path)
                if not category: category = "unsorted"
                filename = os.path.basename(path)
                pretty_name = clean_filename(filename)
                for cat_items in DB.values():
                    for item in cat_items:
                        if filename in item.get('url', ''):
                            pretty_name = item.get('name')
                            break
                if category not in library:
                    library[category] = []
                library[category].append({
                    "name": pretty_name, "filename": filename, "size": format_size(size), "id": file_id
                })
    except Exception as e:
        print(f"error scanning drive: {e}")
    return library

def load_massive_distros():
    path = os.path.join(os.path.dirname(__file__), "massive_distros_categorized.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def generate_html():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(os.path.dirname(script_dir))
    output_path = os.path.join(root_dir, "web", "index.html")
    library = get_drive_content()
    massive_dict = load_massive_distros()
    total_isos = sum(len(v) for v in library.values())
    massive_total = sum(len(v) for v in massive_dict.values())
    last_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>os-deployment-library</title>
    <link rel="stylesheet" href="assets/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="container">
        <pre class="ascii-art">ASCII_ART_PLACEHOLDER</pre>
        <header>
            <div class="header-info">
                <div class="header-left">
                    <h1>os-deployment-library</h1>
                    <div class="stats">
                        &gt; status: active<br>
                        &gt; secured: {{total_isos}} files<br>
                        &gt; discovery: {{massive_count}} distros
                    </div>
                </div>
                <div class="header-right">
                    <div class="tab-controls">
                        <button onclick="showTab('library')" class="tab-btn active" id="libTab">/library</button>
                        <button onclick="showTab('discovery')" class="tab-btn" id="discTab">/discovery</button>
                    </div>
                </div>
            </div>
        </header>
        <div class="search-container">
            <input type="text" id="searchInput" placeholder="user@linux:~$ search library _" class="search-input">
        </div>
        
        <div id="libraryContent" class="tab-content">
            <div class="nav-container">
                <div class="scroll-arrow left-arrow" id="libArrowLeft">&lt;</div>
                <div class="filter-nav" id="libNav">
                    {{library_nav}}
                </div>
                <div class="scroll-arrow right-arrow" id="libArrowRight">&gt;</div>
            </div>
            <div id="librarySections">
                {{library_sections}}
            </div>
        </div>
        
        <div id="discoveryContent" class="tab-content" style="display:none">
            <div class="nav-container">
                <div class="scroll-arrow left-arrow" id="discArrowLeft">&lt;</div>
                <div class="filter-nav" id="discNav">
                    {{discovery_nav}}
                </div>
                <div class="scroll-arrow right-arrow" id="discArrowRight">&gt;</div>
            </div>
            <div id="discoverySections">
                {{discovery_sections}}
            </div>
        </div>
        
        <footer>
            <p>system_last_sync: {{last_updated}}</p>
            <p><a href="https://github.com/tiw302/os-deployment-library">github</a> | <a href="https://instagram.com/tiw3025k_">instagram</a></p>
        </footer>
    </div>
    <script src="assets/script.js"></script>
    <script>
        function showTab(tab) {
            document.getElementById('libraryContent').style.display = tab === 'library' ? 'block' : 'none';
            document.getElementById('discoveryContent').style.display = tab === 'discovery' ? 'block' : 'none';
            document.getElementById('libTab').classList.toggle('active', tab === 'library');
            document.getElementById('discTab').classList.toggle('active', tab === 'discovery');
            const search = document.getElementById('searchInput');
            search.placeholder = tab === 'library' ? "user@linux:~$ search library _" : "user@linux:~$ search discovery _";
            updateArrows(tab === 'library' ? 'libNav' : 'discNav');
        }

        function filterContent(type, categoryId) {
            const sectionClass = type === 'lib' ? '.library-section' : '.discovery-section';
            const pillClass = type === 'lib' ? '.lib-pill' : '.disc-pill';
            const sections = document.querySelectorAll(sectionClass);
            const pills = document.querySelectorAll(pillClass);
            pills.forEach(p => p.classList.toggle('active', p.dataset.target === categoryId));
            sections.forEach(s => {
                if (categoryId === 'all') {
                    s.style.display = 'block';
                } else {
                    s.style.display = s.id === categoryId ? 'block' : 'none';
                }
            });
        }

        function updateArrows(navId) {
            const nav = document.getElementById(navId);
            const leftArrow = document.getElementById(navId === 'libNav' ? 'libArrowLeft' : 'discArrowLeft');
            const rightArrow = document.getElementById(navId === 'libNav' ? 'libArrowRight' : 'discArrowRight');
            if (!nav || !leftArrow || !rightArrow) return;
            const isScrollable = nav.scrollWidth > nav.clientWidth;
            if (!isScrollable) {
                leftArrow.style.display = 'none';
                rightArrow.style.display = 'none';
                return;
            }
            leftArrow.style.display = nav.scrollLeft > 5 ? 'flex' : 'none';
            rightArrow.style.display = (nav.scrollLeft + nav.clientWidth < nav.scrollWidth - 5) ? 'flex' : 'none';
        }

        ['libNav', 'discNav'].forEach(id => {
            const nav = document.getElementById(id);
            const leftArrow = document.getElementById(id === 'libNav' ? 'libArrowLeft' : 'discArrowLeft');
            const rightArrow = document.getElementById(id === 'libNav' ? 'libArrowRight' : 'discArrowRight');
            if (!nav) return;
            leftArrow.onclick = () => nav.scrollBy({left: -200, behavior: 'smooth'});
            rightArrow.onclick = () => nav.scrollBy({left: 200, behavior: 'smooth'});
            nav.addEventListener('wheel', (e) => {
                if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
                    e.preventDefault();
                    nav.scrollLeft += e.deltaY;
                }
            });
            nav.addEventListener('scroll', () => updateArrows(id));
            setTimeout(() => updateArrows(id), 100);
        });

        window.addEventListener('resize', () => {
            updateArrows('libNav');
            updateArrows('discNav');
        });
    </script>
</body>
</html>"""
    
    # Generate Library Section
    lib_sections = ""
    lib_nav = f'<button onclick="filterContent(\'lib\', \'all\')" class="filter-pill lib-pill active" data-target="all">all_files ({total_isos})</button>'
    sorted_lib_cats = sorted(library.keys())
    for i, cat in enumerate(sorted_lib_cats):
        items = library[cat]
        cat_id = f"lib_cat_{i}"
        cat_display = cat.replace('/', ' > ').lower()
        lib_nav += f'<button onclick="filterContent(\'lib\', \'{cat_id}\')" class="filter-pill lib-pill" data-target="{cat_id}">{cat_display} ({len(items)})</button>'
        cards = ""
        for item in items:
            gdrive_url = f"https://drive.google.com/uc?export=download&id={item['id']}"
            cards += f'<div class="iso-card secured" data-name="{item["name"].lower()}"><div class="iso-info"><div class="iso-name">{item["name"]} <span class="status-secured">✓</span></div><div class="iso-size">{item["size"]}</div></div><div class="iso-actions"><a href="{gdrive_url}" target="_blank" class="btn-download btn-gdrive-dl">download</a></div></div>'
        lib_sections += f'<section class="category-section library-section" id="{cat_id}"><div class="category-title">{cat_display} ({len(items)})</div><div class="grid">{cards}</div></section>'

    # Generate Discovery Section
    disc_sections = ""
    disc_nav = f'<button onclick="filterContent(\'disc\', \'all\')" class="filter-pill disc-pill active" data-target="all">all_distros ({massive_total})</button>'
    sorted_disc_cats = sorted(massive_dict.keys(), key=lambda k: len(massive_dict[k]), reverse=True)
    for i, cat in enumerate(sorted_disc_cats):
        distros = massive_dict[cat]
        cat_id = f"disc_cat_{i}"
        disc_nav += f'<button onclick="filterContent(\'disc\', \'{cat_id}\')" class="filter-pill disc-pill" data-target="{cat_id}">{cat.lower()} ({len(distros)})</button>'
        disc_cards = ""
        for distro in distros:
            disc_cards += f'<div class="iso-card discovery-card" data-name="{distro["name"].lower()}"><div class="iso-info"><div class="iso-name">{distro["name"]}</div><div class="iso-size">encyclopedia</div></div><div class="iso-actions"><a href="{distro["url"]}" target="_blank" class="btn-download btn-source-dl">wiki</a></div></div>'
        disc_sections += f'<section class="category-section discovery-section" id="{cat_id}"><div class="category-title">{cat.lower()} ({len(distros)})</div><div class="grid discovery-grid">{disc_cards}</div></section>'

    final_html = html_template.replace("ASCII_ART_PLACEHOLDER", ASCII_ART) \
                             .replace("{{total_isos}}", str(total_isos)) \
                             .replace("{{massive_count}}", str(massive_total)) \
                             .replace("{{library_nav}}", lib_nav) \
                             .replace("{{library_sections}}", lib_sections) \
                             .replace("{{discovery_nav}}", disc_nav) \
                             .replace("{{discovery_sections}}", disc_sections) \
                             .replace("{{last_updated}}", last_updated)
    
    with open(output_path, "w") as f:
        f.write(final_html)
    print(f"dashboard regenerated: {total_isos} library files + {massive_total} discovery entries.")

if __name__ == "__main__":
    generate_html()
