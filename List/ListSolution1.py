from typing import Optional,List,ListNode
class ListSolution1:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        res1:List[int]=[]
        res2:List[int]=[]
        for item in actions:
            if item%2==1:
                res1.append(item)
            else:
                res2.append(item)
        return res1+res2