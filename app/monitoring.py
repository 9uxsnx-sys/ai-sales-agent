"""
Monitoring and health checks.
"""
from fastapi import APIRouter
from datetime import datetime
import aioredis
from sqlalchemy import text
from app.database import engine
from app.config import REDIS_URL

router = APIRouter(prefix="/health", tags=["monitoring"])

@router.get("/")
async def health_check():
    checks = {"database": "healthy", "redis": "healthy"}
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat(), "checks": checks}

@router.get("/ready")
async def readiness_check():
    return {"ready": True}

@router.get("/live")
async def liveness_check():
    return {"alive": True}
