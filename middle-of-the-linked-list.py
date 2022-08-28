# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        
        n = 0
        while temp:
            n += 1
            temp = temp.next
        n = (n // 2)
        
        while n:
            head = head.next
            n -= 1
        return head
        