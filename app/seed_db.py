import json
import asyncio
from app.db import DriveDisc , async_session_maker, create_db_and_tables, Weapon

def load_json(filename):
    try:
        with open(filename) as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return {}


async def seed_drive_dics():
    await create_db_and_tables()
    data= load_json( "../scrape/drive_discs.json")

    async with async_session_maker() as session:
        for _, item in data.items():
            disc = DriveDisc(
                icon=item["icon"],
                name=item["name"],
                desc1=item["desc2"],
                desc2=item["desc4"]
            )
            session.add(disc)

        await session.commit()

async def seed_weapons():
    await create_db_and_tables()
    data=load_json("../scrape/weapons.json")

    async with async_session_maker() as session:
        for _, item in data.items():
            weapon = Weapon(
                icon=item["icon"],
                rank=item["rank"],
                type=item["type"],
                name=item["EN"]
            )
            session.add(weapon)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(seed_drive_dics())
    asyncio.run(seed_weapons())
