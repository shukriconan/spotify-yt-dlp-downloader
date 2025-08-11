import os
import json
from downloader.base_downloader import download_track
from utils.logger import log_info, log_error
from constants import FAILED_FILE

def retry_failed(config):
    if not os.path.exists(FAILED_FILE):
        log_info("No failed downloads to retry.")
        return

    try:
        with open(FAILED_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:  # File exists but is empty
                log_info("No failed downloads.")
                return
            failed_tracks = json.loads(content)
    except json.JSONDecodeError:
        log_error("Failed downloads file is corrupted or invalid JSON.")
        return

    if not failed_tracks:
        log_info("No failed downloads.")
        return

    log_info(f"Retrying {len(failed_tracks)} failed downloads...")
    still_failed = []

    for t in failed_tracks:
        try:
            download_track(t["artist"], t["track"], config["output_dir"], config["audio_format"], config["sleep_between"])
        except Exception as e:
            log_error(f"Retry failed: {t} - {e}")
            still_failed.append(t)

    with open(FAILED_FILE, "w", encoding="utf-8") as f:
        json.dump(still_failed, f, indent=2)