import os
import hashlib
from datetime import datetime
import requests

url = "https://www.skku.edu/skku/campus/support/welfare_11.do?mode=info&conspaceCd=10201030&srResId=1&srShowTime=W&srCategory=L"
import urllib.parse

os.makedirs("menus", exist_ok=True)

resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
resp.raise_for_status()

parsed = urllib.parse.urlparse(url)
base_name = (parsed.netloc + parsed.path).replace("/", "_").strip("_")
short_hash = hashlib.md5(url.encode("utf-8")).hexdigest()[:8]
timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
filename = f"{base_name}_{timestamp}_{short_hash}.html"

filepath = os.path.join("menus", filename)
with open(filepath, "wb") as f:
    f.write(resp.content)

print(f"Saved {filepath}")