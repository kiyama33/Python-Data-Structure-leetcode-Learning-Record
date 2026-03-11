from typing import List
from collections import deque
class StackSolution3:
    def validateBookSequences(self, putIn: List[int], takeOut: List[int]) -> bool:
        stack = deque()
        i = 0
        for item in putIn:
            stack.append(item)
            while stack and takeOut[i]==stack[-1]:
                stack.pop()
                i+=1
        return not stack
