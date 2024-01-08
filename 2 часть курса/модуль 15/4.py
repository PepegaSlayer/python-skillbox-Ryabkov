from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache = OrderedDict()

    @property
    def oldest_item(self):
        if self._cache:
            key, value = next(iter(self._cache.items()))
            return f"{key} : {value}"
        else:
            return "Cache is empty"

    @oldest_item.setter
    def oldest_item(self, new_elem):
        if new_elem[0] in self._cache:
            del self._cache[new_elem[0]]
        elif len(self._cache) == self.capacity:
            self._cache.popitem(last=False)
        self._cache[new_elem[0]] = new_elem[1]

    def print_cache(self):
        for key, value in self._cache.items():
            print(f"{key} : {value}")

    def get(self, key):
        value = self._cache.pop(key)
        self._cache[key] = value
        return value


# Проверка работы
cache = LRUCache(3)
cache.oldest_item = ("key1", "value1")
cache.oldest_item = ("key2", "value2")
cache.oldest_item = ("key3", "value3")
cache.print_cache()
print(cache.get("key2"))
cache.oldest_item = ("key4", "value4")
cache.print_cache()