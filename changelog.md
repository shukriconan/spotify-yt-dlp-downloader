## Changelog

All notable changes to this project will be documented in this file.


### 0.1.0 - 2025-AUG-09

### Added
- Support for importing playlists from Spotify’s playlist files.
- Option to download entire playlists in bulk or pick individual playlists.
- New interactive menu system replacing numbered menus.

### Changed
- Menus are now organized into their own sub-directory (`menus/`) for better project structure.
- Playlist import removed as it wasn't working, switched with new playlist file usage directly

### Fixed
- Bug fix: program no longer crashes when `failed_downloads.json` is empty.
- Bug fix: Weird behavior when no song or artist name are given when searching for a track
- Bug fix: "Unknown Artist" used when no artist name is given