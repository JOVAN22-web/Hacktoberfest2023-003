from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, page):
        if page in self.cache:
            # Move the accessed page to the end
            self.cache.move_to_end(page)
            return page
        else:
            return -1

    def put(self, page):
        if page in self.cache:
            # If the page is already in the cache, move it to the end
            self.cache.move_to_end(page)
        else:
            if len(self.cache) >= self.capacity:
                # If the cache is full, remove the least recently used page (first item)
                self.cache.popitem(last=False)
            self.cache[page] = None

# Example usage
lru = LRUCache(3)  # Create a cache with a capacity of 3 pages

lru.put(1)
lru.put(2)
lru.put(3)

print(lru.cache.keys())  # Output: odict_keys([1, 2, 3])

lru.get(2)
print(lru.cache.keys())  # Output: odict_keys([1, 3, 2])

lru.put(4)
print(lru.cache.keys())  # Output: odict_keys([3, 2, 4])
