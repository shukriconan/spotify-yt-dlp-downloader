# 🎶 Potty

A modular, Python-based command-line tool for downloading music from Spotify using **yt-dlp**.  
Features interactive menus, system checks, download management, metadata embedding, and robust logging.

---

## 📌 Features

- **Interactive CLI menus** for downloads, management, and automation
- **Configurable settings** in `config.json`
- **Track management** via JSON files (pending, failed, history)
- **System resource checks** (CPU, RAM, storage)
- **Download by artist and song name**
- **Batch and single downloads**
- **Playlist import** and metadata embedding
- **Retry failed downloads**
- **Duplicate detection and file organization**
- **Colorful terminal logs** (via `colorama`)
- **Persistent logging** to `app.log`
- **Modular, maintainable codebase**

---

## 📂 Project Structure

```
spotify-ytdlp/
│
├── main.py                # Entry point, interactive menus
├── config.py              # Loads config from config.json
├── config.json            # User-configurable settings
├── requirements.txt       # Dependencies
├── app.log                # Log file
├── todo.md                # Development notes
│
├── data/
│   ├── tracks.json            # Track list (with artist, album, track, uri)
│   ├── failed_downloads.json  # Tracks that failed to download
│   └── download_history.json  # Downloaded tracks history
│
├── downloader/
│   ├── base_downloader.py     # Download logic (single, batch)
│   ├── playlist_import.py     # Import playlists
│   ├── metadata.py            # Embed metadata
│   ├── retry_manager.py       # Retry failed downloads
│   └── __init__.py
│
├── managers/
│   ├── file_manager.py        # Duplicate detection, file organization
│   ├── resume_manager.py      # Resume batch downloads
│   ├── schedule_manager.py    # Scheduled downloads
│   └── __init__.py
│
├── utils/
│   ├── logger.py              # Logging utilities
│   ├── system.py              # System resource checks
│   ├── track_checker.py       # Check downloaded files
│   └── __init__.py
│
└── music/                 # Downloaded music files
```

---

## ⚙️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Ssenseii/spotify-yt-dlp-downloader.git
   cd spotify-ytdlp
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure `yt-dlp` is installed**:

   ```bash
   pip install yt-dlp
   ```

---

## 📄 Configuration

Edit `config.json` to set your preferences:

```json
{
	"json_file": "data/tracks.json",
	"output_dir": "music",
	"audio_format": "mp3",
	"sleep_between": 5,
	"average_download_time": 20
}
```

---

## 🎵 Track List Format

`data/tracks.json` should contain:

```json
{
	"tracks": [
		{
			"artist": "Artist Name",
			"album": "Album Name",
			"track": "Song Title",
			"uri": "spotify:track:xxxx"
		}
	]
}
```

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

You will see a menu with options for downloading, checking files, importing playlists, retrying failed downloads, and more.

---

## 🛠 Dependencies

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) – YouTube downloader
- [psutil](https://pypi.org/project/psutil/) – System resource monitoring
- [colorama](https://pypi.org/project/colorama/) – Colored terminal output

Install all:

```bash
pip install -r requirements.txt
```

---

## 📜 Logging

- **Terminal output** is colored for readability
- **`app.log`** stores a full log history of actions, warnings, and errors

---

## ⚠️ Disclaimer

This tool is for **personal use only**.  
Ensure you respect copyright laws and YouTube’s terms.
