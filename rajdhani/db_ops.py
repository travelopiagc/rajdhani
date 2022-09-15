import requests
from pathlib import Path

from .config import db_path, db_init_url


def init_db():
    download_file(db_init_url, db_path)


def reset_db():
    Path(db_path).unlink(missing_ok=True)
    init_db()


def ensure_db():
    if not Path(db_path).is_file():
        init_db()


def download_file(url, location):
    response = requests.get(url)
    with open(location, "wb") as f:
        f.write(response.content)
