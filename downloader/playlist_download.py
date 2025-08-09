import os
import json
from utils.logger import log_info, log_error, log_success
from downloader.base_downloader import batch_download

"""
Downloads all pending tracks for a given playlist.
Creates the playlist folder if it doesn't exist.
"""
async def download_playlist(playlist_name, tracks, output_dir, audio_format, sleep_between):
    sanitized_name = playlist_name.replace("/", "-").strip()
    playlist_dir = os.path.join(output_dir, sanitized_name)

    os.makedirs(playlist_dir, exist_ok=True)

    log_info(f"Downloading playlist: {playlist_name} → {len(tracks)} tracks")

    # Format track dict for batch_download
    formatted_tracks = [
        {"artist": t["artist"], "track": t["track"]}
        for t in tracks
    ]

    await batch_download(formatted_tracks, playlist_dir, audio_format)
    log_success(f"Finished downloading playlist: {playlist_name}")
