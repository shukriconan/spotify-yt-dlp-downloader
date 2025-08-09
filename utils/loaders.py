from utils.logger import log_info, log_warning, log_error

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
