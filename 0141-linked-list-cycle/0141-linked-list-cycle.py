# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p, q = head, head
        while p and q :
            if p.next:
                p = p.next
            else:
                break
            if q.next and q.next.next :
                q = q.next.next
            else:
                break
            if p == q:
                return True
        return False
        