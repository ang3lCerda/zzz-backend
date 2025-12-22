from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
import os

# Updated imports to ensure they work regardless of how you run the script
from app.db import DriveDisc, Weapon, get_async_session, create_db_and_tables, DATABASE_URL
from app.schemas import DriveDiscResponse, WeaponsResponse

app = FastAPI(title="zzz-backend")

@app.on_event("startup")
async def on_startup():
    # This will print to your terminal so you can verify the DB path matches your seeder
    print(f"--- API CONNECTING TO: {DATABASE_URL} ---")
    await create_db_and_tables()

@app.get("/discs", response_model=List[DriveDiscResponse])
async def list_discs(session: AsyncSession = Depends(get_async_session)):
    """Fetches all Drive Discs from the database."""
    result = await session.execute(select(DriveDisc))
    discs = result.scalars().all()
    return discs

@app.get("/weapons", response_model=List[WeaponsResponse])
async def list_weapons(session: AsyncSession = Depends(get_async_session)):
    """Fetches all Weapons from the database."""
    result = await session.execute(select(Weapon))
    weapons = result.scalars().all()
    return weapons

# Root endpoint for a quick health check
@app.get("/")
async def root():
    return {"status": "online", "database": DATABASE_URL}