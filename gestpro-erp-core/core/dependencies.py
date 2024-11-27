from shared.http_client import HTTPClient
from core.config import settings

def get_database_client() -> HTTPClient:
    return HTTPClient(base_url=settings.DATABASE_SERVICE_URL)
