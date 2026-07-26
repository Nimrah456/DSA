class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.bucket = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        hashkey = hash(key) % self.size
        buckets = self.bucket[hashkey]
        for index, (record_key, _) in enumerate(buckets):
            if record_key == key:
                buckets[index] = (key, value)   # update existing
                return
        buckets.append((key, value))            # insert new

    def get(self, key: int) -> int:
        hashkey = hash(key) % self.size
        buckets = self.bucket[hashkey]
        for record_key, record_value in buckets:
            if record_key == key:
                return record_value
        return -1

    def remove(self, key: int) -> None:
        hashkey = hash(key) % self.size
        buckets = self.bucket[hashkey]
        for index, (record_key, _) in enumerate(buckets):
            if record_key == key:
                del buckets[index]
                return