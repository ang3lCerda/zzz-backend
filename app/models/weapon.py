from pydantic import BaseModel
from typing import Dict


class WeaponType(BaseModel):
    __root__: Dict[str, str]


class Property(BaseModel):
    Name: str
    Name2: str
    Format: str
    Value: int


class LevelEntry(BaseModel):
    Exp: int
    Rate: int
    Rate2: int


class StarEntry(BaseModel):
    StarRate: int
    RanRate: int


class Talent(BaseModel):
    Name: str
    Decription: str


class Weapon(BaseModel):
    Id: int
    CodeName: str
    Name: str
    Desc: str
    Desc2: str
    Desc3: str
    Rarity: int
    Icon: str

    WeaponType: Dict[str, str]
    BaseProperty: Property
    RandProperty: Property

    Level: Dict[str, LevelEntry]
    Stars: Dict[str, StarEntry]

    Materials: str
    Talents: Dict[str, Talent]
