class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        q = self.queue.pop()
        return q

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return False if len(self.queue) >= 1 else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()