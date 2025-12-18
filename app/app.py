from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List


from app.db import DriveDisc, get_async_session, create_db_and_tables
from app.schemas import DriveDiscCreate, DriveDiscResponse


app = FastAPI(title="zzz-backend")


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()

@app.get("/discs", response_model=List[DriveDiscResponse])
async def list_discs(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(DriveDisc))
    discs = result.scalars().all()
    return discs


# GET a single DriveDisc by ID
@app.get("/discs/{disc_id}", response_model=DriveDiscResponse)
async def get_disc(disc_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(DriveDisc).where(DriveDisc.id == disc_id))
    disc = result.scalars().first()

    if not disc:
        raise HTTPException(status_code=404, detail="DriveDisc not found")

    return disc  # Pydantic model will handle serialization


# CREATE a new DriveDisc
@app.post("/discs", response_model=DriveDiscResponse)
async def create_drive_disc(
    disc_in: DriveDiscCreate,
    session: AsyncSession = Depends(get_async_session)
):
    new_disc = DriveDisc(
        icon=disc_in.icon,
        name=disc_in.name,
        desc1=disc_in.desc1,
        desc2=disc_in.desc2,
        story=disc_in.story
    )

    session.add(new_disc)
    await session.commit()
    await session.refresh(new_disc)

    return new_disc
