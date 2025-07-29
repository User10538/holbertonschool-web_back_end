#!/usr/bin/env python3

import random
import asyncio


async def wait_random(max_delay: int = 0):
    """
    asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random
      that waits for a random delay between 0 and max_delay

    Args:
    lst: list.

    Returns:
    random delay between 0 and
      max_delay (included and float value) seconds
    """

    get_random = random.uniform(0, max_delay)
    await asyncio.sleep(get_random)
    return get_random
