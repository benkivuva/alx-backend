#!/usr/bin/python3
""" LRUCache module to work with a basic dictionary using LRU algorithm.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and
    is a caching system using LRU algorithm.
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.order_used = []

    def put(self, key, item):
        """ Add an item in the cache using LRU algorithm
        """
        if key is None or item is None:
            return

        dict_data = self.cache_data
        if len(dict_data) >= BaseCaching.MAX_ITEMS:
            # If the cache is full, discard the least recently used item (LRU)
            lru_key = self.order_used.pop(0)
            del dict_data[lru_key]
            print("DISCARD:", lru_key)

        # Add the new item to the cache and update order_used
        dict_data[key] = item
        self.order_used.append(key)

    def get(self, key):
        """ Get an item by key
        """
        dict_data = self.cache_data
        if key is None or key not in dict_data:
            return None

        # Update order_used to indicate recent usage
        self.order_used.remove(key)
        self.order_used.append(key)

        return dict_data[key]
