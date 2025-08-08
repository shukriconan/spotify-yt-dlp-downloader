import os
import psutil
import logging
from colorama import Fore, Style, init

init(autoreset=True)

def setup_logging():
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def log_info(msg):
    print(Fore.CYAN + msg)
    logging.info(msg)

def log_success(msg):
    print(Fore.GREEN + msg)
    logging.info(msg)

def log_error(msg):
    print(Fore.RED + msg)
    logging.error(msg)

def log_warning(msg):
    print(Fore.YELLOW + msg)
    logging.warning(msg)

def system_check():
    """Check RAM, CPU, and Storage availability."""
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    cpu_percent = psutil.cpu_percent(interval=1)

    log_info(f"CPU Usage: {cpu_percent}%")
    log_info(f"RAM Available: {ram.available // (1024*1024)} MB")
    log_info(f"Disk Free: {disk.free // (1024*1024*1024)} GB")

    if ram.available < 200*1024*1024:  # less than 200MB
        log_warning("Low RAM available. Downloads might fail.")
    if disk.free < 1*1024*1024*1024:  # less than 1GB
        log_warning("Low disk space available.")

def check_downloaded_files(output_dir, tracks):
    """Return tuple: (downloaded_count, pending_tracks)"""
    downloaded = []
    pending = []
    existing_files = set(os.listdir(output_dir))

    for track in tracks:
        filename = f"{track['artist']} - {track['track']}.mp3".replace("/", "-")
        if filename in existing_files:
            downloaded.append(track)
        else:
            pending.append(track)

    return len(downloaded), pending
