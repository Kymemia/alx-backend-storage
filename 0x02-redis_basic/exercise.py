#!/usr/bin/env python3

"""
class, Cache, that's got the __init__ method
to store an instance of the redis client
as a private variable named, _redis, using redis.Redis()
method, store, that takes a data arg and returns a string
"""
import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"{method.__qualname__}_calls"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def replay(method: Callable):
    """
    method definition to display the history
    of calls of a particular function
    """
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    redis_instance = method.__Self__.__redis
    inputs = redis_instance.lrange(input_key, 0, -1)
    ouputs = redis_instance.lrange(output_key, 0, -1)
    print(f"{method.__qualname__} was called {len(inouts)} times:")
    for x, (input_args, output) in enumerate(zip(inputs, outputs), 1):
        print(f"{method.__qualname__}(*{input_args.decode('utf-8')}) -> {output.decode('utf-8')}")

def call_history(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper

class Cache:
    def __init__(self):
        """
        method definition to initialize cache class
        and flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method definition to store input data
        with a randomly generated key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        method definition that takes a key string argument
        and an optional Callable argument, fn
        the callable will be used to convert
        the data back to the desired format
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_int(self, key: str) -> Optional[int]:
        """
        method definition to parametrize Cache.get
        with the correct conversion function
        """
        return self.get(key, fn=int)

    def get_str(self, key: str) -> Optional[str]:
        """
        method definition to parametrize Cache.get
        with the correct conversion function
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))
