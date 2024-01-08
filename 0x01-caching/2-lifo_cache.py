#!/usr/bin/python3
""" LIFOCache module to work with a basic dictionary using LIFO algorithm.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and
    is a caching system using LIFO algorithm.
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache using LIFO algorithm
        """
        if key is None or item is None:
            return

        dict_data = self.cache_data
        if len(dict_data) >= BaseCaching.MAX_ITEMS:
            # If the cache is full, discard the last item (LIFO)
            discarded_key = list(dict_data.keys())[-1]
            del dict_data[discarded_key]
            print("DISCARD:", discarded_key)

        # Add the new item to the cache
        dict_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        dict_data = self.cache_data
        return dict_data.get(key) if key is not None else None
