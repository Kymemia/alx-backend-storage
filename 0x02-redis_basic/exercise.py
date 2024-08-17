#!/usr/bin/env python3

"""

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

    def store(self, data: Union[str, bytes, int, float]):
        """
        method definition to store input data
        with a randomly generated key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
