#!/usr/bin/python3
""" FIFOCache module to work with a basic dictionary using FIFO algorithm.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and
    is a caching system using FIFO algorithm.
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm
        """
        if key is None or item is None:
            return

        dict_data = self.cache_data
        if len(dict_data) >= BaseCaching.MAX_ITEMS:
            # If the cache is full, discard the first item (FIFO)
            discarded_key = next(iter(dict_data))
            del dict_data[discarded_key]
            print("DISCARD:", discarded_key)

        # Add the new item to the cache
        dict_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        dict_data = self.cache_data
        return dict_data.get(key) if key is not None else None
