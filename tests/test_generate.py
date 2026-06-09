# tests for generate_index.py helper functions

import unittest
import os

# setup path
script_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.join(os.path.dirname(script_dir), "src", "scripts"))

from os_deployment_library.scripts.generate_index import clean_filename, format_size, infer_tags, get_lib_description


class TestCleanFilename(unittest.TestCase):
    def test_standard_iso(self):
        result = clean_filename("ubuntu-24.04.2-desktop-amd64.iso")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_strips_arch_keywords(self):
        result = clean_filename("fedora-workstation-amd64-x86_64.iso")
        self.assertNotIn("amd64", result.lower())
        self.assertNotIn("x86_64", result.lower())

    def test_replaces_separators(self):
        result = clean_filename("my-distro_name.version.iso")
        # should not contain raw separators
        self.assertNotIn("-", result)
        self.assertNotIn("_", result)

    def test_title_case(self):
        result = clean_filename("alpine-standard-3.21.iso")
        # each word should be title case
        for word in result.split():
            if word[0].isalpha():
                self.assertTrue(word[0].isupper(), f"'{word}' is not title cased")

    def test_double_ext_img(self):
        result = clean_filename("noble-server-arm64.img.xz")
        self.assertIsInstance(result, str)


class TestFormatSize(unittest.TestCase):
    def test_bytes(self):
        self.assertEqual(format_size(500), "500.0 B")

    def test_kilobytes(self):
        self.assertEqual(format_size(1024), "1.0 KB")

    def test_megabytes(self):
        self.assertEqual(format_size(1048576), "1.0 MB")

    def test_gigabytes(self):
        self.assertEqual(format_size(1073741824), "1.0 GB")

    def test_terabytes(self):
        self.assertEqual(format_size(1099511627776), "1.0 TB")

    def test_invalid_input(self):
        result = format_size("not a number")
        self.assertEqual(result, "?.? GB")

    def test_zero(self):
        self.assertEqual(format_size(0), "0.0 B")

    def test_fractional(self):
        result = format_size(1536)
        self.assertEqual(result, "1.5 KB")


