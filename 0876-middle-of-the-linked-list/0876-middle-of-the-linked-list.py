# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #tortoise method
        onestep = twostep = head
        while twostep and twostep.next:
            onestep = onestep.next
            twostep = twostep.next.next
        return onestep # since it is linkedlist so along with 3 , 4 & 5 will automatically get returned
        