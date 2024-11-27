import httpx
from app.config import settings

class DatabaseClient:
    def __init__(self, base_url: str = settings.DATABASE_SERVICE_URL):
        self.base_url = base_url

    async def get_user(self, username: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/users/{username}")
            response.raise_for_status()
            return response.json()

    async def create_user(self, user_data: dict):
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/users", json=user_data)
            response.raise_for_status()
            return response.json()
