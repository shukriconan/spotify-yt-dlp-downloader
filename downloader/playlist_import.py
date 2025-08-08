from utils.logger import log_info, log_error
import json

def import_playlist(url, json_file):
    try:
        # You can enhance: parse playlist using yt-dlp --flat-playlist
        log_info(f"Importing playlist from {url}")
        
        # Todo: append new tracks
        
        new_tracks = [{"artist": "Sample Artist", "track": "Sample Song"}]
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        data["tracks"].extend(new_tracks)
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        log_info("Playlist imported.")
    except Exception as e:
        log_error(f"Error importing playlist: {e}")
