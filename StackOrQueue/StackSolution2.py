from collections import deque
class MinStack:
    def __init__(self):
        self.stackall = deque()
        self.stackmin = deque()
    def push(self, x: int) -> None:
        self.stackall.append(x)
        if len(self.stackmin)==0:
            self.stackmin.append(x)
        else:
            if (self.stackmin[-1]>=x):
                self.stackmin.append(x)
    def pop(self) -> None:
        if self.stackmin[-1]==self.stackall.pop():
            self.stackmin.pop()
    def top(self) -> int:
        return self.stackall[-1]
    def getMin(self) -> int:
        return self.stackmin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()