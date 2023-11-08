#!/usr/bin/env python3
import asyncio
"""
   Execute multiple coroutines at the same time with async.
"""

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list[int]:
    """
      will spawn wait_random n times with the specified max_delay.
      wait_n should return the list of all the delays (float values).
      The list of the delays should be in ascending order without
      using sort() because of concurrency.
    """

    num_list = []
    coroutines = []

    for i in range(n):
        task = wait_random(max_delay)
        coroutines.append(task)

    for task in asyncio.as_completed(coroutines):
        coro = await task
        num_list.append(coro)

    return num_list



