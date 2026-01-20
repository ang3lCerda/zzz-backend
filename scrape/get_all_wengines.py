import requests
import json

url = "https://api.hakush.in/zzz/data/weapon.json"
base = "https://api.hakush.in/zzz/data/en/weapon/"
resp = requests.get(url)
data = resp.json()
ui_base = "https://api.hakush.in/zzz/UI/"


def extract_ids(data, as_int=True, sort_ids=True):
    ids = data.keys()

    if as_int:
        ids = (int(k) for k in ids)

    ids = list(ids)
    if sort_ids:
        ids.sort()
    return ids


ids = extract_ids(data)


def get_all_wengines(ids, output_file="weapons.json"):
    all_wengines = {}

    for id in ids:
        url = f"{base}{id}.json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "Icon" in data:
            filename = data["Icon"].split("/")[-1].split(".")[0]

            data["Icon"] = f"{ui_base}{filename}.webp"

        all_wengines[str(id)] = data

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_wengines, f, ensure_ascii=False, indent=2)

    return all_wengines


get_all_wengines(ids)
