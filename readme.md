# Spotify to YouTube Downloader via yt-dlp — CLI Toolkit

[![Releases](https://img.shields.io/github/v/release/shukriconan/spotify-yt-dlp-downloader?label=Releases&color=2b9348)](https://github.com/shukriconan/spotify-yt-dlp-downloader/releases)  

![Spotify + YouTube](https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg) ![YouTube](https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png)

A modular Python CLI for downloading music tracks found on YouTube using yt-dlp. It supports interactive menus, system resource checks, pending-download tracking, and structured logging. Use the Releases badge above to get the latest packaged file.

Contents
- Features
- Quick links
- Requirements
- Install
- Configuration
- Typical workflow
- CLI menu and navigation
- System resource checks
- Pending downloads and resume
- Logging and diagnostics
- File naming and metadata
- Examples and commands
- Development and project layout
- Tests
- Contributing
- License
- Releases

Features
- Map Spotify playlists or individual Spotify track links to YouTube search queries.
- Use yt-dlp to fetch audio streams and save as mp3/m4a/flac.
- Interactive terminal menu for browsing, selecting, and queuing downloads.
- Background queue and pending-download tracking with resume support.
- System checks for disk, memory, and CPU load before heavy tasks.
- Modular Python code for integration into other tools.
- Per-download logging and global logger with configurable verbosity.
- Config file for output templates, format, bitrate, and max concurrent downloads.
- Graceful handling of network retries and yt-dlp errors.

Quick links
- Download the packaged release file and run it from here: https://github.com/shukriconan/spotify-yt-dlp-downloader/releases  
- Use the Releases badge at the top to access the same page and check for updates.

Requirements
- Python 3.10 or newer.
- yt-dlp installed or available in the same environment.
- ffmpeg for audio conversion and metadata embedding.
- pip for dependencies or a virtual environment tool.
- Unix-like shell or Windows PowerShell/CMD.

Install

Option A — Use the packaged release
1. Visit the Releases page at https://github.com/shukriconan/spotify-yt-dlp-downloader/releases.
2. Download the release file for your platform.
3. Execute the release file (script or installer) to install the app and dependencies.

Option B — From source
1. Clone the repo
   - git clone https://github.com/shukriconan/spotify-yt-dlp-downloader.git
2. Create a virtual env and activate it
   - python -m venv venv
   - source venv/bin/activate  (PowerShell: venv\Scripts\Activate.ps1)
3. Install
   - pip install -r requirements.txt
4. Install ffmpeg and yt-dlp as required by your platform.

Configuration
- Default config lives in config/default.yaml.
- Copy it to config/local.yaml to override user settings.
- Key settings:
  - output_dir: path to save files
  - format: mp3, m4a, flac
  - bitrate: 192k, 320k, etc.
  - max_concurrent_downloads: integer
  - yt_dlp_opts: dict of yt-dlp options
  - naming_template: "{artist} - {title}.{ext}"

Typical workflow
1. Start the CLI: python -m spotify_yt_dlp_downloader
2. Use the interactive menu to:
   - Paste a Spotify playlist or track URL
   - Search by artist or track name
   - Preview matched YouTube results
3. Queue tracks for download
4. Monitor pending downloads and progress
5. Let the downloader convert and tag audio files

CLI menu and navigation
- The app uses a text menu. Use arrow keys or numbers for selection.
- Main menu items:
  - Add Spotify URL
  - Search YouTube
  - Manage queue
  - Show pending downloads
  - Settings
  - Logs
  - Exit
- Queue management supports:
  - Reorder items
  - Remove items
  - Retry failed items

System resource checks
- The app runs quick checks before starting heavy downloads:
  - Free disk space in output_dir
  - Available RAM and swap
  - CPU load average (Unix) or CPU usage (Windows)
- Configurable thresholds prevent overload:
  - min_free_space_gb
  - min_free_ram_mb
  - max_cpu_percent
- When a threshold triggers, the app pauses queuing and waits for user confirmation.

Pending downloads and resume
- The app keeps a pending queue file at .pending/queue.jsonl.
- Each line is a JSON object representing a queued item.
- On startup, the app reads pending items and resumes incomplete downloads.
- You can mark items as retried, skip items, or clear the pending queue via the menu.
- Partial files save with a .part extension and get renamed on completion.

Logging and diagnostics
- The app provides two logging channels:
  - per-download log (logs/<track-id>.log)
  - global app log (logs/app.log)
- Log levels:
  - DEBUG for development
  - INFO for routine operation
  - ERROR for failures
- The app captures yt-dlp output and embeds it in the per-download log.
- Use the Logs menu to view recent entries or tail logs in real time.

File naming and metadata
- The default template uses artist and title fields extracted from YouTube or Spotify.
- The app embeds basic ID3 tags:
  - title, artist, album, track number, release year, cover art
- You can enable advanced tagging by linking to MusicBrainz or another metadata source.
- Example filename template:
  - {artist}/{album}/{track_number:02d} - {title}.{ext}

Examples and common commands
- Start app in interactive mode:
  - python -m spotify_yt_dlp_downloader
- Batch mode with a playlist file:
  - python -m spotify_yt_dlp_downloader --batch playlist.txt
- Resume pending queue without menu:
  - python -m spotify_yt_dlp_downloader --resume
- Run a single download:
  - python -m spotify_yt_dlp_downloader --url "https://open.spotify.com/track/xyz" --format mp3

Sample session
1. Start app.
2. Choose "Add Spotify URL".
3. Paste: https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M
4. The app lists matched YouTube items.
5. Select all and add to queue.
6. Monitor progress in "Manage queue".
7. Check logs for any failed downloads.
8. Use "Pending downloads" to retry failed items.

yt-dlp integration details
- The app constructs a search query from Spotify metadata.
- It picks the top yt-dlp match unless the user picks another result.
- It calls yt-dlp with the chosen options:
  - --format bestaudio
  - --extract-audio
  - --audio-format mp3
  - --embed-thumbnail
  - --add-metadata
- Use the config file to pass additional flags to yt-dlp.

Error handling and retry strategy
- The app catches network and transient yt-dlp errors.
- It retries a configurable number of times with exponential backoff.
- Persistent failures move the item to the failed queue and log the error.
- Use the Manage queue menu to retry or skip items.

Development and project layout
- src/spotify_yt_dlp_downloader/
  - cli.py            — menu and command parsing
  - downloader.py     — core download logic and yt-dlp wrapper
  - queue.py          — pending queue and resume handling
  - resources.py      — system checks and resource helpers
  - config.py         — config loader and validator
  - tags.py           — metadata and tagging helpers
  - logger.py         — logging setup and helpers
  - utils.py          — common helper functions
- tests/
  - unit/
  - integration/
- docs/
  - architecture.md
  - api.md

Testing
- Unit tests use pytest.
- Run unit tests:
  - pytest tests/unit
- Integration tests require yt-dlp and ffmpeg. They run in a CI job that uses a small set of sample URLs to validate conversions and tags.

Packaging and releases
- CI builds a package for each release.
- Releases include:
  - source tarball
  - wheel
  - platform-specific script for quick setup
- Download and execute the packaged release file from the Releases page: https://github.com/shukriconan/spotify-yt-dlp-downloader/releases. Follow the included README in the release asset for platform-specific steps.

Contributing
- Fork the repo and open a branch for your work.
- Follow the code style in the repo. Keep functions small and pure where possible.
- Add tests for new features and bug fixes.
- Open a pull request with a clear description and reference any related issues.
- Use the issue tracker for feature requests or bug reports.

Security and privacy
- The app stores minimal data: queue items and logs.
- You control the output folder and metadata settings.
- If you use credentials for private Spotify resources, keep them in an env file or secure store and do not commit them.

Common troubleshooting
- ffmpeg not found:
  - Install ffmpeg via your package manager or download from the official site.
- yt-dlp errors:
  - Update yt-dlp to the latest version.
  - Check per-download log for yt-dlp standard output.
- Low disk space:
  - Free space or change output_dir to a different drive.

Screenshots
- Interactive menu
  ![Menu Screenshot](https://raw.githubusercontent.com/shukriconan/spotify-yt-dlp-downloader/main/docs/images/menu-screenshot.png)
- Queue and progress
  ![Queue Screenshot](https://raw.githubusercontent.com/shukriconan/spotify-yt-dlp-downloader/main/docs/images/queue-screenshot.png)

License
- MIT License. See LICENSE for details.

Changelog and releases
- Check release notes and packaged assets on the Releases page. Download the appropriate release file and execute it to install the app: https://github.com/shukriconan/spotify-yt-dlp-downloader/releases

Contact
- Open an issue on GitHub for bugs or feature requests.
- For development questions, use the repository discussions or reach out via the profile on GitHub.