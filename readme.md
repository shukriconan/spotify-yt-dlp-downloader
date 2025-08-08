# 🎶 Music Downloader CLI

A modular, Python-based command-line application for downloading music from YouTube using **yt-dlp**.
Supports interactive menu navigation, system resource checks, pending download tracking, and logging.

---

## 📌 Features

* **Interactive menu** with multiple actions (download all, single track, check status, etc.)
* **Configurable settings** in `config.json`
* **Tracks loaded from JSON file**
* **System resource checks** (CPU, RAM, storage)
* **Checks already downloaded vs. pending tracks**
* **Download by artist and song name** directly from the menu
* **Colorful terminal logs** (via `colorama`)
* **Logging to `app.log`** for persistent history
* **Modular code structure** for easier maintenance

---

## 📂 Project Structure

```
music_downloader/
│
├── main.py            # Entry point with menu
├── config.py          # Loads config from config.json
├── utils.py           # Utility functions (logging, system check, file check)
├── downloader.py      # Download logic
├── prototype.py       # Standalone version, runs sequentially
├── requirements.txt   # Dependencies
├── config.json        # User-configurable settings
└── tracks.json        # Your list of tracks
```

---

## ⚙️ Installation

1. **Clone the repository**:

```bash
git clone https://github.com/Ssenseii/spotify_downloader.git
cd music_downloader
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Ensure `yt-dlp` is installed**:
cd ../../
```bash
pip install yt-dlp
```

---

## 📄 Configuration

Edit `config.json` to set your preferences:

```json
{
    "json_file": "tracks.json",
    "output_dir": "music",
    "audio_format": "mp3",
    "sleep_between": 5,
    "average_download_time": 20
}
```

---

## 🎵 Track List Format

`tracks.json` should contain:

```json
{
    "tracks": [
        { "artist": "Artist Name", "track": "Song Title" },
        { "artist": "Another Artist", "track": "Another Song" }
    ]
}
```

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

You will see a **menu**:

```
=== Music Downloader Menu ===
1. Download all pending tracks
2. Check downloaded files
3. Download a single track
4. System check
5. Help
6. Exit
```

---

## 🛠 Dependencies

* [yt-dlp](https://github.com/yt-dlp/yt-dlp) – YouTube downloader
* [psutil](https://pypi.org/project/psutil/) – System resource monitoring
* [colorama](https://pypi.org/project/colorama/) – Colored terminal output

Install all:

```bash
pip install -r requirements.txt
```

---

## 📜 Logging

* **Terminal output** is colored for readability
* **`app.log`** stores a full log history of actions, warnings, and errors

---

## ⚠️ Disclaimer

This tool is for **personal use only**.
Ensure you respect copyright laws and YouTube’s terms of service.
