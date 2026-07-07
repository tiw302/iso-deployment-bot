# utils.py
#
# shared utility functions and centralized configuration.
# contains category definitions and url parsing helpers for the library.

import os
from urllib.parse import urlparse, parse_qs

def resolve_filename(url: str) -> str:
    """
    resolves the expected local filename from a download url.
    handles standard filenames, sourceforge downloads, and query params.
    prevents name clashes for generic names (e.g. latest.iso) by adding parent path.
    """
    if not url or url == '#':
        return 'image.iso'

    parsed = urlparse(url)

    # 1. handle sourceforge '/download' urls
    path_parts = [p for p in parsed.path.split('/') if p]
    filename = ""
    if path_parts and path_parts[-1] == 'download':
        if len(path_parts) >= 2:
            filename = path_parts[-2]

    # 2. handle query parameters (e.g. slax ?file=...)
    if not filename:
        query_params = parse_qs(parsed.query)
        for key in ['file', 'filename', 'path']:
            if key in query_params and query_params[key]:
                filename = os.path.basename(query_params[key][0])
                break

    # 3. fallback to standard path basename
    if not filename:
        filename = os.path.basename(parsed.path)

    # 4. fallback to url split if path basename is empty or generic
    if not filename or filename in ('', 'download', 'download.php', 'download.cgi'):
        # filter out trailing slash to get the last non-empty segment
        non_empty_segments = [s for s in url.split('/') if s]
        if len(non_empty_segments) > 1:
            filename = non_empty_segments[-1].split('?')[0]

    # clean query parameters or hash anchors
    if filename:
        filename = filename.split('?')[0].split('#')[0]

    # ensure filename has an extension
    if not filename or '.' not in filename:
        filename = (filename or 'image') + '.iso'

    filename = filename.strip()

    # 5. handle generic filenames like 'latest.iso', 'latest', 'download.iso' to avoid collisions
    # strip extensions for checking, e.g. 'download.php.iso' -> 'download'
    fn_clean = os.path.splitext(filename)[0].lower()
    if fn_clean in ('latest', 'download', 'image', 'download.php', 'download.cgi'):
        forbidden = {'latest', 'download', 'iso', 'files', 'projects', 'release', 'current', 'amd64', 'x86_64', 'x64', 'image', 'bin'}
        non_generic_parent = None
        for p in reversed(path_parts):
            p_clean = os.path.splitext(p)[0].lower()
            if p_clean not in forbidden:
                non_generic_parent = p
                break
        if non_generic_parent:
            filename = f"{non_generic_parent}-{filename}"
            # ensure it ends with .iso if it got stripped or messed up
            if not any(filename.endswith(ext) for ext in ('.iso', '.img', '.gz', '.xz', '.zip', '.bin', '.bz2', '.7z')):
                filename += '.iso'

    # standardize .img to .img.iso (to allow downloading in homelabs as bootable isos)
    # replace only trailing .img to prevent mangling middle parts of name
    if filename.endswith(".img"):
        filename = filename[:-4] + ".img.iso"

    return filename

# global order of categories for dashboard and database formatting
CATEGORY_ORDER = [
    "linux/ubuntu", "linux/ubuntu-noble", "linux/ubuntu-plucky", "linux/ubuntu-jammy",
    "linux/debian", "linux/debian-based", "linux/mint", "linux/pop-os", "linux/zorin",
    "linux/arch-family",
    "linux/enterprise", "linux/server", "linux/server-cloud", "linux/fedora-spins",
    "linux/gaming",
    "linux/security", "linux/pentesting", "linux/forensic", "linux/privacy",
    "linux/immutable", "linux/wayland-tiling", "linux/rolling",
    "linux/lightweight", "linux/minimal",
    "homelab", "homelab/virtualization", "homelab/firewall", "homelab/nas",
    "specialized/vintage", "specialized/containers", "specialized/risc-emulation",
    "recovery/tools", "recovery/backup",
    "arm/raspberry-pi", "arm/sbc",
    "windows/eval",
    "android-x86", "chromeos",
    "alternative/bsd",
    "linux/ai-ml", "linux/developer", "linux/desktop-env", "linux/embedded", "linux/specialized",
    "linux/office", "linux/hardware", "linux/live-tools", "linux/education", "linux/scientific",
    "linux/legacy", "linux/others", "linux/experimental", "linux/alternative-arch", "linux/cloud",
    "linux/multimedia"
]

# map keys to clean display names
CATEGORY_NAMES = {
    "linux/ubuntu": "ubuntu",
    "linux/ubuntu-noble": "ubuntu 24.04 noble",
    "linux/ubuntu-plucky": "ubuntu 25.04 plucky",
    "linux/ubuntu-jammy": "ubuntu 22.04 jammy",
    "linux/debian": "debian",
    "linux/debian-based": "debian derivatives",
    "linux/mint": "linux mint",
    "linux/pop-os": "pop!_os",
    "linux/zorin": "zorin os",
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
    "homelab/firewall": "firewall / router",
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
    "linux/alternative-arch": "alternative architectures",
    "linux/cloud": "cloud",
    "linux/multimedia": "multimedia"
}
