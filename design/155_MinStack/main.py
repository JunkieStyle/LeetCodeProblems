class MinStack:
    def __init__(self):
        self.storage = []
        self.min_indices = [] 
        
    def push(self, val: int) -> None:
        idx = len(self.storage)
        
        if self.min_indices:
            prev = self.min_indices[-1]
            idx = idx if val <= self.storage[prev] else prev
                    
        self.storage.append(val)
        self.min_indices.append(idx)

    def pop(self) -> None:
        self.min_indices.pop()
        return self.storage.pop()
        

    def top(self) -> int:
        return self.storage[-1]
        

    def getMin(self) -> int:
        return self.storage[self.min_indices[-1]]
