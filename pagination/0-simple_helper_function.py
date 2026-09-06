#!/usr/bin/env python3
"""
Build a helper method to show the first and end index of the page
"""


def index_range(page, page_size):
    """
    Calculate the start and end index for a given page and page size.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


