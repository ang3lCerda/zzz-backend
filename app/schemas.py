# schemas.py
from pydantic import BaseModel

class DriveDiscBase(BaseModel):
    icon: str
    name: str
    desc2: str
    story: str  # corresponds to desc4

class DriveDiscCreate(DriveDiscBase):
    pass  # used for POST input

class DriveDiscResponse(DriveDiscBase):
    id: str  # include id in the response

    class Config:
        orm_mode = True  # <-- important to work with SQLAlchemy models
