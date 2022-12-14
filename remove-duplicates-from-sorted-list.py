# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head is None:
            return head
        
        curr = head
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
                continue
            
            curr = curr.next
        
        return head
        