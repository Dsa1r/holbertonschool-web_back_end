#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n function
    """
    list_float: List[float] = []
    for i in range(n):
        list_float.append(await wait_random(max_delay))
    return sorted(list_float)
