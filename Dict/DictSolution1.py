from typing import List,Dict
#LeetCode 1 两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Res:List[int] = []
        index:int = 0
        Hash:Dict[int,int] = {}
        for i in nums:
            if target-i in Hash:
                Res.append(index)
                Res.append(Hash[target-i])
            Hash[i]=index
            index+=1
        return Res