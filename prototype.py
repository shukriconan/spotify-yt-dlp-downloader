# Standalone version, once you run it
# It'll automatically download tracks from a JSON file
# using yt-dlp and save them in a specified folder.


import json
import subprocess
import time
import os
import math

# ===== CONFIG =====
JSON_FILE = "tracks.json"
OUTPUT_DIR = "music"
AUDIO_FORMAT = "mp3"
SLEEP_BETWEEN = 5  # seconds between downloads
AVERAGE_DOWNLOAD_TIME = 20  # estimated seconds per track (adjust if needed)
# ==================

# Create music folder if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load track list
with open(JSON_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

total_tracks = len(data["tracks"])

# Estimate total time
estimated_total_seconds = (AVERAGE_DOWNLOAD_TIME + SLEEP_BETWEEN) * total_tracks
estimated_minutes = math.ceil(estimated_total_seconds / 60)

print(f"\n🎵 Found {total_tracks} tracks in {JSON_FILE}")
print(f"📂 Output folder: {OUTPUT_DIR}")
print(f"⏳ Estimated total time: ~{estimated_minutes} minutes "
      f"({AVERAGE_DOWNLOAD_TIME + SLEEP_BETWEEN} sec per track)")
print("=" * 50, "\n")

# Loop through tracks
for i, entry in enumerate(data["tracks"], start=1):
    artist = entry['artist'].strip()
    track = entry['track'].strip()
    query = f"{artist} - {track}"
    filename = f"{artist} - {track}".replace("/", "-")  # avoid folder issues

    print(f"[{i}/{total_tracks}] 🎶 Starting download: {query}")

    # yt-dlp command
    cmd = [
        "yt-dlp",
        f"ytsearch1:{query}",
        "-x",
        "--audio-format", AUDIO_FORMAT,
        "-o", os.path.join(OUTPUT_DIR, f"{filename}.%(ext)s")
    ]

    print(f"🔍 Searching & downloading from YouTube...")
    print(f"💾 Saving as {filename}.{AUDIO_FORMAT} in {OUTPUT_DIR}/")
    print("-" * 50)

    # Run command and stream output directly to terminal
    process = subprocess.Popen(cmd)
    process.wait()  # Wait until finished

    if process.returncode == 0:
        print(f"✅ Downloaded successfully: {query}")
    else:
        print(f"❌ Failed to download: {query}")

    print("-" * 50)
    time.sleep(SLEEP_BETWEEN)

print("\n🎉 All downloads completed!")
