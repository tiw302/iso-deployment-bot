import unittest
from tools.fetch_checksums import guess_checksum_urls

class TestChecksums(unittest.TestCase):
    def test_guess_checksum_urls(self):
        url = "https://example.com/iso/distro-1.0.iso"
        guesses = guess_checksum_urls(url)
        self.assertIn("https://example.com/iso/distro-1.0.iso.sha256", guesses)
        self.assertIn("https://example.com/iso/SHA256SUMS", guesses)
        self.assertIn("https://example.com/iso/sha256sum.txt", guesses)
