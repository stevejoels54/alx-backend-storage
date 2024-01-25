#!/usr/bin/env python3
"""
Redis basic.
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Stores history of inputs and outputs for a particular function"""
    key = method.__qualname__
    inputs = key + ':inputs'
    outputs = key + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


def count_calls(method: Callable) -> Callable:
    """count how many times methods of the Cache class are called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method: Callable) -> None:
    """Displays history of calls of a particular function"""
    cache = Cache()
    key = method.__qualname__
    input_key = "{}:inputs".format(key)
    output_key = "{}:outputs".format(key)

    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(output_key, 0, -1)

    method_count = cache._redis.get(key).decode('utf-8')

    print("{} was called {} times:".format(key, method_count))

    for inp, out in zip(inputs, outputs):
        input_args = eval(inp.decode('utf-8'))
        print("{}{} -> {}".format(key, input_args, out.decode('utf-8')))


class Cache:
    """Cache class handles redis operations."""
    def __init__(self):
        """stores instance of Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
