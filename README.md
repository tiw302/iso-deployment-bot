# os-deployment-library

## overview
automated iso mirroring system designed to synchronize multiple operating system distributions to google drive storage. the system utilizes github actions for scheduled execution, aria2 for multi-threaded downloads, and rclone for cloud storage synchronization.

## project structure
- `src/distros.py`: primary database containing iso names, urls, and sizes.
- `src/scripts/sync.py`: core operational script for downloading and cloud syncing.
- `src/scripts/refactor.py`: maintenance tool for database sorting and de-duplication.
- `.github/workflows/daily_sync.yml`: automated workflow configuration.

## infrastructure
- runtime: github actions (ubuntu-latest)
- downloader: aria2c (optimized with 16 connections)
- storage: google drive (via rclone)
- automation: cron schedule (00:00 utc+7 daily)

## prerequisites
- rclone configuration: must be converted to **base64** and stored in github secrets as `RCLONE_CONF_DATA`.
- storage quota: ensure target drive has 400gb+ available space.
- private repo: mandatory to prevent accidental credential leakage in logs.

## manual execution
to run the synchronization locally:
```bash
# update database formatting/sorting
python3 src/scripts/refactor.py

# run sync process
python3 src/scripts/sync.py
```

## automation logic
1. checkout repository & setup python environment.
2. restore `rclone.conf` from base64 secret.
3. parse `src/distros.py` and verify remote file existence.
4. fetch missing assets via `aria2c` to ephemeral runner storage.
5. stream/move verified assets to gdrive destination.
6. perform exhaustive cleanup of local temp files.

## maintenance
- database: update `src/distros.py` when new upstream versions are released.
- logs: check github actions for exit code 3 (broken links) or code 9 (disk full).
- security: rotate rclone tokens if authentication errors occur.

## contact
dm via instagram for system inquiries or emergency manual override.
