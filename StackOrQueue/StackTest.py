from collections import deque
from typing import List
stack = deque()
stack.appendleft(1)
stack.appendleft(2)
print(stack[-1])
print(list(stack))
stack.popleft()
print(list(stack))

queue = deque()
queue.append(1) #append是right
queue.append(2)
print(list(queue))
queue.pop()#pop right
print(list(queue))