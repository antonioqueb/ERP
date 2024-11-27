# db-service/app/routers/health.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "db-service is healthy"}
