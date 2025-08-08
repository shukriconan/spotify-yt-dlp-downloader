import asyncio
from downloader import download_track, batch_download
from utils import setup_logging, log_info, log_error, check_downloaded_files
from config import load_config
import os
import json

def load_tracks(json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            return json.load(f)["tracks"]
    except Exception as e:
        log_error(f"Error loading tracks file: {e}")
        return []

def menu():
    print("\n=== Music Downloader Menu ===")
    print("1. Download all pending tracks (sequential)")
    print("2. Download all pending tracks (BATCH async)")
    print("3. Check downloaded files")
    print("4. Download a single track")
    print("5. System check")
    print("6. Help")
    print("7. Exit")

def main():
    setup_logging()
    config = load_config()
    os.makedirs(config["output_dir"], exist_ok=True)

    while True:
        menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            tracks = load_tracks(config["json_file"])
            _, pending_tracks = check_downloaded_files(config["output_dir"], tracks)
            for track in pending_tracks:
                download_track(track["artist"], track["track"], config["output_dir"], config["audio_format"], config["sleep_between"])

        elif choice == "2":  # NEW BATCH DOWNLOAD
            tracks = load_tracks(config["json_file"])
            _, pending_tracks = check_downloaded_files(config["output_dir"], tracks)
            log_info(f"{len(pending_tracks)} tracks pending download. Starting batch mode...")
            asyncio.run(batch_download(pending_tracks, config["output_dir"], config["audio_format"], max_workers=4))

        elif choice == "3":
            tracks = load_tracks(config["json_file"])
            downloaded_count, pending_tracks = check_downloaded_files(config["output_dir"], tracks)
            log_info(f"Downloaded: {downloaded_count}")
            log_info(f"Pending: {len(pending_tracks)}")

        elif choice == "4":
            artist = input("Enter artist name: ").strip()
            song = input("Enter song name: ").strip()
            download_track(artist, song, config["output_dir"], config["audio_format"], config["sleep_between"])

        elif choice == "5":
            from utils import system_check
            system_check()

        elif choice == "6":
            log_info("This tool downloads music from YouTube using yt-dlp. Ensure yt-dlp is installed.")

        elif choice == "7":
            log_info("Exiting program...")
            break

        else:
            log_error("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
