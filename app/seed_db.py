import asyncio
import uuid
from app.db import DriveDisc, async_session_maker, create_db_and_tables

data = [
    {
        "icon": "UI/Sprite/A1DynamicLoad/IconSuit/UnPacker/SuitSavior.png",
        "name": "Shining Aria",
        "desc1": "Example Desc1",
        "desc2": "<color=#FE437E>Ether DMG</color> +10%",
        "story": "The first album released after \"Angels of Delusion\"..."
    },
    {
        "icon": "UI/Sprite/A1DynamicLoad/IconSuit/UnPacker/SuitSavior.png",
        "name": "Phaethon's Melody",
        "desc1": "Example Desc1",
        "desc2": "Anomaly Mastery +8%.",
        "story": "A peculiar Drive Disc created by fanatical followers of Phaethon..."
    }
]

async def seed_db():
    await create_db_and_tables()

    async with async_session_maker() as session:
        for item in data:
            disc = DriveDisc(
                icon=item["icon"],
                name=item["name"],
                desc1=item.get("desc1", ""),
                desc2=item["desc2"],
                story=item["story"]
            )
            session.add(disc)
        await session.commit()
        print("DB seeded successfully!")


if __name__ == "__main__":
    asyncio.run(seed_db())
