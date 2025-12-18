import uuid
from sqlalchemy import Column, String, Text,Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

# Database URL — change to PostgreSQL if needed
DATABASE_URL = "sqlite+aiosqlite:///./zzz-backend.db"

# Base class for models
class Base(DeclarativeBase):
    pass

# DriveDisc table
class DriveDisc(Base):
    __tablename__ = "drive_discs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    icon = Column(String, nullable=False)
    name = Column(String, nullable=False)
    desc1 = Column(Text, nullable=False)
    desc2 = Column(Text, nullable=False)
    story = Column(Text, nullable=False)

# Async engine and session maker
engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# Create tables function
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependency for FastAPI
async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
