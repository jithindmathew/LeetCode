# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        curr_node = head
        prev_node = None
        
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        head = prev_node
        return head
"""
1 > 2 > 3 > 4 > 5 > NONE
    ^

curr = 2
prev = 2
next = 3
              2 > 1 > None
              ^




        
        
class Solution:
    def reverseList(self, head):
        
        :type head: ListNode
        :rtype: ListNode
        
        prev_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next # Remember next node
            curr_node.next = prev_node  # REVERSE! None, first time round.
            prev_node = curr_node  # Used in the next iteration.
            curr_node = next_node  # Move to next node.
        head = prev_node
        return head
"""