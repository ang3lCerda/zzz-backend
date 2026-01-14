from fastapi import FastAPI
from app.db import drive_discs_collection, weapons_collection # your Motor collectio

app = FastAPI()

@app.get("/drive-discs")
async def get_drive_discs():
    # Exclude MongoDB _id
    discs_list = await drive_discs_collection.find({}, {"_id": 0}).to_list(length=None)
    
    # Wrap by your custom Id
    wrapped = {str(disc["Id"]): disc for disc in discs_list}
    
    return wrapped

@app.get("/weapons")
async def get_weapons():
    # Exclude MongoDB _id
    discs_list = await weapons_collection.find({}, {"_id": 0}).to_list(length=None)
    
    # Wrap by your custom Id
    wrapped = {str(disc["Id"]): disc for disc in discs_list}
    
    return wrapped

