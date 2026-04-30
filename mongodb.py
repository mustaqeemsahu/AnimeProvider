# ==============================
# MONGODB + CACHE + FAST SEARCH
# ==============================

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI
import time

# ==============================
# CONNECTION
# ==============================

client = AsyncIOMotorClient(MONGO_URI)
db = client["AnimeBotDB"]

# Collections
users_col = db["users"]
groups_col = db["groups"]
anime_col = db["anime"]
warns_col = db["warns"]

# ==============================
# CACHE SYSTEM
# ==============================

ANIME_CACHE = []
CACHE_TIME = 0
CACHE_TTL = 300  # 5 minutes

# ==============================
# USERS SYSTEM
# ==============================

async def add_user(user_id: int):
    if not await users_col.find_one({"_id": user_id}):
        await users_col.insert_one({"_id": user_id})


async def get_all_users():
    return [u["_id"] async for u in users_col.find()]


# ==============================
# GROUP SYSTEM
# ==============================

async def add_group(chat_id: int):
    if not await groups_col.find_one({"_id": chat_id}):
        await groups_col.insert_one({"_id": chat_id})


async def get_all_groups():
    return [g["_id"] async for g in groups_col.find()]


# ==============================
# ANIME SYSTEM (CACHED)
# ==============================

async def load_anime_cache():
    global ANIME_CACHE, CACHE_TIME

    ANIME_CACHE = [a async for a in anime_col.find()]
    CACHE_TIME = time.time()


async def get_all_anime():
    global CACHE_TIME

    # Reload cache if expired
    if time.time() - CACHE_TIME > CACHE_TTL or not ANIME_CACHE:
        await load_anime_cache()

    return ANIME_CACHE


async def add_anime_db(name, keys, sticker, link):
    await anime_col.update_one(
        {"name": name},
        {"$set": {
            "name": name,
            "keys": keys,
            "sticker": sticker,
            "link": link
        }},
        upsert=True
    )

    # 🔥 Refresh cache instantly
    await load_anime_cache()


async def delete_anime_db(name):
    await anime_col.delete_one({"name": name})

    # 🔥 Refresh cache instantly
    await load_anime_cache()


# ==============================
# FAST SEARCH (INDEX BASED)
# ==============================

async def create_indexes():
    await anime_col.create_index("name")
    await anime_col.create_index("keys")
