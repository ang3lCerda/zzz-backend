import requests
import json

url = "https://api.hakush.in/zzz/data/weapon.json"
resp = requests.get(url)
data = resp.json()

base = "https://api.hakush.in/zzz/UI/"
keys_to_remove = ["KO", "CHS", "JA","desc"]

for weapon_id in data:
    weapon_data = data[weapon_id]

    if "icon" in weapon_data:
        weapon_data["icon"] = f"{base}{weapon_data['icon']}.png" 

    for key in keys_to_remove:
        weapon_data.pop(key, None)

with open("weapons.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

