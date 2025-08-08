import os
from utils.logger import log_info

def check_downloaded_files(output_dir, tracks):
    downloaded = []
    pending = []
    existing_files = set(os.listdir(output_dir))

    for track in tracks:
        filename = f"{track['artist']} - {track['track']}.mp3".replace("/", "-")
        if filename in existing_files:
            downloaded.append(track)
        else:
            pending.append(track)

    log_info(f"Downloaded: {len(downloaded)} tracks, Pending: {len(pending)} tracks")
    return len(downloaded), pending
