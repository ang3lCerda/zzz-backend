import json
import asyncio
from db import drive_discs_collection  # your Motor collection

async def seed():
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

if __name__ == "__main__":
    asyncio.run(seed())
