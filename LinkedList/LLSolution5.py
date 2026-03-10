from typing import Optional,List,ListNode
class Solution:
    def trainningPlan(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        if l1==None and l2==None:
            return None
        while l1:
            list.append(l1.val)
            l1=l1.next
        while l2:
            list.append(l2.val)
            l2=l2.next
        list.sort()
        head = ListNode(list[0])
        cur = head
        for node in list[1:]:
            cur.next = ListNode(node)
            cur = cur.next
        return head