import os
import subprocess
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
from utils import log_info, log_success, log_error
from tqdm import tqdm

def download_track(artist, track, output_dir, audio_format, sleep_between):
    query = f"{artist} - {track}"
    filename = query.replace("/", "-")

    log_info(f"Starting download: {query}")
    cmd = [
        "yt-dlp",
        f"ytsearch1:{query}",
        "-x",
        "--audio-format", audio_format,
        "-o", os.path.join(output_dir, f"{filename}.%(ext)s")
    ]

    try:
        process = subprocess.Popen(cmd)
        process.wait()
        if process.returncode == 0:
            log_success(f"Downloaded successfully: {query}")
        else:
            log_error(f"Failed to download: {query}")
    except Exception as e:
        log_error(f"Error downloading {query}: {e}")

    time.sleep(sleep_between)


# Worker function for a single track
def _download_worker(artist, track, output_dir, audio_format):
    query = f"{artist} - {track}"
    filename = query.replace("/", "-")

    cmd = [
        "yt-dlp",
        f"ytsearch1:{query}",
        "-x",
        "--audio-format", audio_format,
        "-o", os.path.join(output_dir, f"{filename}.%(ext)s"),
        "--quiet"
    ]

    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()
        if process.returncode == 0:
            log_success(f"Downloaded: {query}")
        else:
            log_error(f"Failed: {query}")
    except Exception as e:
        log_error(f"Error downloading {query}: {e}")


# Async batch downloader
async def batch_download(tracks, output_dir, audio_format, max_workers=4):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        tasks = []
        with tqdm(total=len(tracks), desc="Downloading", unit="track") as pbar:
            for track in tracks:
                artist = track["artist"].strip()
                song = track["track"].strip()
                task = loop.run_in_executor(executor, _download_worker, artist, song, output_dir, audio_format)
                task.add_done_callback(lambda _: pbar.update(1))
                tasks.append(task)
            await asyncio.gather(*tasks)