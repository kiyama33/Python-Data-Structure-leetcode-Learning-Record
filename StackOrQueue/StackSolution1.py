from typing import List
from collections import deque
class CQueue:
    queue:deque
    def __init__(self):
        self.queue=deque()
    def appendTail(self, value: int) -> None:
        self.queue.appendleft(value)
    def deleteHead(self) -> int:
        if len(self.queue)==0:
            return -1
        tmp = self.queue.pop()
        return tmp

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()