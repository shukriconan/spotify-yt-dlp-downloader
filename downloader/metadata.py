import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC
from utils.logger import log_info, log_error

def embed_metadata(output_dir):
    try:
        for root, _, files in os.walk(output_dir):
            for file in files:
                if not file.endswith(".mp3"):
                    continue
                filepath = os.path.join(root, file)
                try:
                    audio = EasyID3(filepath)
                except Exception:
                    audio = ID3()

                # Extract artist and title from filename format: Artist - Title.mp3
                try:
                    artist, title_ext = file.split(" - ", 1)
                    title = title_ext.rsplit(".", 1)[0]
                except Exception:
                    log_error(f"Skipping {file}: Cannot parse artist/title")
                    continue

                try:
                    audio["artist"] = artist.strip()
                    audio["title"] = title.strip()
                    audio.save(filepath)
                    log_info(f"Metadata saved for {file}")
                except Exception as e:
                    log_error(f"Failed to save metadata for {file}: {e}")

                # Optional: embed album art (if you have a .jpg file with same name)
                jpg_path = filepath.rsplit(".", 1)[0] + ".jpg"
                if os.path.exists(jpg_path):
                    try:
                        id3 = ID3(filepath)
                        with open(jpg_path, "rb") as albumart:
                            id3["APIC"] = APIC(
                                encoding=3,
                                mime="image/jpeg",
                                type=3,  # Cover(front)
                                desc="Cover",
                                data=albumart.read()
                            )
                        id3.save()
                        log_info(f"Embedded album art in {file}")
                    except Exception as e:
                        log_error(f"Failed to embed album art for {file}: {e}")

    except Exception as e:
        log_error(f"Error in embed_metadata: {e}")
