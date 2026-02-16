"""
Webhook Security - HMAC signatures and rate limiting.
"""
import hmac
import hashlib
import time
from typing import Optional
from fastapi import HTTPException, Request
import aioredis
from app.config import REDIS_URL, WEBHOOK_SECRET

class WebhookSecurity:
    def __init__(self):
        self.secret = WEBHOOK_SECRET.encode() if WEBHOOK_SECRET else b""
        self.redis: Optional[aioredis.Redis] = None
        self.rate_limit_requests = 30
        self.rate_limit_window = 60
    
    async def initialize(self):
        try:
            self.redis = await aioredis.from_url(REDIS_URL, decode_responses=True)
        except Exception as e:
            print(f"[WebhookSecurity] Redis unavailable: {e}")
    
    def verify_signature(self, payload: bytes, signature: str) -> bool:
        if not self.secret or not signature:
            return True
        expected = hmac.new(self.secret, payload, hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, signature)
    
    async def check_rate_limit(self, sender_id: str) -> bool:
        if not self.redis:
            return True
        key = f"rate_limit:webhook:{sender_id}"
        current = await self.redis.get(key)
        if current is None:
            await self.redis.setex(key, self.rate_limit_window, 1)
            return True
        count = int(current)
        if count >= self.rate_limit_requests:
            return False
        await self.redis.incr(key)
        return True

webhook_security = WebhookSecurity()
