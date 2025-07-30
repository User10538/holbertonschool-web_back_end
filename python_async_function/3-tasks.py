#!/usr/bin/env python3
"""
Create afunction task_wait_random that takes an integer 
max_delay and returns a asyncio.Task.
"""


import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """
    Create afunction task_wait_random that takes an integer 
    max_delay and returns a asyncio.Task.

    Args:
    max_delay: int = 10

    Returns:
    asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))    
 
