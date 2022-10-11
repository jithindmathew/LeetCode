"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old_to_new = {
            None: None
        }
        curr = head

        while curr:
            temp = Node(curr.val)
            old_to_new[curr] = temp
            curr = curr.next

        curr = head

        while curr:
            temp = old_to_new[curr]
            temp.next = old_to_new[curr.next]
            temp.random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]
