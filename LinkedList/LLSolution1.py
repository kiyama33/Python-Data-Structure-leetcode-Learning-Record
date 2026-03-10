from typing import Optional,List,ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class LLSolution1:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        res = []
        if not head:
            return []
        prev = None
        curr = head
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        while prev:
            res.append(prev.val)
            prev = prev.next
        return res
""""
res = []
while head:
    res.append(head.val)
    head = head.next
res.reverse() #注意这个括号！！！
return res
"""