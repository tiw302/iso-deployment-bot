# updated 2026-05-09

import os
import sys
import datetime

# setup path to import distros from parent directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))
from distros import DB

def generate_html():
    """generate a static index.html dashboard for the iso collection."""
    output_path = os.path.join(os.path.dirname(script_dir), "index.html")
    
    total_isos = sum(len(v) for v in DB.values())
    categories = sorted(DB.keys())
    
    # helper for size calculation (rough estimate)
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
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {{ background-color: #0f172a; color: #e2e8f0; }}
        .glass {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); }}
        .search-input {{ background: #1e293b; border: 1px solid #334155; }}
        .search-input:focus {{ outline: none; border-color: #38bdf8; ring: 1px #38bdf8; }}
        .iso-card {{ transition: transform 0.2s, box-shadow 0.2s; }}
        .iso-card:hover {{ transform: translateY(-2px); box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); }}
    </style>
</head>
<body class="min-h-screen p-4 md:p-8">
    <div class="max-w-6xl mx-auto">
        <!-- Header -->
        <header class="mb-8 flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
                <h1 class="text-3xl font-bold text-sky-400"><i class="fas fa-server mr-2"></i>OS Deployment Library</h1>
                <p class="text-slate-400 mt-1">Automated ISO Mirroring & Distribution System</p>
            </div>
            <div class="flex gap-4">
                <div class="glass p-3 rounded-lg text-center min-w-[100px]">
                    <div class="text-xs text-slate-400 uppercase font-bold">Total ISOs</div>
                    <div class="text-xl font-mono text-white">{total_isos}</div>
                </div>
                <div class="glass p-3 rounded-lg text-center min-w-[100px]">
                    <div class="text-xs text-slate-400 uppercase font-bold">Est. Size</div>
                    <div class="text-xl font-mono text-white">{total_size_gb:.1f} GB</div>
                </div>
            </div>
        </header>

        <!-- Search & Stats -->
        <div class="mb-6 relative">
            <i class="fas fa-search absolute left-4 top-1/2 -translate-y-1/2 text-slate-500"></i>
            <input type="text" id="searchInput" placeholder="Search distributions (e.g. ubuntu, arch, proxmox)..." 
                   class="w-full pl-12 pr-4 py-3 rounded-xl search-input text-lg">
        </div>

        <!-- Main Content -->
        <div id="content">
            {generate_sections(DB)}
        </div>

        <footer class="mt-12 pt-8 border-t border-slate-800 text-center text-slate-500 text-sm">
            <p>Generated on {last_updated} • Built with <i class="fas fa-heart text-red-500"></i> for Open Source Education</p>
            <div class="mt-2 space-x-4">
                <a href="https://github.com/tiw302/os-deployment-library" class="hover:text-sky-400"><i class="fab fa-github"></i> GitHub</a>
                <a href="https://instagram.com/tiw3025k_" class="hover:text-sky-400"><i class="fab fa-instagram"></i> Instagram</a>
            </div>
        </footer>
    </div>

    <script>
        const searchInput = document.getElementById('searchInput');
        const sections = document.querySelectorAll('.category-section');
        const cards = document.querySelectorAll('.iso-card');

        searchInput.addEventListener('input', (e) => {{
            const term = e.target.value.toLowerCase();
            
            sections.forEach(section => {{
                let hasMatch = false;
                const sectionCards = section.querySelectorAll('.iso-card');
                
                sectionCards.forEach(card => {{
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
        cat_name = category.replace('linux/', '').replace('-', ' ').title()
        
        sections += f"""
        <section class="category-section mb-10">
            <h2 class="text-xl font-bold mb-4 flex items-center text-slate-300">
                <span class="w-2 h-6 bg-sky-500 rounded-full mr-3"></span>
                {cat_name}
                <span class="ml-3 text-sm font-normal text-slate-500">({len(entries)} items)</span>
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {generate_cards(entries)}
            </div>
        </section>"""
    return sections

def generate_cards(entries):
    cards = ""
    for entry in entries:
        name = entry.get('name', 'Unknown')
        size = entry.get('size', '?.? GB')
        url = entry.get('url', '#')
        
        cards += f"""
        <div class="glass p-4 rounded-xl iso-card flex justify-between items-center" data-name="{name}">
            <div class="overflow-hidden">
                <div class="font-medium text-white truncate pr-2" title="{name}">{name}</div>
                <div class="text-xs text-slate-400 flex items-center mt-1">
                    <i class="fas fa-file-iso mr-1.5"></i> {size}
                </div>
            </div>
            <a href="{url}" target="_blank" class="text-sky-500 hover:text-sky-400 p-2 hover:bg-sky-500/10 rounded-lg transition-colors">
                <i class="fas fa-external-link-alt"></i>
            </a>
        </div>"""
    return cards

if __name__ == "__main__":
    generate_html()
