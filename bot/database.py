# ---------------------------------------------------------
# GitHubBot - All rights reserved
# ---------------------------------------------------------

from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["github_bot"]

users_col = db["users"]

async def save_user_token(user_id: int, token: str):
    await users_col.update_one(
        {"_id": user_id},
        {"$set": {"token": token}},
        upsert=True
    )

async def get_user_token(user_id: int):
    user = await users_col.find_one({"_id": user_id})
    return user["token"] if user else None

async def remove_user_token(user_id: int):
    await users_col.delete_one({"_id": user_id})
