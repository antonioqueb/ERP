from fastapi import APIRouter, Depends
from core.dependencies import get_database_client

router = APIRouter()

@router.get("/health")
async def health_check(db_client=Depends(get_database_client)):
    db_status = await db_client.get("/health")
    return {"status": "ok", "db_status": db_status}
