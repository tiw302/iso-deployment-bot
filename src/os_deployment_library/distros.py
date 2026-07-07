# distros.py
#
# runtime loader for the central iso inventory database.
# dynamically loads distros.json for backwards compatibility.

import os
import json

# load distros database from JSON file
distros_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(distros_dir, "distros.json")

with open(json_path, "r", encoding="utf-8") as _f:
    DB: dict[str, list[dict]] = json.load(_f)

if __name__ == '__main__':
    total = sum(len(v) for v in DB.values())
    print(f"distros database loaded: total {total} entries")
