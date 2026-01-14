import requests
import json
url = "https://api.hakush.in/zzz/data/equipment.json"

base= "https://api.hakush.in/zzz/data/en/equipment/"
ui_base = "https://api.hakush.in/zzz/UI/"
resp = requests.get(url)

if resp.status_code != 200:
    raise RuntimeError(f"Error fetching data: {resp.status_code}")

data = resp.json()

def extract_ids(data, as_int=True, sort_ids=True):
    ids = data.keys()

    if as_int:
        ids = (int(k) for k in ids)

    ids = list(ids)
    if sort_ids:
        ids.sort()
    return ids

ids=extract_ids(data)


def get_all_drive_discs(ids, output_file="drive_discs.json"):
    all_discs = {}

    for disc_id in ids:
        url = f"{base}{disc_id}.json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "Icon" in data:
            filename = data["Icon"].split("/")[-1].split(".")[0]

            data["Icon"] = f"{ui_base}{filename}.webp"

        data.pop("Icon2", None)
        data.pop("Id",None)

        all_discs[str(disc_id)] = data

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_discs, f, ensure_ascii=False, indent=2)

    return all_discs
get_all_drive_discs(ids)
