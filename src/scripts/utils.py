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
            if not any(filename.endswith(ext) for ext in ('.iso', '.img', '.gz', '.xz', '.zip', '.bin', '.bz2')):
                filename += '.iso'

    # standardize .img to .img.iso (to allow downloading in homelabs as bootable isos)
    if filename.endswith(".img"):
        filename = filename.replace(".img", ".img.iso")

    return filename
