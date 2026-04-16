import time
import requests
from config import REQUEST_TIMEOUT, MAX_RETRIES

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

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