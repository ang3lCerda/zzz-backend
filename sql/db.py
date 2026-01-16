from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite+aiosqlite:///./zzz-backend.db"


class Base(DeclarativeBase):
    pass


class DriveDisc(Base):
    __tablename__ = "drive_discs"
    __table_args__ = {"sqlite_autoincrement": True}

    id = Column(Integer, primary_key=True)
    icon = Column(String, nullable=False)
    name = Column(String, nullable=False)
    desc1 = Column(Text, nullable=False)
    desc2 = Column(Text, nullable=False)


class Weapon(Base):
    __tablename__ = "weapons"
    __table_args__ = {"sqlite_autoincrement": True}

    id = Column(Integer, primary_key=True)
    icon = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)
    type = Column(Integer, nullable=False)
    name = Column(String, nullable=False)


engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
