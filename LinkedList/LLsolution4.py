from typing import List,Optional,ListNode
class LLSolution4:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        list = []
        count = 0
        while head:
            list.append(head)
            head = head.next
            count=count+1
        #list.reverse()
        return list[count-cnt]