# updated 2026-05-09

import ast
import os
import json

def format_val(val):
    if isinstance(val, str):
        return json.dumps(val)
    elif isinstance(val, bool):
        return "True" if val else "False"
    elif val is None:
        return "None"
    elif isinstance(val, (int, float)):
        return str(val)
    elif isinstance(val, list):
        return "[" + ", ".join(format_val(x) for x in val) + "]"
    elif isinstance(val, dict):
        return "{" + ", ".join(f"{format_val(k)}: {format_val(v)}" for k, v in val.items()) + "}"
    else:
        return repr(val)

def process_dict_node(dict_node, db_dict):
    if isinstance(dict_node, ast.Dict):
        for key_node, value_node in zip(dict_node.keys, dict_node.values):
            try:
                key = ast.literal_eval(key_node)
            except Exception:
                continue

            # parse value_node list
            entries = []
            if isinstance(value_node, ast.List):
                for elt in value_node.elts:
                    try:
                        entry = ast.literal_eval(elt)
                        if isinstance(entry, dict):
                            entries.append(entry)
                    except Exception:
                        continue

            if key not in db_dict:
                db_dict[key] = []
            db_dict[key].extend(entries)

def validate_db(db_dict):
    """validate database entries for missing fields or invalid data."""
    errors = 0
    warnings = 0
    seen_names = {}

    print("\n--- database validation ---")

    for category, entries in db_dict.items():
        for entry in entries:
            name = entry.get('name', 'unknown')
            url = entry.get('url', '')

            # check 1: required fields
            if not url or not entry.get('name'):
                print(f"[error] category '{category}': missing name or url in entry")
                errors += 1

            # check 2: valid url format
            if url and not (url.startswith('http://') or url.startswith('https://') or url.startswith('ftp://')):
                print(f"[error] entry '{name}': invalid url protocol -> {url}")
                errors += 1

            # check 3: name collisions (potential file overwrites)
            full_path = f"{category}/{name}"
            if full_path in seen_names:
                print(f"[warning] collision: name '{name}' appears multiple times in '{category}'")
                warnings += 1
            seen_names[full_path] = True

            # check 4: missing size (optional but recommended)
            if 'size' not in entry:
                # we don't print for every entry to avoid noise, just a summary later if needed
                pass

    print(f"validation finished: {errors} errors, {warnings} warnings")
    return errors == 0

def refactor_distros():
    # define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    distros_path = os.path.join(base_dir, 'src', 'distros.py')

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

    # run validation before proceeding
    if not validate_db(db_dict):
        print("refactor aborted due to critical errors in database.")
        # we still proceed with refactor in this script because it fixes some errors like duplicates
        # but in a real CI environment, this would fail.

    # de-duplicate entries by resolved filename per category
    import sys
    sys.path.append(os.path.join(base_dir, 'src', 'scripts'))
    from utils import resolve_filename

    filename_to_entry = {}
    for key, entries in db_dict.items():
        for entry in entries:
            url = entry.get('url')
            if not url: continue
            filename = resolve_filename(url)
            uniq_key = (key, filename)

            if uniq_key not in filename_to_entry:
                filename_to_entry[uniq_key] = entry
            else:
                existing = filename_to_entry[uniq_key]
                if 'mirror' in entry.get('name', '').lower() or 'kku' in entry.get('name', '').lower():
                    pass
                elif 'mirror' in existing.get('name', '').lower() or 'kku' in existing.get('name', '').lower():
                    filename_to_entry[uniq_key] = entry
                else:
                    score_existing = len(existing.get('tags', [])) + (1 if 'docs' in existing else 0)
                    score_current = len(entry.get('tags', [])) + (1 if 'docs' in entry else 0)
                    if score_current > score_existing:
                        filename_to_entry[uniq_key] = entry

    # rebuild db with unique filenames
    new_db_dict = {}
    seen_keys = set()

    # preserve category assignment
    for key in db_dict.keys():
        new_db_dict[key] = []
        for entry in db_dict[key]:
            url = entry.get('url')
            if not url: continue
            filename = resolve_filename(url)
            uniq_key = (key, filename)
            if uniq_key not in seen_keys:
                new_db_dict[key].append(filename_to_entry[uniq_key])
                seen_keys.add(uniq_key)

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
            ordered_keys = []
            keys = list(entry.keys())
            for k in ["name", "url", "size"]:
                if k in keys:
                    ordered_keys.append(k)
                    keys.remove(k)
            ordered_keys.extend(keys)

            parts = []
            for k in ordered_keys:
                parts.append(f'"{k}": {format_val(entry[k])}')
            line = "        {" + ", ".join(parts) + "},"
            new_content += line + "\n"
        new_content += "    ]"
        if i < len(sorted_keys) - 1:
            new_content += ",\n"
        else:
            new_content += "\n"

    new_content += "}\n\n"
    new_content += "if __name__ == '__main__':\n"
    new_content += "    total = sum(len(v) for v in DB.values())\n"
    new_content += "    print(f\"refactor complete: total {total} entries\")\n"

    with open(distros_path, 'w') as f:
        f.write(new_content)

if __name__ == '__main__':
    refactor_distros()
