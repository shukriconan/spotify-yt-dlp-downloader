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


"""
    Checks which playlists and tracks have already been downloaded.
    Returns:
        downloaded_playlists: list of dicts with playlist info and downloaded tracks
        pending_playlists: list of dicts with playlist info and pending tracks
    """
def check_downloaded_playlists(output_dir, playlists):

    downloaded_playlists = []
    pending_playlists = []

    for pl in playlists:
        playlist_name = pl["name"]
        sanitized_name = playlist_name.replace("/", "-").strip()
        playlist_dir = os.path.join(output_dir, sanitized_name)

        tracks = [
            {
                "artist": item["track"]["artistName"],
                "track": item["track"]["trackName"]
            }
            for item in pl.get("items", [])
            if item.get("track")
        ]

        if not os.path.exists(playlist_dir):
            log_info(f"Playlist folder missing: {playlist_name}")
            pending_playlists.append({
                "name": playlist_name,
                "tracks": tracks
            })
            continue

        existing_files = set(os.listdir(playlist_dir))
        downloaded_tracks = []
        pending_tracks = []

        for track in tracks:
            filename = f"{track['artist']} - {track['track']}.mp3".replace("/", "-")
            if filename in existing_files:
                downloaded_tracks.append(track)
            else:
                pending_tracks.append(track)

        log_info(f"{playlist_name} → Downloaded: {len(downloaded_tracks)}, Pending: {len(pending_tracks)}")

        if pending_tracks:
            pending_playlists.append({
                "name": playlist_name,
                "tracks": pending_tracks
            })
        else:
            downloaded_playlists.append({
                "name": playlist_name,
                "tracks": downloaded_tracks
            })

    return downloaded_playlists, pending_playlists