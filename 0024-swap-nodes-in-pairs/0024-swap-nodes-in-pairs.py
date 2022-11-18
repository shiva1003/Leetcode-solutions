# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        hed = head
        while hed and hed.next:
            hed.val,  hed.next.val = hed.next.val, hed.val
            hed = hed.next.next
        return head
            
        