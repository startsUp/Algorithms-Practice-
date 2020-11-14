import functools
class Solution:
    def lruCacheMisses(self, num, pages, maxCacheSize):
        @functools.lru_cache(maxsize=maxCacheSize)
        def helper(page): return
        for page in pages: helper(page)
        return helper.cache_info().misses

"""

from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
        self.misses = 0
        self.n = 0
        
    def hit(self, key):
        if key in self: self.move_to_end(key)
        else:
            self.misses += 1
            self[key] = None
            self.n += 1
        if self.n > self.capacity:
            self.popitem(last = False)
            self.n -= 1
            
class Solution:
    def lruCacheMisses(self, num, pages, maxCacheSize):
        lru_cache = LRUCache(maxCacheSize)
        for page in pages:
            lru_cache.hit(page)
        return lru_cache.misses

"""