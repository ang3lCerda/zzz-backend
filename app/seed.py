import json
import asyncio
from db import (
    drive_discs_collection,
    weapons_collection,
    characters_collection,
)


def load_json(filename: str):
    try:
        with open(filename) as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return {}


async def seed_collection(
    *,
    collection,
    json_path: str,
    label: str,
):
    raw = load_json(json_path)
    data_list = list(raw.values()) if isinstance(raw, dict) else raw

    if not data_list:
        print(f"No {label} to insert!")
        return

    # Clear existing data
    await collection.delete_many({})

    for i, doc in enumerate(data_list):
    
        doc["old_id"] = doc.get("Id")

        # 2. Assign the new sequential ID
        doc["Id"] = i

    # Insert the modified list
    await collection.insert_many(data_list)
    print(f"Inserted {len(data_list)} {label} ")

async def main():
    await seed_collection(
        collection=drive_discs_collection,
        json_path="app/data/drive_discs.json",
        label="drive discs",
    )

    await seed_collection(
        collection=weapons_collection,
        json_path="app/data/weapons.json",
        label="weapons",
    )

    await seed_collection(
        collection=characters_collection,
        json_path="app/data/characters.json",
        label="characters",
    )


if __name__ == "__main__":
    asyncio.run(main())
