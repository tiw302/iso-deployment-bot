# updated 2026-05-09

import os
import sys
import datetime

# setup path to import distros from parent directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))
from distros import DB

GDRIVE_LIBRARY_URL = "https://drive.google.com/drive/folders/1B64Y44QVMlgoVm49PRk2_UvPXRzXNZ8e?usp=sharing"

ASCII_ART = r"""
  _      _____  _   _ _    _ __   __  _____  _____  _____   _____  ____  
 | |    |_   _|| \ | |\ \  / /\ \ / / |  _  ||  ___||  __ \ |_   _|/ ___| 
 | |      | |  |  \| | \ \/ /  \ V /  | | | || |___ | |__) |  | |  \___ \ 
 | |___  _| |_ | |\  |  |  |    | |   | |_| ||  ___||  _  /  _| |_  ___) |
 |_____||_____||_| \_|  |__|    |_|   |_____||_|    |_| \_\ |_____||____/ 
                                                                           
"""

def generate_html():
    """generate a static index.html dashboard with raw terminal style."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(os.path.dirname(script_dir))
    output_path = os.path.join(root_dir, "web", "index.html")
    
    total_isos = sum(len(v) for v in DB.values())
    
    def parse_size(size_str):
        if not size_str: return 0
        try:
            num = float(''.join(c for c in size_str if c.isdigit() or c == '.'))
            if 'GB' in size_str: return num
            if 'MB' in size_str: return num / 1024
        except: pass
        return 0

    total_size_gb = sum(parse_size(entry.get('size')) for cat in DB.values() for entry in cat)
    last_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    html_template = f"""<!DOCTYPE html>
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
        <pre class="ascii-art">{ASCII_ART}</pre>
        
        <header>
            <div class="header-info">
                <div class="header-left">
                    <h1>os-deployment-library</h1>
                    <div class="stats">
                        &gt; status: active<br>
                        &gt; total_isos: {{total_isos}}<br>
                        &gt; storage_est: {{total_size_gb:.1f}} gb
                    </div>
                </div>
                <div class="header-right">
                    <a href="{{GDRIVE_LIBRARY_URL}}" target="_blank" class="btn-gdrive">
                        [ browse_google_drive ]
                    </a>
                </div>
            </div>
        </header>

        <div class="search-container">
            <input type="text" id="searchInput" placeholder="user@linux:~$ search _" class="search-input">
        </div>

        <div id="content">
            {{generate_sections(DB)}}
        </div>

        <footer>
            <p>system_generated: {{last_updated}}</p>
            <p>
                <a href="https://github.com/tiw302/os-deployment-library">github</a> | 
                <a href="https://instagram.com/tiw3025k_">instagram</a>
            </p>
        </footer>
    </div>
    <script src="assets/script.js"></script>
</body>
</html>"""
    
    final_html = html_template.replace("{{total_isos}}", str(total_isos)) \
                             .replace("{{total_size_gb:.1f}}", f"{total_size_gb:.1f}") \
                             .replace("{{generate_sections(DB)}}", generate_sections(DB)) \
                             .replace("{{last_updated}}", last_updated) \
                             .replace("{{GDRIVE_LIBRARY_URL}}", GDRIVE_LIBRARY_URL)
    
    with open(output_path, "w") as f:
        f.write(final_html)
    print(f"dashboard generated: {output_path}")

def generate_sections(db):
    sections = ""
    for category in sorted(db.keys()):
        entries = db[category]
        cat_name = category.replace('linux/', '').replace('-', ' ').lower()
        sections += f"""
        <section class="category-section">
            <div class="category-title">
                {cat_name} ({len(entries)})
            </div>
            <div class="grid">
                {generate_cards(entries)}
            </div>
        </section>"""
    return sections

def generate_cards(entries):
    cards = ""
    for entry in entries:
        name = entry.get('name', 'unknown').lower()
        size = entry.get('size', '?.? gb').lower()
        url = entry.get('url', '#')
        cards += f"""
        <div class="iso-card" data-name="{name}">
            <div class="iso-info">
                <div class="iso-name">{name}</div>
                <div class="iso-size">{size}</div>
            </div>
            <a href="{url}" target="_blank" class="external-link">
                <i class="fas fa-link"></i>
            </a>
        </div>"""
    return cards

if __name__ == "__main__":
    generate_html()
