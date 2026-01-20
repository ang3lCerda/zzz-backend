from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.db import drive_discs_collection, weapons_collection, characters_collection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://ang3lcerda.github.io"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/disc")
async def get_all_drive_discs():
    discs_list = await drive_discs_collection.find(
        {},
        {"_id": 0, "Story": 0}
    ).to_list(length=None)

    wrapped = {str(disc["Id"]): disc for disc in discs_list}
    return wrapped

@app.get("/disc/{id}")
async def get_disc(id:int):
    disc = await drive_discs_collection.find_one({"Id": id})
    
    if not disc:
        raise HTTPException(status_code=404, detail="Disc not found")
    
    disc["_id"] = str(disc["_id"])

    return disc

@app.get("/weapons")
async def get_all_weapons():
    weapons_list = await weapons_collection.find(
        {}, 
        {"_id": 0, "Icon": 1, "WeaponType": 1, "Rarity": 1, "Desc3": 1, "Id": 1, "Name": 1}
    ).sort("Rarity", -1).to_list(length=None) 
   

    return weapons_list


@app.get("/weapon/{id}")
async def get_weapon(id: int):
    weapon = await weapons_collection.find_one({"Id": id})

    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")

    # Optional: remove MongoDB _id entirely
    weapon["_id"] = str(weapon["_id"])

    return weapon


@app.get("/character/{id}")
async def get_disc(id:int):
    char = await characters_collection.find_one({"Id": id})
    
    if not char:
        raise HTTPException(status_code=404, detail="Character not found")
    
    char["_id"] = str(char["_id"])

    return char
