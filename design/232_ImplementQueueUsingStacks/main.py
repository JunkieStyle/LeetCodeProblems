class MyQueue:
    def __init__(self):
        self.back, self.front = [], []
        

    def push(self, x: int) -> None:
        if not self.front:
            self.front.append(x)
        else:
            self.back.append(x)
        

    def pop(self) -> int:
        result = self.front.pop()
        if not self.front and self.back:
            while self.back:
                self.front.append(self.back.pop())
        return result

    def peek(self) -> int:
        return self.front[-1]


    def empty(self) -> bool:
        return not self.front
