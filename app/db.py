from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URL)
db = client["my_local_db"]

drive_discs_collection = db["drive_discs"]
weapons_collection = db["weapons"]
characters_collection = db["characters"]
