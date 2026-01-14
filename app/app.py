from fastapi import FastAPI
from app.db import drive_discs_collection  # your Motor collection

app = FastAPI()

@app.get("/drive-discs")
async def get_drive_discs():
    # Exclude MongoDB _id
    discs_list = await drive_discs_collection.find({}, {"_id": 0}).to_list(length=None)
    
    # Wrap by your custom Id
    wrapped = {str(disc["Id"]): disc for disc in discs_list}
    
    return wrapped

