class MyHashSet:

    def __init__(self):
        self.size = 1000 
        self.bs = [[] for _ in range(self.size)]
        

    def add(self, key: int) -> None:
        b = self.bs[key % self.size]
        if key not in b:
            b.append(key)
        

    def remove(self, key: int) -> None:
        b = self.bs[key % self.size]
        if key in b:
            b.remove(key)
        

    def contains(self, key: int) -> bool:
        b = self.bs[key % self.size]
        if key in b:
            return True
        else:
            return False    
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)