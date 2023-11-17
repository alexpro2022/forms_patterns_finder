from motor.motor_asyncio import AsyncIOMotorClient

from app.config import config


async def setup_db(db_url: str, documents: list[dict[str, str]]):
    client = AsyncIOMotorClient(db_url)
    db = client[config.database_name]
    await db[config.collection_name].drop()
    await db[config.collection_name].insert_many(documents)
    return db
