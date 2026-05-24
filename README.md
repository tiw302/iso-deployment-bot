# os-deployment-library

[![Daily Sync](https://github.com/tiw302/iso-deployment-bot/actions/workflows/daily_sync.yml/badge.svg)](https://github.com/tiw302/iso-deployment-bot/actions/workflows/daily_sync.yml)
[![Lint](https://github.com/tiw302/iso-deployment-bot/actions/workflows/lint.yml/badge.svg)](https://github.com/tiw302/iso-deployment-bot/actions/workflows/lint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Language-Python_3-3776AB.svg)](https://www.python.org/)
[![Storage](https://img.shields.io/badge/Storage-Google_Drive-4285F4.svg)](#how-it-works)
[![Last Commit](https://img.shields.io/github/last-commit/tiw302/iso-deployment-bot.svg)](https://github.com/tiw302/iso-deployment-bot/commits/master)

A simple, automated ISO mirroring system for homelabs and personal use. This project utilizes an ephemeral runner architecture via GitHub Actions, fetching operating system images through multi-threaded downloaders (`aria2c`) and synchronizing them directly to Google Drive (`rclone`) to generate a static web directory.

**[Browse the Web Directory: https://tiw302.github.io/iso-deployment-bot](https://tiw302.github.io/iso-deployment-bot)**

---

## Table of Contents

| Introduction | Setup & Build | Components | Resources |
|---|---|---|---|
| [Overview](#introduction) | [Requirements](#requirements) | [Core Scripts](#core-scripts) | [Web Directory](https://tiw302.github.io/iso-deployment-bot) |
| [Motivation](#motivation) | [Installation](#installation) | [Data Sources](#adding-distributions) | [Contributing](#contributing) |
| [Design Choices](#design-choices) | [Cloud Config](#rclone-configuration) | [Maintenance Tools](#maintenance-tools) | [License](#license) |

---

## Introduction

**os-deployment-library (OSDL)** is a modest collection of Python scripts designed to automate the downloading and storing of operating system ISOs.

It was built as a practical workaround for homelab operators or developers who frequently need to provision virtual machines but find it inconvenient to repeatedly download images from slow or distant official mirrors. By utilizing GitHub Actions as a free compute runner and Rclone to upload files to Google Drive, it maintains a personal repository of OS images with minimal manual intervention.

---

## Motivation

When setting up test environments or home servers, grabbing an ISO directly from upstream sources can sometimes be frustrating:

- **Download Speeds:** Official mirrors can be slow depending on your geographic location or their current load.
- **Archival:** Older point-releases are often removed from upstream sites once a newer version drops, making reproducible setups difficult.
- **Manual Effort:** Keeping track of which distributions have released new versions and manually downloading them is tedious.

This project attempts to mitigate these minor annoyances by running an automated script overnight. It fetches the required files using multi-threaded tools and places them into cloud storage, generating a basic web page so the files are easy to find the next day.

---

## Design Choices

The project is not an enterprise-grade infrastructure tool, but rather a pragmatic script built around a few specific choices to keep it free and easy to maintain:

**Stateless Execution:** The system does not require a persistent server. It runs entirely on ephemeral GitHub Actions runners. It determines what needs to be downloaded by comparing a local text file (`src/distros.py`) against what currently exists in the target Google Drive.

**Parallel Downloading:** Instead of standard single-thread downloads, it uses `aria2c` with 16 connections. This helps finish the downloads quickly before the GitHub Action job times out.

**Basic Web Index:** Browsing files in Google Drive can be slow. To make downloading the ISOs easier, the script automatically generates a static HTML page (`web/index.html`) using a simple Python template after every successful sync.

---

## How It Works

The workflow runs daily via a GitHub Actions Cron schedule (`.github/workflows/daily_sync.yml`). The sequence of events is straightforward:

1. **Check State:** `sync.py` reads the desired list of ISOs from `src/distros.py` and uses Rclone to check which ones are missing from your Google Drive.
2. **Download:** Any missing files are downloaded to the GitHub runner's temporary storage using `aria2c`.
3. **Upload:** The successfully downloaded files are moved to Google Drive via Rclone.
4. **Cleanup:** Because GitHub runners have limited disk space (~14GB), the script deletes local files immediately after uploading to make room for the next one.
5. **Generate Index:** `generate_index.py` creates a fresh static HTML page based on what is now available in the database.

---

## Requirements

| Component | Requirement |
|---|---|
| Runtime | Python 3.8+ |
| Downloader | `aria2` |
| Cloud Sync | `rclone` |
| Storage Target | Google Drive (or any Rclone-compatible cloud storage) with adequate free space. |

---

## Installation

### Local Execution

If you want to run the scripts manually on your own machine instead of GitHub Actions:

```bash
# 1. Tidy up the database (sort entries and remove duplicates)
python3 src/scripts/refactor.py

# 2. Run the main download/upload script
python3 src/scripts/sync.py

# 3. Generate the static web index
python3 src/scripts/generate_index.py
```

### Rclone Configuration (For GitHub Actions)

To let GitHub Actions access your Google Drive without committing passwords to the repository, you need to provide your Rclone configuration as a base64-encoded secret.

1. Setup your remote locally using `rclone config`. Make sure the remote name in your config matches the one expected in `sync.py`.
2. Find where your config file is stored by running: `rclone config file`.
3. Encode the file's contents to base64:

   ```bash
   base64 -w 0 <path_to_rclone.conf>
   ```

4. In your GitHub repository, go to **Settings > Secrets and variables > Actions**.
5. Create a new repository secret named `RCLONE_CONF_DATA` and paste the base64 string.

---

## Adding Distributions

The primary list of all operating systems is kept in a simple Python dictionary inside `src/distros.py`. To track a new OS, just add an entry:

```python
{
    "name": "Ubuntu 24.04 LTS",
    "url": "https://releases.ubuntu.com/24.04/ubuntu-24.04-desktop-amd64.iso",
    "category": "Linux",
    "description": "The latest Long Term Support release of Ubuntu."
}
```

The next time the script runs, it will notice the new entry, download the ISO, upload it to the cloud, and update the web page.

---

## Included Tools & Scripts

The repository is divided into core operational scripts and a few helper tools used to maintain the database.

### Core Scripts

- `src/distros.py`: The single source of truth containing the list of all ISO URLs.
- `src/scripts/sync.py`: The main script that handles the logic of downloading and uploading.
- `src/scripts/generate_index.py`: The script responsible for creating the HTML front-end.

### Maintenance Tools

These are optional scripts located in the `tools/` folder, written to make managing a large list of ISOs less manual:

- `tools/fetch_top_distros.py`: A basic scraper to find popular Linux distributions and add them to the list.
- `tools/fetch_descriptions_wikipedia.py`: Reaches out to the Wikipedia API to automatically pull short text descriptions for the OSs in the database.
- `tools/check_links.py`: Pings every URL in `src/distros.py` to check for 404/dead links, so they can be updated or removed.
- `tools/refactor.py`: A formatting script to sort the list alphabetically and remove any accidental duplicates.

---

## Contributing

This is a personal utility, but suggestions and improvements are welcome. If you find a bug in the synchronization logic, want to add support for a different cloud provider, or just want to fix a broken link in `distros.py`, feel free to open an issue or a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.