class TestInferTags(unittest.TestCase):
    """Test the tag inference engine that auto-tags distros."""

    # os family tags
    def test_ubuntu_tags(self):
        tags = infer_tags("Ubuntu 24.04 Desktop", "linux/ubuntu")
        self.assertIn("ubuntu", tags)
        self.assertIn("debian", tags)
        self.assertIn("desktop", tags)

    def test_fedora_tags(self):
        tags = infer_tags("Fedora 44 Workstation", "linux/enterprise")
        self.assertIn("fedora", tags)
        self.assertIn("redhat", tags)

    def test_arch_tags(self):
        tags = infer_tags("Arch Linux latest", "linux/arch-family")
        self.assertIn("arch", tags)

    def test_kali_tags(self):
        tags = infer_tags("Kali Linux 2026.1", "linux/security")
        self.assertIn("kali", tags)
        self.assertIn("security", tags)
        self.assertIn("debian", tags)

    def test_mint_tags(self):
        tags = infer_tags("Linux Mint 22.3 Cinnamon", "linux/mint")
        self.assertIn("mint", tags)
        self.assertIn("ubuntu", tags)
        self.assertIn("debian", tags)
        self.assertIn("cinnamon", tags)

    def test_manjaro_tags(self):
        tags = infer_tags("Manjaro KDE", "linux/arch-family")
        self.assertIn("manjaro", tags)
        self.assertIn("arch", tags)
        self.assertIn("kde", tags)

    def test_rocky_tags(self):
        tags = infer_tags("Rocky Linux 9 Minimal", "linux/enterprise")
        self.assertIn("rocky-linux", tags)
        self.assertIn("redhat", tags)

    def test_alma_tags(self):
        tags = infer_tags("AlmaLinux 9 DVD", "linux/enterprise")
        self.assertIn("almalinux", tags)
        self.assertIn("redhat", tags)

    # desktop environment tags
    def test_kde_tag(self):
        tags = infer_tags("Kubuntu 26.04", "linux/ubuntu")
        self.assertIn("kde", tags)

    def test_xfce_tag(self):
        tags = infer_tags("Xubuntu 26.04", "linux/ubuntu")
        self.assertIn("xfce", tags)

    def test_gnome_tag(self):
        tags = infer_tags("GNOME OS Nightly", "linux/desktop-env")
        self.assertIn("gnome", tags)

    def test_sway_tag(self):
        tags = infer_tags("Fedora 44 Sway Spin", "linux/fedora-spins")
        self.assertIn("sway", tags)

    def test_budgie_tag(self):
        tags = infer_tags("Ubuntu Budgie 26.04", "linux/office")
        self.assertIn("budgie", tags)

    # role tags
    def test_server_tag(self):
        tags = infer_tags("Ubuntu 24.04 Server", "linux/server")
        self.assertIn("server", tags)

    def test_lts_tag(self):
        tags = infer_tags("Ubuntu 24.04 LTS Desktop", "linux/ubuntu")
        self.assertIn("lts", tags)
        self.assertIn("desktop", tags)

    def test_minimal_tag(self):
        tags = infer_tags("Alpine Linux", "linux/minimal", description="lightweight")
        self.assertIn("minimal", tags)

    def test_gaming_tag(self):
        tags = infer_tags("Garuda Gaming latest", "linux/gaming")
        self.assertIn("gaming", tags)

    def test_hypervisor_tag(self):
        tags = infer_tags("Proxmox VE 9.1", "homelab/virtualization")
        self.assertIn("proxmox", tags)
        self.assertIn("hypervisor", tags)

    def test_nas_tag(self):
        tags = infer_tags("OpenMediaVault 7.4", "homelab/nas")
        self.assertIn("openmediavault", tags)
        self.assertIn("nas", tags)

    def test_recovery_tag(self):
        tags = infer_tags("CloneZilla 3.2.0", "recovery/tools")
        self.assertIn("clonezilla", tags)
        self.assertIn("recovery", tags)

    # bsd family
    def test_freebsd_tags(self):
        tags = infer_tags("FreeBSD 14.4 amd64", "alternative/bsd")
        self.assertIn("freebsd", tags)
        self.assertIn("bsd", tags)

    def test_openbsd_tags(self):
        tags = infer_tags("OpenBSD 7.7 amd64", "alternative/bsd")
        self.assertIn("openbsd", tags)
        self.assertIn("bsd", tags)

    # architecture tags
    def test_arm64_tag(self):
        tags = infer_tags("Ubuntu Server RPi", "arm/raspberry-pi", filename="noble-arm64.img")
        self.assertIn("arm64", tags)
        self.assertIn("rpi", tags)

    def test_android_tag(self):
        tags = infer_tags("BlissOS 16.9.9", "android-x86")
        self.assertIn("blissos", tags)
        self.assertIn("android", tags)

    # return type
    def test_returns_sorted_list(self):
        tags = infer_tags("Ubuntu 24.04 Desktop", "linux/ubuntu")
        self.assertIsInstance(tags, list)
        self.assertEqual(tags, sorted(tags))

    def test_no_duplicates(self):
        tags = infer_tags("Ubuntu 24.04 Desktop", "linux/ubuntu")
        self.assertEqual(len(tags), len(set(tags)))


class TestGetLibDescription(unittest.TestCase):
    def test_ubuntu_description(self):
        desc = get_lib_description("Ubuntu 24.04")
        self.assertIn("linux", desc.lower())

    def test_proxmox_description(self):
        desc = get_lib_description("Proxmox VE 9.1")
        self.assertIn("virtualization", desc.lower())

    def test_unknown_distro(self):
        desc = get_lib_description("SomeRandomOS 1.0")
        self.assertIsInstance(desc, str)
        self.assertGreater(len(desc), 0)

    def test_alpine_description(self):
        desc = get_lib_description("Alpine Linux 3.21")
        self.assertIn("lightweight", desc.lower())


if __name__ == "__main__":
    unittest.main()
