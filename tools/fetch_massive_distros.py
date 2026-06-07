# fetch massive categorized distro list from wikidata

import urllib.request
import urllib.parse
import json
import os

def fetch_massive_distros():
    print("querying wikidata for categorized linux distributions... (this may take 10-20 seconds)")

    # query for linux distributions and what they are based on
    query = """
    SELECT ?itemLabel ?website ?basedOnLabel WHERE {
      ?item wdt:P31/wdt:P279* wd:Q14579.
      OPTIONAL { ?item wdt:P856 ?website. }
      OPTIONAL { ?item wdt:P144 ?basedOn. }
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    """

    url = "https://query.wikidata.org/sparql?query=" + urllib.parse.quote(query) + "&format=json"

    try:
        req = urllib.request.Request(url)
        # Using a very standard browser-like User-Agent
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        req.add_header('Accept', 'application/sparql-results+json')

        with urllib.request.urlopen(req, timeout=45) as response:
            data = json.loads(response.read().decode('utf-8'))

        results = data.get('results', {}).get('bindings', [])

        # grouping by category
        categories = {}
        total_count = 0

        for item in results:
            name = item.get('itemLabel', {}).get('value')
            website = item.get('website', {}).get('value', '#')
            based_on = item.get('basedOnLabel', {}).get('value', 'Independent / Others')

            if not name or name.startswith('Q') and name[1:].isdigit(): continue # skip raw IDs

            # Clean up category name
            cat_name = based_on
            if "Linux" in cat_name and cat_name != "Linux":
                cat_name = cat_name.replace("Linux", "").strip()
            if cat_name == "Independent / Others":
                cat_name = "Independent / Specialty"
            else:
                cat_name = f"{cat_name} Based"

            if cat_name not in categories:
                categories[cat_name] = []

            # avoid duplicates within category
            if not any(d['name'] == name for d in categories[cat_name]):
                categories[cat_name].append({
                    "name": name,
                    "url": website
                })
                total_count += 1

        return categories, total_count
    except Exception as e:
        print(f"error fetching from wikidata: {e}")
        return {}, 0

if __name__ == "__main__":
    categories, count = fetch_massive_distros()
    if categories:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(os.path.dirname(script_dir), "src", "scripts", "massive_distros_categorized.json")
        with open(output_path, "w") as f:
            json.dump(categories, f, indent=4)
        print(f"successfully saved {count} distributions across {len(categories)} categories to {output_path}")
    else:
        print("failed to fetch data.")
