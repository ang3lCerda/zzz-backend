import requests
import json

def fetch_and_save_character(char_id: int, filename="character.json"):
    url = f"https://api.hakush.in/zzz/data/en/character/{char_id}.json"
    response = requests.get(url)
    response.raise_for_status()  # ensure no HTTP errors

    data = response.json()

    with open(filename, "w", encoding="utf-8", errors="ignore") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Saved character data to {filename}")

if __name__ == "__main__":
    fetch_and_save_character(1331)
