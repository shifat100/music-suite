
import json
import os
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
AUDIO_DIR = ROOT / "audio"

REPO = os.getenv("GITHUB_REPOSITORY", "shifat100/music-suite")
BRANCH = os.getenv("GITHUB_REF_NAME", "main")

AUDIO_EXTENSIONS = {
    ".mp3", ".opus", ".ogg", ".wav",
    ".flac", ".m4a", ".aac", ".wma"
}


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w]+", "_", text)
    return text.strip("_")


def get_metadata(file_path):
    title = file_path.stem
    artist = "Unknown Artist"

    # Recognize filenames such as:
    # Arash feat. Helena - Broken Angel.mp3
    if " - " in title:
        possible_artist, possible_title = title.split(" - ", 1)
        if possible_artist.strip() and possible_title.strip():
            artist = possible_artist.strip()
            title = possible_title.strip()

    return title, artist


def get_raw_url(file_path):
    relative_path = file_path.relative_to(ROOT).as_posix()
    encoded_path = quote(relative_path, safe="/")
    return (
        f"https://raw.githubusercontent.com/"
        f"{REPO}/{quote(BRANCH, safe='')}/{encoded_path}"
    )


def generate_databases():
    if not AUDIO_DIR.is_dir():
        raise FileNotFoundError(f"Audio directory not found: {AUDIO_DIR}")

    folders = sorted(
        folder
        for folder in AUDIO_DIR.rglob("*")
        if folder.is_dir()
        and any(
            item.is_file() and item.suffix.lower() in AUDIO_EXTENSIONS
            for item in folder.iterdir()
        )
    )

    generated = 0

    for folder in folders:
        audio_files = sorted(
            (
                item for item in folder.iterdir()
                if item.is_file()
                and item.suffix.lower() in AUDIO_EXTENSIONS
            ),
            key=lambda item: item.name.lower()
        )

        category = slugify(folder.name) or "audio"
        database = []

        for index, file_path in enumerate(audio_files, start=1):
            title, artist = get_metadata(file_path)

            database.append({
                "id": f"{category}_{index}_{slugify(title)}",
                "title": title,
                "artist": artist,
                "category": category,
                "url": get_raw_url(file_path),
            })

        output_file = folder / "db.json"
        output_file.write_text(
            json.dumps(database, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

        print(f"Generated {output_file.relative_to(ROOT)} "
              f"({len(database)} audio files)")
        generated += 1

    print(f"Finished: generated {generated} database file(s).")


if __name__ == "__main__":
    generate_databases()
