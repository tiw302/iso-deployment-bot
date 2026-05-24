import json
import os
import urllib.request
import urllib.parse
import time

def fetch_summary(title):
    safe_title = urllib.parse.quote(title)
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{safe_title}"
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'OS-Deployment-Library-Bot/1.0 (contact: siripukwaewwrrn@gmail.com)')
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            extract = data.get('extract', '')
            if extract:
                sentences = extract.split('. ')
                if sentences:
                    desc = sentences[0]
                    if not desc.endswith('.'):
                        desc += '.'
                    return desc
            return data.get('description', '')
    except Exception as e:
        print(f"Error fetching summary for {title}: {e}")
        return None

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(os.path.dirname(script_dir), "src", "scripts", "massive_distros_categorized.json")
    
    if not os.path.exists(json_path):
        print(f"JSON not found at: {json_path}")
        return
        
    with open(json_path, "r") as f:
        categories = json.load(f)
        
    total_items = sum(len(items) for items in categories.values())
    print(f"Loaded {total_items} items. Starting Wikipedia summary fetch...")
    
    count = 0
    updated = 0
    
    for cat_name, items in categories.items():
        for item in items:
            count += 1
            name = item.get("name")
            url = item.get("url", "")
            current_desc = item.get("description", "")
            
            if current_desc and not current_desc.startswith("View "):
                continue
                
            if "wikipedia.org/wiki/" in url:
                title = url.split("wikipedia.org/wiki/")[-1]
                title = urllib.parse.unquote(title)
                print(f"[{count}/{total_items}] Fetching summary for {name} ({title})...")
                desc = fetch_summary(title)
                if desc:
                    desc = desc.replace("\n", " ").strip()
                    item["description"] = desc
                    updated += 1
                    print(f" -> Found: {desc[:60]}...")
                else:
                    print(f" -> Failed/No extract")
                
                time.sleep(0.1)
                
            if updated > 0 and updated % 20 == 0:
                with open(json_path, "w") as f:
                    json.dump(categories, f, indent=4)
                print("--- Intermediate progress saved ---")

    with open(json_path, "w") as f:
        json.dump(categories, f, indent=4)
        
    print(f"Finished. Updated {updated} descriptions out of {total_items} total.")

if __name__ == "__main__":
    main()
