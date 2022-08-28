# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        ans = ''
        while node != None:
            ans += str(node.val)
            node = node.next
        return int(ans, 2)