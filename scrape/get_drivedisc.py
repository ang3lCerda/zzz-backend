import requests
from pprint import pprint
import json

url = "https://api.hakush.in/zzz/data/equipment.json"
resp = requests.get(url)

if resp.status_code != 200:
    raise RuntimeError(f"Error fetching data: {resp.status_code}")

data = resp.json()


for disc in data.values():
    disc_keys = list(disc.keys())
    for key in disc_keys:
        if key not in {"icon", "EN"}:
            del disc[key]

for disc in data.values():
    en = disc.pop("EN", None)
    if en:
        disc.update(en)



with open("drive_discs.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)