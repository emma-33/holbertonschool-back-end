#!/usr/bin/env python3
"""Defines a class Server"""
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """Returns a tuple of size two containing a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


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
        """Get dataset page"""
        assert isinstance(page, int) or isinstance(page_size, int)
        assert page > 0 or page_size > 0

        indexes = index_range(page, page_size)
        my_dataset = self.dataset()

        if indexes[0] > len(my_dataset) and indexes[1] > len(my_dataset):
            return []

        return my_dataset[indexes[0]:indexes[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get hypermedia pagination"""
        return_get_page = self.get_page(page, page_size)
        my_dataset = self.dataset()

        page_size = len(return_get_page)

        data = return_get_page

        if self.get_page(page + 1, page_size) == []:
            next_page = None
        else:
            next_page = page + 1

        if self.get_page(page - 1, page_size) == []:
            prev_page = None
        else:
            prev_page = page - 1

        total_pages = len(my_dataset)

        dict_data = {"page_size": page_size,
                     "page": page,
                     "data": data,
                     "next_page": next_page,
                     "prev_page": prev_page,
                     "total_pages": total_pages}

        return dict_data
