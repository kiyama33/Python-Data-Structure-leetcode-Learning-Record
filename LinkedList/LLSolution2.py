from typing import List,Optional,ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class LLSolution2:
    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        prev = None
        if head.val==val:
            return head.next
        while cur:
            prev = cur
            cur = cur.next
            if cur.val==val:
                prev.next = cur.next
                break
        return head