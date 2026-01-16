import json
import asyncio
from db import drive_discs_collection, weapons_collection  # your Motor collections

def load_json(filename):
    try:
        with open(filename) as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return {}

async def seed_drive_discs():
    raw = load_json("app/data/drive_discs.json")
    data_list = list(raw.values()) if isinstance(raw, dict) else raw

    if not data_list:
        print("No drive discs to insert!")
        return

    await drive_discs_collection.delete_many({})

    # Build a dict keyed by Id
    wrapped = {}
    for i, doc in enumerate(data_list, start=1):
        doc["Id"] = i
        wrapped[str(i)] = doc  # wrap by Id

    await drive_discs_collection.insert_many(list(wrapped.values()))
    print(f"Inserted {len(wrapped)} drive discs with Id keys")

async def seed_weapons():
    raw = load_json("app/data/weapons.json")
    data_list = list(raw.values()) if isinstance(raw, dict) else raw

    if not data_list:
        print("No weapons to insert!")
        return

    await weapons_collection.delete_many({})

    wrapped = {}
    for i, doc in enumerate(data_list, start=1):
        doc["Id"] = i
        wrapped[str(i)] = doc

    await weapons_collection.insert_many(list(wrapped.values()))
    print(f"Inserted {len(wrapped)} weapons")

async def main():
    await seed_drive_discs()
    await seed_weapons()

if __name__ == "__main__":
    asyncio.run(main())
