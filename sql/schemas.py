from pydantic import BaseModel


class DriveDiscBase(BaseModel):
    icon: str
    name: str
    desc1: str
    desc2: str


class DriveDiscCreate(DriveDiscBase):
    pass


class DriveDiscResponse(DriveDiscBase):
    id: int

    class Config:
        from_attributes = True


class WeaponBase(BaseModel):
    icon: str
    rank: int
    type: int
    name: str


class WeaponsResponse(WeaponBase):
    id: int

    class Config:
        from_attributes = True
