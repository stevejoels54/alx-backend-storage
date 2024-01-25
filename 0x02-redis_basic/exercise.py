#!/usr/bin/env python3
"""
Redis basic.
"""
import redis
import uuid
from typing import Union, Callable


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

    def get(self,
            key: str, fn: Optional[Callable] = None) -> str:
        """Takes key str arg, convert data to desired format"""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, data: str) -> str:
        """Returns string value of decoded byte"""
        return data.decode('utf-8', 'strict')

    def get_int(self, data: str) -> int:
        """Returns integer value of decoded byte """
        return int(data)
