# super categorizer for 1000+ distro lists

import json
import os

def categorize():
    input_path = os.path.join(os.path.dirname(__file__), "massive_distros.json")
    output_path = os.path.join(os.path.dirname(__file__), "massive_distros_categorized.json")
    
    if not os.path.exists(input_path):
        print("input file not found.")
        return

    with open(input_path, "r") as f:
        distros = json.load(f)

    # Comprehensive Category Mapping
    families = {
        "Ubuntu Family": ["Ubuntu", "Kubuntu", "Xubuntu", "Lubuntu", "Edubuntu", "Mint", "Zorin", "Pop!", "Elementary", "Neon", "Bodhi", "Trisquel", "Peppermint"],
        "Debian Family": ["Debian", "Kali", "Parrot", "MX Linux", "antiX", "PureOS", "Deepin", "Sparky", "BunsenLabs", "Devuan", "Q4OS", "SolydXK"],
        "Arch Family": ["Arch", "Manjaro", "Endeavour", "Garuda", "Artix", "BlackArch", "CachyOS", "RebornOS", "ArcoLinux", "Antergos"],
        "Red Hat / Enterprise": ["Fedora", "Red Hat", "RHEL", "CentOS", "AlmaLinux", "Rocky", "Oracle", "Nobara", "Scientific", "Clear", "EuroLinux"],
        "SUSE / openSUSE": ["SUSE", "openSUSE", "Tumbleweed", "Leap", "Gecko"],
        "Gentoo / Source": ["Gentoo", "Calculate", "Sabayon", "Funtoo", "Exherbo", "Source Mage"],
        "Slackware Based": ["Slackware", "Salix", "Zenwalk", "Vector", "Porteus", "Absolute", "Slax"],
        "Lightweight / Minimal": ["Puppy", "Tiny Core", "SliTaz", "Damn Small", "Porteus", "Alpine", "Bodhi", "AntiX", "LXLE", "Puppy"],
        "Security / Recovery": ["Tails", "Qubes", "Whonix", "Kodachi", "BackBox", "Pentoo", "SystemRescue", "GParted", "Clonezilla", "Rescuezilla", "Hiren", "CAINE", "DEFT"],
        "Server / Cloud / NAS": ["Proxmox", "TrueNAS", "OpenMediaVault", "Unraid", "Talos", "CoreOS", "Flatcar", "Rancher", "Synology", "FreeNAS"],
        "Gaming / Multimedia": ["SteamOS", "ChimeraOS", "Batocera", "Lakka", "Recalbox", "RetroPie", "Nobara", "Bazzite", "AV Linux", "Studio", "LibreELEC", "OSMC"],
        "Mobile / Android": ["Android", "Bliss", "Lineage", "postmarketOS", "Mobian", "Plasma Mobile", "Ubuntu Touch", "Sailfish", "PrimeOS", "Phoenix OS"],
        "Independent / Unique": ["NixOS", "Void", "Solus", "KaOS", "Haiku", "ReactOS", "FreeBSD", "OpenBSD", "NetBSD", "DragonFly", "GhostBSD", "PCLinuxOS", "Mageia", "OpenMandriva"]
    }

    categorized = {}
    
    for distro in distros:
        name = distro['name']
        found = False
        
        # skip general articles
        if any(x in name for x in ["Comparison of", "List of", "Linux distribution"]):
            continue

        for family, keywords in families.items():
            if any(key.lower() in name.lower() for key in keywords):
                if family not in categorized:
                    categorized[family] = []
                categorized[family].append(distro)
                found = True
                break
        
        if not found:
            # Try to catch some common suffixes
            if "BSD" in name:
                cat = "BSD / Alternative"
            elif "Edu" in name:
                cat = "Education"
            elif "Server" in name:
                cat = "Server / Cloud / NAS"
            else:
                cat = "Others / Niche"
                
            if cat not in categorized:
                categorized[cat] = []
            categorized[cat].append(distro)

    # Sort categories to ensure a good flow
    sorted_categorized = dict(sorted(categorized.items(), key=lambda x: len(x[1]), reverse=True))

    with open(output_path, "w") as f:
        json.dump(sorted_categorized, f, indent=4)
    
    count = sum(len(v) for v in sorted_categorized.values())
    print(f"categorized {count} distros into {len(sorted_categorized)} refined groups.")

if __name__ == "__main__":
    categorize()
