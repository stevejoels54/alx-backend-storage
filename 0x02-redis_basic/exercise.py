#!/usr/bin/env python3
"""
Redis basic.
"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class handles redis operations."""
    def __init__(self):
        """stores instance of Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes data argument stores it and returns a string."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
