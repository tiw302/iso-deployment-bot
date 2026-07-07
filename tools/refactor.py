# refactor.py
#
# database migration and structure refactoring tool.
# safely validates and reorganizes the json database structure.

import os
import json
from os_deployment_library.scripts.utils import resolve_filename, CATEGORY_ORDER

def validate_db(db_dict):
    # validate database entries for missing fields or invalid data
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

    print(f"validation finished: {errors} errors, {warnings} warnings")
    return errors == 0

def refactor_distros():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    distros_json_path = os.path.join(base_dir, 'src', 'os_deployment_library', 'distros.json')

    if not os.path.exists(distros_json_path):
        print(f"error: {distros_json_path} not found")
        return

    # load from distros.json directly
    with open(distros_json_path, 'r', encoding='utf-8') as f:
        db_dict = json.load(f)

    # run validation before proceeding
    if not validate_db(db_dict):
        print("refactor aborted due to critical errors in database.")

    # de-duplicate entries by resolved filename per category
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

    # reorganize categories by CATEGORY_ORDER
    sorted_keys = []
    for cat in CATEGORY_ORDER:
        if cat in new_db_dict:
            sorted_keys.append(cat)
    for cat in sorted(new_db_dict.keys()):
        if cat not in sorted_keys:
            sorted_keys.append(cat)

    # rebuild ordered DB dictionary
    ordered_db = {}
    for key in sorted_keys:
        ordered_db[key] = []
        for entry in new_db_dict[key]:
            # sort keys in each entry to keep name, url, size first
            ordered_entry = {}
            for k in ["name", "url", "size"]:
                if k in entry:
                    ordered_entry[k] = entry[k]
            for k in entry:
                if k not in ordered_entry:
                    ordered_entry[k] = entry[k]
            ordered_db[key].append(ordered_entry)

    # save back to distros.json
    with open(distros_json_path, 'w', encoding='utf-8') as f:
        json.dump(ordered_db, f, indent=4)

    print(f"successfully refactored and saved to: {distros_json_path}")

if __name__ == '__main__':
    refactor_distros()
