from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.appendleft(x)
        self.queue.rotate(len(self.queue) - 1)

    def pop(self) -> int:
        return self.queue.pop()
        
    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue

obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.top())
print(obj.empty())
