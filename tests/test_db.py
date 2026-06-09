import unittest
import os

# setup path to import DB and resolve_filename
script_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.join(os.path.dirname(script_dir), "src"))
# sys.path.append(os.path.join(os.path.dirname(script_dir), "src", "scripts"))

from os_deployment_library.distros import DB
from os_deployment_library.scripts.utils import resolve_filename

class TestDatabase(unittest.TestCase):
    def test_db_structure(self):
        self.assertIsInstance(DB, dict)
        self.assertGreater(len(DB), 0)

    def test_entries_validity(self):
        seen_urls = set()
        seen_filenames = {}

        for category, entries in DB.items():
            self.assertIsInstance(category, str)
            self.assertIsInstance(entries, list)
            self.assertGreater(len(entries), 0, f"Category '{category}' is empty.")

            for idx, entry in enumerate(entries):
                self.assertIsInstance(entry, dict, f"Entry at index {idx} in category '{category}' is not a dict.")

                # Check required fields
                name = entry.get('name')
                url = entry.get('url')

                self.assertIsNotNone(name, f"Entry {idx} in '{category}' is missing name.")
                self.assertIsNotNone(url, f"Entry {idx} in '{category}' is missing url.")
                self.assertGreater(len(name), 0, f"Entry {idx} in '{category}' has empty name.")
                self.assertGreater(len(url), 0, f"Entry {idx} in '{category}' has empty url.")

                # Check url protocol
                self.assertTrue(
                    url.startswith('http://') or url.startswith('https://') or url.startswith('ftp://'),
                    f"Entry '{name}' in '{category}' has invalid protocol: {url}"
                )

                # Check duplicate URLs
                self.assertNotIn(url, seen_urls, f"Duplicate URL found in DB: {url}")
                seen_urls.add(url)

                # Resolve filename and check for crashes
                filename = resolve_filename(url)
                self.assertTrue(filename, f"Failed to resolve filename for '{name}': {url}")

                # Check for filename collisions in the same category (would cause Google Drive clobbering)
                full_path = f"{category}/{filename}"
                self.assertNotIn(full_path, seen_filenames, f"Filename collision in Google Drive: '{filename}' used by both '{name}' and '{seen_filenames.get(full_path)}' under category '{category}'.")
                seen_filenames[full_path] = name

if __name__ == "__main__":
    unittest.main()
