#!/usr/bin/env python3
"""
Track expiring web cache
"""
import redis
import requests
from typing import Callable
from functools import wraps
client = redis.Redis()


def url_count(method: Callable) -> Callable:
    """counts times url is accessed"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        url = args[0]
        client.incr(f"count:{url}")
        cached = client.get(f'{url}')

        if cached:
            return cached.decode('utf-8')

        client.setex(f'{url}, 10, {method(url)}')
        return method(*args, **kwargs)
    return wrapper


@url_count
def get_page(url: str) -> str:
    """page and cache value"""
    res = requests.get(url)
    return res.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
