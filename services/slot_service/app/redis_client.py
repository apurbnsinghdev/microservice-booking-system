import redis.asyncio as redis
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class RedisSettings(BaseSettings):
    slot_redis_host: str = "localhost"
    slot_redis_port: int = 6379
    slot_redis_db: int = 0
    slot_redis_pass: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        populate_by_name=True,
    )

class RedisClient:
    _redis_instance: Optional[redis.Redis] = None

    @classmethod
    def init_client(cls):
        if cls._redis_instance is None:
            settings = RedisSettings()
            cls._redis_instance = redis.Redis(
                host=settings.slot_redis_host,
                port=settings.slot_redis_port,
                db=settings.slot_redis_db,
                password=settings.slot_redis_pass,
                decode_responses=True,
            )
        return cls._redis_instance

    @classmethod
    def get_client(cls) -> redis.Redis:
        if cls._redis_instance is None:
            cls.init_client()
        return cls._redis_instance
    

async def set_slot(key: str, value: str, expire_seconds: int = 3600):
    client = RedisClient.get_client()
    await client.set(key, value, ex=expire_seconds)

async def get_slot(key: str) -> Optional[str]:
    client = RedisClient.get_client()
    return await client.get(key)

async def delete_slot(key: str):
    client = RedisClient.get_client()
    await client.delete(key)