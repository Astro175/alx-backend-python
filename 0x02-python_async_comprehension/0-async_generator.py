#!/usr/bin/env python3

"""Module that creates a coroutine"""
import random
import asyncio


async def async_generator() -> Iterable[float]: 
    """
       The coroutine will loop 10 times, each time asynchronously wait 1
       second, then yield a random number between 0 and 10.
       Use the random module.
    """
    for i in range(11):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
