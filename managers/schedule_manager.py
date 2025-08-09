import schedule
import time
from utils.logger import log_info, log_error
from downloader.base_downloader import batch_download
import asyncio
from utils.loaders import load_tracks, load_playlists

def schedule_download(config):
    time_str = input("Enter time to schedule download (HH:MM, 24h): ").strip()

    def job():
        from utils.track_checker import check_downloaded_files
        tracks = load_tracks(config["tracks_file"])
        _, pending = check_downloaded_files(config["output_dir"], tracks)
        if not pending:
            log_info("No pending downloads for scheduled job.")
            return
        log_info("Starting scheduled batch download...")
        asyncio.run(batch_download(pending, config["output_dir"], config["audio_format"]))

    try:
        schedule.every().day.at(time_str).do(job)
        log_info(f"Scheduled daily download at {time_str}. Press Ctrl+C to stop.")
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        log_error(f"Error scheduling download: {e}")

def load_tracks(tracks_file):
    import json
    try:
        with open(tracks_file, "r", encoding="utf-8") as f:
            return json.load(f)["tracks"]
    except Exception as e:
        log_error(f"Error loading tracks file: {e}")
        return []


def load_playlists(playlists_file):
    import json
    try:
        with open(playlists_file, "r", encoding="utf-8") as f:
            return json.load(f)["playlists"]
    except Exception as e:
        log_error(f"Error loading playlists file: {e}")
        return []
