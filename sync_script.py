import os
import subprocess

# terminal colors for github logs
C = '\033[96m'  # cyan
G = '\033[92m'  # green
R = '\033[91m'  # red
Y = '\033[93m'  # yellow
W = '\033[0m'   # reset

# remote name must match rclone.conf (we used [gdrive])
REMOTE_BASE = "gdrive:os-deployment-library"

def dl(url, category):
    name = url.split('/')[-1].split('?')[0]
    local_dir = f"./temp/{category}"
    os.makedirs(local_dir, exist_ok=True)
    remote_path = f"{REMOTE_BASE}/{category}/{name}"

    print(f"{C}[ CHECK  ]{W} {name}")
    
    # check if file already exists on gdrive
    check = subprocess.run(["rclone", "lsf", remote_path], capture_output=True)
    if check.returncode == 0 and name in check.stdout.decode():
        print(f"{Y}[ SKIP   ]{W} {name} (already exists)")
        return

    # start download
    print(f"{C}[ FETCH  ]{W} downloading {name}...")
    cmd = [
        "aria2c", "-x", "16", "-s", "16", 
        "--auto-file-renaming=false", "--dir", local_dir, "-o", name, url
    ]
    
    try:
        subprocess.run(cmd, check=True)
        # upload to gdrive
        print(f"{C}[ UPLOAD ]{W} sending {name} to cloud...")
        subprocess.run(["rclone", "move", f"{local_dir}/{name}", f"{REMOTE_BASE}/{category}/"], check=True)
        print(f"{G}[  OK    ]{W} {name} synced successfully")
    except Exception as e:
        print(f"{R}[ ERROR  ]{W} failed to process {name}: {e}")

# database 2026 (add more as you like)
db = {
    "Linux-Distros/Arch-Based": [
        "https://mirror.kku.ac.th/archlinux/iso/latest/archlinux-x86_64.iso",
        "https://mirrors.n0p.me/cachyos/desktop/260101/cachyos-desktop-linux-260101.iso"
    ],
    "Linux-Distros/Debian-Based": [
        "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.9.0-amd64-DVD-1.iso",
        "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-desktop-amd64.iso"
    ],
    "Security-Pentest": [
        "https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-installer-amd64.iso",
        "https://deb.parrot.sh/parrot/iso/7.0/Parrot-security-7.0_amd64.iso"
    ]
}

if __name__ == "__main__":
    print(f"{C}[ START  ]{W} iso mirror automation initiated")
    # clean up any leftovers
    subprocess.run("rm -rf ./temp/*.aria2", shell=True)
    for cat, urls in db.items():
        for url in urls:
            dl(url, cat)
    print(f"{G}[ FINISH ]{W} automation cycle complete")
