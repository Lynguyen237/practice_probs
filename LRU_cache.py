# https://www.geeksforgeeks.org/lru-cache-in-python-using-ordereddict/
# Our problem statement is to design and implement a data structure for Least Recently Used (LRU) cache. 
# It should support the following operations: get and put.
# * get(key) – Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1. 
# * put(key, value) – Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
# The cache is always initialized with positive capacity.

from collections import OrderedDict

class LRUCache:

    def __init__(self, maxsize: int):
        self.cache = OrderedDict()
        self.maxsize = maxsize

    def __repr__(self):
        return f'cache: {self.cache}, maxsize: {self.maxsize}'

    # Add the key-value pair to the dictionary
    # Move it to the end of the OrderedDict to show that it was recently visited 
    # If the size of the cache is greater than maxsize
    # Pop the first key in the dict (the least recently used)
    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)

        if len(self.cache) > self.maxsize:
            self.cache.popitem(last = False)

    # If the key does not exist in the dictionary, return None
    # If it does, return the value and move it to the end of the OrderedDict
    # To show that it was recenlty visited
    def get(self, key):
        if key not in self.cache:
            return "None"
        else:
            self.cache.move_to_end(key)
        
        return self.cache[key]


#==== Test ====
cache = LRUCache(2)

cache.put(1, 1)
print(cache.cache)
cache.put(2, 2)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.put(3, 3)
print(cache.cache)
cache.get(2)
print(cache.cache)
cache.put(4, 4)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.get(3)
print(cache.cache)
cache.get(4)
print(cache.cache)