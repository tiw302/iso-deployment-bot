# updated 2026-05-09

import os
import sys
import datetime

# setup path to import distros from parent directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))
from distros import DB

def generate_html():
    """generate a static index.html dashboard with separate css."""
    # write to the project root directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(os.path.dirname(script_dir))
    output_path = os.path.join(root_dir, "index.html")
    
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
    <title>OS Deployment Library</title>
    <link rel="stylesheet" href="assets/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="container">
        <header>
            <div>
                <h1>OS Deployment Library</h1>
                <p class="subtitle">automated iso mirroring & distribution system</p>
            </div>
            <div class="stats-group">
                <div class="stat-box">
                    <div class="stat-label">total isos</div>
                    <div class="stat-value">{total_isos}</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">est. size</div>
                    <div class="stat-value">{total_size_gb:.1f} gb</div>
                </div>
            </div>
        </header>

        <div class="search-container">
            <i class="fas fa-search search-icon"></i>
            <input type="text" id="searchInput" placeholder="search distributions..." class="search-input">
        </div>

        <div id="content">
            {generate_sections(DB)}
        </div>

        <footer>
            <p>generated on {last_updated} • open source education</p>
            <div class="footer-links">
                <a href="https://github.com/tiw302/os-deployment-library"><i class="fab fa-github"></i> github</a>
                <a href="https://instagram.com/tiw3025k_"><i class="fab fa-instagram"></i> instagram</a>
            </div>
        </footer>
    </div>

    <script>
        const searchInput = document.getElementById('searchInput');
        const sections = document.querySelectorAll('.category-section');

        searchInput.addEventListener('input', (e) => {{
            const term = e.target.value.toLowerCase();
            sections.forEach(section => {{
                let hasMatch = false;
                const cards = section.querySelectorAll('.iso-card');
                cards.forEach(card => {{
                    const name = card.dataset.name.toLowerCase();
                    if (name.includes(term)) {{
                        card.style.display = 'flex';
                        hasMatch = true;
                    }} else {{
                        card.style.display = 'none';
                    }}
                }});
                section.style.display = hasMatch ? 'block' : 'none';
            }});
        }});
    </script>
</body>
</html>"""
    
    with open(output_path, "w") as f:
        f.write(html_template)
    print(f"dashboard generated: {output_path}")

def generate_sections(db):
    sections = ""
    for category in sorted(db.keys()):
        entries = db[category]
        cat_name = category.replace('linux/', '').replace('-', ' ').lower()
        sections += f"""
        <section class="category-section">
            <div class="category-title">
                <div class="category-indicator"></div>
                {cat_name}
                <span class="category-count">({len(entries)} items)</span>
            </div>
            <div class="grid">
                {generate_cards(entries)}
            </div>
        </section>"""
    return sections

def generate_cards(entries):
    cards = ""
    for entry in entries:
        name = entry.get('name', 'unknown')
        size = entry.get('size', '?.? gb')
        url = entry.get('url', '#')
        cards += f"""
        <div class="iso-card" data-name="{name}">
            <div class="iso-info">
                <div class="iso-name" title="{name}">{name}</div>
                <div class="iso-details">
                    <i class="fas fa-file-iso"></i> {size.lower()}
                </div>
            </div>
            <a href="{url}" target="_blank" class="external-link">
                <i class="fas fa-external-link-alt"></i>
            </a>
        </div>"""
    return cards

if __name__ == "__main__":
    generate_html()
