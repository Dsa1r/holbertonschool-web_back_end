#!/usr/bin/env python3
"""
Build a helper method to get the page
"""

import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of the dataset.

        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.

        Returns:
            List[List]: list of lists representing the requested page of data.
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be apositive."
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive."

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get a hypermedia page of the dataset.

        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.

        Returns:
            dict: A dictionary containing the requested \
            page of data and pagination information.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
