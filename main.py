# main.py
import os
import asyncio
from config import load_config
from utils.logger import setup_logging, log_info, log_error
from utils.system import system_check
from utils.track_checker import check_downloaded_files
from downloader.base_downloader import download_track, batch_download
from downloader.retry_manager import retry_failed
from downloader.playlist_import import import_playlist
from downloader.metadata import embed_metadata
from managers.file_manager import organize_files, detect_duplicates
from managers.resume_manager import save_progress, resume_batch
from managers.schedule_manager import schedule_download

def main_menu():
    print("\n=== Music Downloader ===")
    print("1. Downloads Menu")
    print("2. Management Menu")
    print("3. Automation Menu")
    print("4. Tools Menu")
    print("5. Exit")

def downloads_menu(config):
    print("\n--- Downloads ---")
    print("1. Download all pending (sequential)")
    print("2. Download all pending (batch async)")
    print("3. Download a single track")
    print("4. Import playlist")
    print("5. Back")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        tracks = load_tracks(config["json_file"])
        _, pending = check_downloaded_files(config["output_dir"], tracks)
        for t in pending:
            download_track(t["artist"], t["track"], config["output_dir"], config["audio_format"], config["sleep_between"])

    elif choice == "2":
        tracks = load_tracks(config["json_file"])
        _, pending = check_downloaded_files(config["output_dir"], tracks)
        asyncio.run(batch_download(pending, config["output_dir"], config["audio_format"]))

    elif choice == "3":
        artist = input("Artist: ").strip()
        song = input("Song: ").strip()
        download_track(artist, song, config["output_dir"], config["audio_format"], config["sleep_between"])

    elif choice == "4":
        link = input("Enter playlist URL: ")
        import_playlist(link, config["json_file"])

def management_menu(config):
    print("\n--- Management ---")
    print("1. Retry failed downloads")
    print("2. Detect duplicates")
    print("3. Organize files by artist/album")
    print("4. Embed metadata in MP3s")
    print("5. Back")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        retry_failed(config)
    elif choice == "2":
        detect_duplicates(config["output_dir"])
    elif choice == "3":
        organize_files(config["output_dir"])
    elif choice == "4":
        embed_metadata(config["output_dir"])

def automation_menu(config):
    print("\n--- Automation ---")
    print("1. Resume paused batch download")
    print("2. Schedule a download job")
    print("3. Back")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        resume_batch(config)
    elif choice == "2":
        schedule_download(config)

def tools_menu():
    print("\n--- Tools ---")
    print("1. System check")
    print("2. Help")
    print("3. Back")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        system_check()
    elif choice == "2":
        log_info("Help: Use yt-dlp for YouTube downloads. Modify config.json to change settings.")

def load_tracks(json_file):
    import json
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            return json.load(f)["tracks"]
    except Exception as e:
        log_error(f"Error loading tracks file: {e}")
        return []

if __name__ == "__main__":
    setup_logging()
    config = load_config()
    os.makedirs(config["output_dir"], exist_ok=True)

    while True:
        main_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            downloads_menu(config)
        elif choice == "2":
            management_menu(config)
        elif choice == "3":
            automation_menu(config)
        elif choice == "4":
            tools_menu()
        elif choice == "5":
            log_info("Exiting program...")
            break
        else:
            log_error("Invalid choice.")
