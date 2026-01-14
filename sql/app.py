from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.db import DriveDisc, Weapon, get_async_session, create_db_and_tables
from app.sql.seed_db import seed_drive_dics, seed_weapons

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    await seed_drive_dics()
    await seed_weapons()
    yield

app = FastAPI(title="zzz-backend", lifespan=lifespan)

from typing import Dict
from app.sql.schemas import DriveDiscBase, WeaponBase 

@app.get("/discs", response_model=Dict[int, DriveDiscBase])
async def list_discs(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(DriveDisc))
    discs = result.scalars().all()
    return {disc.id: disc for disc in discs}

@app.get("/weapons", response_model=Dict[int, WeaponBase])
async def list_weapons(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Weapon))
    weapons = result.scalars().all()
    return {weapon.id: weapon for weapon in weapons}

@app.get("/")
async def root():
    return {"status": "online"}