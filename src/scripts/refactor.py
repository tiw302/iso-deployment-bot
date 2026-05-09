# updated 2026-05-09

import ast
import re
import os

def process_dict_node(dict_node, db_dict):
    if isinstance(dict_node, ast.Dict):
        for key_node, value_node in zip(dict_node.keys, dict_node.values):
            if hasattr(ast, 'Constant') and isinstance(key_node, ast.Constant):
                key = key_node.value
            elif hasattr(ast, 'Str') and isinstance(key_node, ast.Str):
                key = key_node.s
            else:
                continue
            
            # parse value_node list
            entries = []
            if isinstance(value_node, ast.List):
                for elt in value_node.elts:
                    if isinstance(elt, ast.Dict):
                        entry = {}
                        for k, v in zip(elt.keys, elt.values):
                            if hasattr(ast, 'Constant') and isinstance(k, ast.Constant):
                                k_val = k.value
                            elif hasattr(ast, 'Str') and isinstance(k, ast.Str):
                                k_val = k.s
                            else: continue
                            
                            if hasattr(ast, 'Constant') and isinstance(v, ast.Constant):
                                v_val = v.value
                            elif hasattr(ast, 'Str') and isinstance(v, ast.Str):
                                v_val = v.s
                            else: continue
                            
                            entry[k_val] = v_val
                        entries.append(entry)
            
            if key not in db_dict:
                db_dict[key] = []
            db_dict[key].extend(entries)

