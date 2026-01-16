from pydantic import BaseModel, Field
from datetime import datetime


class MongoBaseModel(BaseModel):
    id: int = Field(..., alias="_id")

    class Config:
        populate_by_name = True


class DriveDisc(MongoBaseModel):
    Name: str
    Desc2: str
    Desc4: str
    Story: str
    Icon: str
