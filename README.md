# os-deployment-library

## overview
automated iso mirroring system designed to synchronize multiple operating system distributions to google drive storage. the system utilizes github actions for scheduled execution, aria2 for multi-threaded downloads, and rclone for cloud storage synchronization.

## infrastructure
- runtime: github actions (ubuntu-latest)
- downloader: aria2c (16 connections per task)
- storage: google drive (via rclone)
- automation: cron schedule (00:00 utc+7 daily)

## directory structure
- `Linux-Distros/Arch-Based`: rolling release and arch-derived systems
- `Linux-Distros/Debian-Based`: debian, ubuntu, and stable ecosystem
- `Security-Pentest`: security auditing and penetration testing tools
- `Recovery-Tools`: system maintenance and disk utilities
- `Virtualization`: hypervisors and storage solutions

## prerequisites
- rclone configuration stored in github secrets (`RCLONE_CONF_DATA`)
- private repository setting (mandatory due to credential exposure in logs)
- sufficient google drive quota (target: 400gb+)

## automation logic
1. checkout repository and initialize environment.
2. configure rclone with encrypted secret data.
3. verify existing files on remote storage to prevent redundant transfers.
4. fetch missing assets to local ephemeral storage.
5. move verified assets to remote destination.
6. cleanup local workspace and session files.

## maintenance
- update `src/distros.py` database to reflect upstream version changes.
- monitor github action logs for code 3 (broken links) or code 9 (storage limits).
- rotate rclone tokens if authentication failures occur.

## contact
dm via instagram for system inquiries or emergency manual override.