def refactor_distros():
    # define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    distros_path = os.path.join(base_dir, 'distros.py')
    
    if not os.path.exists(distros_path):
        print(f"error: {distros_path} not found")
        return

    with open(distros_path, 'r') as f:
        content = f.read()

    # use ast to parse the file
    tree = ast.parse(content)
    
    db_dict = {}
    
    # find the db assignment
    for node in tree.body:
        # handle regular assignment: db = { ... }
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id.upper() == 'DB':
                    process_dict_node(node.value, db_dict)
        # handle annotated assignment: db: dict = { ... }
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id.upper() == 'DB':
                process_dict_node(node.value, db_dict)

    if not db_dict:
        print("error: db variable not found in distros.py")
        return

    # de-duplicate entries by url
    url_to_entry = {}
    for key, entries in db_dict.items():
        for entry in entries:
            url = entry.get('url')
            if not url: continue
            if url not in url_to_entry:
                url_to_entry[url] = entry
            else:
                # keep the one with the longer name for better description
                if len(entry.get('name', '')) > len(url_to_entry[url].get('name', '')):
                    url_to_entry[url] = entry
                # keep size if available
                if 'size' in entry and 'size' not in url_to_entry[url]:
                    url_to_entry[url]['size'] = entry['size']

    # rebuild db with unique urls
    best_entries = url_to_entry
    new_db_dict = {}
    seen_urls = set()
    
    # preserve category assignment
    for key in db_dict.keys():
        new_db_dict[key] = []
        for entry in db_dict[key]:
            url = entry.get('url')
            if url and url not in seen_urls:
                new_db_dict[key].append(best_entries[url])
                seen_urls.add(url)
    
    # remove empty categories
    new_db_dict = {k: v for k, v in new_db_dict.items() if v}

    # reorganize categories
    category_order = [
        "linux/ubuntu", "linux/ubuntu-noble", "linux/ubuntu-plucky", "linux/ubuntu-jammy",
        "linux/debian", "linux/debian-based", "linux/mint",
        "linux/arch-family",
        "linux/enterprise", "linux/server", "linux/server-cloud", "linux/fedora-spins",
        "linux/gaming",
        "linux/security", "linux/pentesting", "linux/forensic", "linux/privacy",
        "linux/immutable", "linux/wayland-tiling", "linux/rolling",
        "linux/lightweight", "linux/minimal",
        "homelab", "homelab/virtualization", "homelab/nas",
        "specialized/vintage", "specialized/containers", "specialized/risc-emulation",
        "recovery/tools", "recovery/backup",
        "arm/raspberry-pi", "arm/sbc",
        "windows/eval",
        "android-x86", "chromeos",
        "alternative/bsd",
        "linux/ai-ml", "linux/developer", "linux/desktop-env", "linux/embedded", "linux/specialized", "linux/office", "linux/hardware", "linux/live-tools", "linux/education", "linux/scientific", "linux/legacy", "linux/others", "linux/experimental", "linux/alternative-arch"
    ]
    
    sorted_keys = []
    for cat in category_order:
        if cat in new_db_dict:
            sorted_keys.append(cat)
    for cat in sorted(new_db_dict.keys()):
        if cat not in sorted_keys:
            sorted_keys.append(cat)

    # map keys to simple english names
    category_names = {
        "linux/ubuntu": "ubuntu",
        "linux/ubuntu-noble": "ubuntu 24.04 noble",
        "linux/ubuntu-plucky": "ubuntu 25.04 plucky",
        "linux/ubuntu-jammy": "ubuntu 22.04 jammy",
        "linux/debian": "debian",
        "linux/debian-based": "debian derivatives",
        "linux/mint": "linux mint",
        "linux/arch-family": "arch family",
        "linux/enterprise": "enterprise / rpm",
        "linux/server": "server",
        "linux/server-cloud": "server & cloud",
        "linux/fedora-spins": "fedora spins & labs",
        "linux/gaming": "gaming",
        "linux/security": "security",
        "linux/pentesting": "pentesting & red team",
        "linux/forensic": "forensic & digital investigation",
        "linux/privacy": "privacy & security focused",
        "linux/immutable": "immutable / atomic desktops",
        "linux/wayland-tiling": "wayland / tiling wm",
        "linux/rolling": "rolling release",
        "linux/lightweight": "lightweight",
        "linux/minimal": "minimal & diy",
        "homelab": "homelab",
        "homelab/virtualization": "virtualization",
        "homelab/nas": "nas",
        "specialized/vintage": "vintage / novelty / retro",
        "specialized/containers": "containers & cloud native",
        "specialized/risc-emulation": "risc / emulation / research",
        "recovery/tools": "recovery & rescue tools",
        "recovery/backup": "backup & recovery",
        "arm/raspberry-pi": "raspberry pi",
        "arm/sbc": "arm / sbc",
        "windows/eval": "windows evaluation",
        "android-x86": "android-x86",
        "chromeos": "chromeos",
        "alternative/bsd": "bsd / alternative",
        "linux/ai-ml": "ai / machine learning",
        "linux/developer": "developer tools",
        "linux/desktop-env": "desktop environments",
        "linux/embedded": "embedded & iot",
        "linux/specialized": "specialized / custom",
        "linux/office": "office & productivity",
        "linux/hardware": "hardware specific",
        "linux/live-tools": "live usb tools",
        "linux/education": "education & learning",
        "linux/scientific": "scientific & data science",
        "linux/legacy": "legacy / old stable",
        "linux/others": "other distributions",
        "linux/experimental": "experimental",
        "linux/alternative-arch": "alternative architectures"
    }

    # generate new file content
    new_content = "# updated 2026-05\n\nDB: dict[str, list[dict]] = {\n"
    
    for i, key in enumerate(sorted_keys):
        cat_name = category_names.get(key, key.replace('linux/', '').replace('-', ' ').lower())
        new_content += f"\n    # {cat_name}\n"
        new_content += f"    \"{key}\": [\n"
        for entry in new_db_dict[key]:
            line = f"        {{\"name\": \"{entry.get('name', '')}\", \"url\": \"{entry.get('url', '')}\""
            if 'size' in entry:
                line += f", \"size\": \"{entry['size']}\""
            line += "},"
            new_content += line + "\n"
        new_content += "    ]"
        if i < len(sorted_keys) - 1:
            new_content += ",\n"
        else:
            new_content += "\n"
            
    new_content += "}\n\n"
    new_content += "total = sum(len(v) for v in DB.values())\n"
    new_content += "print(f\"refactor complete: total {total} entries\")\n"

    with open(distros_path, 'w') as f:
        f.write(new_content)

if __name__ == '__main__':
    refactor_distros()
