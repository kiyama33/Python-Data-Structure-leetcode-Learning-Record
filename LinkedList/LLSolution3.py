from typing import Optional,List,ListNode
class LLSolution3:
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nextnode = cur.next
            cur.next = prev
            prev = cur 
            cur = nextnode
        return prev