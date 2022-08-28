# 92

"""
Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head is None or left == right or head.next is None:
            return head
        
        dummy = ListNode(0, next = head)
        
        prev = dummy
        
        i = 1
        
        while i < left:
            prev = prev.next
            i += 1
            
        cur = prev.next
        nxt = cur.next
        
        while i < right:
            temp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = temp
            i += 1
            
        prev.next.next = nxt
        prev.next = cur
        
        return dummy.next
