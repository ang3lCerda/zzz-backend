from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.db import DriveDisc, Weapon, get_async_session, create_db_and_tables
from app.schemas import DriveDiscResponse, WeaponsResponse
from app.seed_db import seed_drive_dics, seed_weapons

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    await seed_drive_dics()
    await seed_weapons()
    yield

app = FastAPI(title="zzz-backend", lifespan=lifespan)

@app.get("/discs", response_model=List[DriveDiscResponse])
async def list_discs(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(DriveDisc))
    discs = result.scalars().all()
    return discs

@app.get("/weapons", response_model=List[WeaponsResponse])
async def list_weapons(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Weapon))
    weapons = result.scalars().all()
    return weapons

@app.get("/")
async def root():
    return {"status": "online"}