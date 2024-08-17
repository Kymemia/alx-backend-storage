#!/usr/bin/env python3

"""
class, Cache, that's got the __init__ method
to store an instance of the redis client
as a private variable named, _redis, using redis.Redis()
method, store, that takes a data arg and returns a string
"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """
        method definition to initialize cache class
        and flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method definition to store input data
        with a randomly generated key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
