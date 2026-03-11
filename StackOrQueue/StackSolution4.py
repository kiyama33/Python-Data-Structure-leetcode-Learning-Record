from typing import List
from collections import deque
class Solution:
    def maxAltitude(self, heights: List[int], limit: int) -> List[int]:
        if heights==[]:
            return []
        queue = deque()
        res:List[int]=[]
        for i in range(limit):
            queue.append(heights[i])
        for j in range(limit,len(heights),1):
            res.append(self.check(queue,limit))
            queue.append(heights[j])
            queue.popleft()
        res.append(self.check(queue, limit))
        return res
    def check(self,nums:deque[int],limit:int)->int:
        res = 0
        for i in range(limit):
            if nums[i]>res:
                res = nums[i]
        return res
