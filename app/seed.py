import json
import asyncio
from db import drive_discs_collection , weapons_collection # your Motor collection

def load_json(filename):
    try:
        with open(filename) as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return {}




async def seed_drive_discs():
     # Load JSON
    with open("app/data/drive_discs.json") as f:
        raw = json.load(f)

    # Convert dict values to list if your JSON is keyed by strings
    data_list = list(raw.values()) if isinstance(raw, dict) else raw

    if not data_list:
        print("No documents to insert!")
        return

    # Clear existing collection
    await drive_discs_collection.delete_many({})

    # Assign custom incremental Id for each document
    for i, doc in enumerate(data_list, start=1):
        doc["Id"] = i  # your custom ID property
        # _id is untouched and remains ObjectId

    # Insert all documents
    await drive_discs_collection.insert_many(data_list)
    print(f"Inserted {len(data_list)} drive discs with custom Id property")

async def seed_weapons():
    with open("app/data/weapons.json") as f:
        raw = json.load(f)

    # Convert dict values to list if your JSON is keyed by strings
    data_list = list(raw.values()) if isinstance(raw, dict) else raw

    data_list = list(raw.values()) if isinstance(raw, dict) else raw

    if not data_list:
        print("No documents to insert!")
        return
    for i, doc in enumerate(data_list, start=1):
        doc["Id"] = i  # your custom ID property
    
    await weapons_collection.insert_many(data_list)
    print(f"Inserted {len(data_list)} weapons with custom Id property")

async def main():
    await seed_drive_discs()
    await seed_weapons()


if __name__ == "__main__":
    asyncio.run(main())
