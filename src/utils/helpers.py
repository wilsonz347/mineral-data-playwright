import time
import requests
from config import REQUEST_TIMEOUT, MAX_RETRIES
from pathlib import Path
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

CHECKPOINT_FILE = Path("/tmp/policy_checkpoint.json")

session = requests.Session()
session.headers.update(HEADERS)

def clean(text):
    return " ".join(text.split()) if text else ""

def safe_get(url, retries=MAX_RETRIES, timeout=REQUEST_TIMEOUT):
    for attempt in range(retries):
        try:
            resp = session.get(url, timeout=timeout)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            print(f"  [retry {attempt + 1}] {url} — {e}")
            time.sleep(2 ** attempt)
    return None

def load_checkpoint():
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE, "r", encoding="utf-8") as f:
            return set(tuple(x) for x in json.load(f))
    return set()


def save_checkpoint(done):
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump([list(x) for x in sorted(done)], f)
