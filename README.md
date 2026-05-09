# os-deployment-library

### overview
automated iso mirroring system designed to synchronize multiple operating system distributions to google drive storage. the system utilizes github actions for scheduled execution, aria2 for multi-threaded downloads, and rclone for cloud storage synchronization.

### project structure
- `src/distros.py`: primary database containing iso names, urls, and sizes.
- `src/scripts/sync.py`: core operational script for downloading and cloud syncing.
- `src/scripts/refactor.py`: maintenance tool for database sorting and de-duplication.
- `.github/workflows/daily_sync.yml`: automated workflow configuration.

### infrastructure
- runtime: github actions (ubuntu-latest)
- downloader: aria2c (optimized with 16 connections)
- storage: google drive (via rclone)
- automation: cron schedule (00:00 utc+7 daily)

### rclone configuration setup
to enable cloud synchronization, you must provide your rclone configuration as a base64 encoded secret.

1. **generate configuration**: run `rclone config` on your local machine to set up your google drive remote (ensure the remote name matches `remote_name` in `src/scripts/sync.py`).
2. **locate config file**: find the path to your `rclone.conf` by running:
   ```bash
   rclone config file
   ```
3. **encode to base64**: convert the file content to a base64 string (without line breaks):
   ```bash
   # linux / mac
   base64 -w 0 <path_to_rclone.conf>
   ```
4. **add to github secrets**:
   - go to your repository on github.
   - navigate to **settings** > **secrets and variables** > **actions**.
   - create a **new repository secret** named `RCLONE_CONF_DATA`.
   - paste the generated base64 string as the value.

### prerequisites
- rclone configuration: must be converted to **base64** and stored in github secrets as `RCLONE_CONF_DATA`.
- storage quota: ensure target drive has 400gb+ available space.
- private repo: mandatory to prevent accidental credential leakage in logs.

### manual execution
to run the synchronization locally:
```bash
# update database formatting/sorting
python3 src/scripts/refactor.py

# run sync process
python3 src/scripts/sync.py
```

### automation logic
1. checkout repository & setup python environment.
2. restore `rclone.conf` from base64 secret.
3. parse `src/distros.py` and verify remote file existence.
4. fetch missing assets via `aria2c` to ephemeral runner storage.
5. stream/move verified assets to gdrive destination.
6. perform exhaustive cleanup of local temp files.

### maintenance
- database: update `src/distros.py` when new upstream versions are released.
- logs: check github actions for exit code 3 (broken links) or code 9 (disk full).
- security: rotate rclone tokens if authentication errors occur.

### contact
dm via instagram for system inquiries or emergency manual override.

---

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.
