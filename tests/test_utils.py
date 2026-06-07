import unittest
import sys
import os

# setup path to import utils
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(os.path.dirname(script_dir), "src", "scripts"))

from utils import resolve_filename

class TestUtils(unittest.TestCase):
    def test_standard_url(self):
        url = "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-desktop-amd64.iso"
        self.assertEqual(resolve_filename(url), "ubuntu-24.04.2-desktop-amd64.iso")
        
    def test_sourceforge_download_url(self):
        url = "https://sourceforge.net/projects/mx-linux/files/Final/MX-23.6/MX-23.6-kde_x64.iso/download"
        self.assertEqual(resolve_filename(url), "MX-23.6-kde_x64.iso")
        
    def test_sourceforge_nested_download_url(self):
        url = "https://sourceforge.net/projects/sparkylinux/files/8.0/sparkylinux-8.0-x86_64-kde.iso/download"
        self.assertEqual(resolve_filename(url), "sparkylinux-8.0-x86_64-kde.iso")
        
    def test_query_parameter_file(self):
        url = "https://www.slax.org/download.php?type=x86_64&file=slax-64bit-11.6.0.iso"
        self.assertEqual(resolve_filename(url), "slax-64bit-11.6.0.iso")
        
    def test_img_to_img_iso(self):
        url = "https://example.com/raspbian.img"
        self.assertEqual(resolve_filename(url), "raspbian.img.iso")
        
    def test_img_xz_preserved(self):
        url = "https://cdimage.ubuntu.com/.../noble-preinstalled-server-arm64+raspi.img.xz"
        self.assertEqual(resolve_filename(url), "noble-preinstalled-server-arm64+raspi.img.xz")
        
    def test_bz2_preserved(self):
        url = "https://example.com/distro-image.bz2"
        self.assertEqual(resolve_filename(url), "distro-image.bz2")

    def test_iso_bz2_preserved(self):
        url = "https://mirror.opnsense.org/.../OPNsense-25.1-dvd-amd64.iso.bz2"
        self.assertEqual(resolve_filename(url), "OPNsense-25.1-dvd-amd64.iso.bz2")
        
    def test_missing_extension(self):
        url = "https://example.com/somefile"
        self.assertEqual(resolve_filename(url), "somefile.iso")
        
    def test_empty_or_hash(self):
        self.assertEqual(resolve_filename(""), "image.iso")
        self.assertEqual(resolve_filename("#"), "image.iso")

if __name__ == "__main__":
    unittest.main()
