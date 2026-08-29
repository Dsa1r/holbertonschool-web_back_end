#!/usr/bin/env python3
"""
Tasks
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n function
    """
    list_float: List[float] = []
    for i in range(n):
        list_float.append(await task_wait_random(max_delay))
    return sorted(list_float)
