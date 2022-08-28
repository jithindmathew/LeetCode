
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        dummy = new = Node(-1)
        curr = head
        old_new = {}
        
        while curr:
            new.next = Node(curr.val)
            old_new[curr] = new.next
            curr = curr.next
            new = new.next
        curr = head
        new = dummy.next
        
        while curr:
            if curr.random:
                new.random = old_new[curr.random]
            curr = curr.next
            new = new.next
        return dummy.next
        """
        
        #interweave
        #update
        # remove old node
        dummy = Node(-1)
        dummy.next = head
        curr = head
        
        while curr:
            temp = Node(curr.val)
            temp.next = curr.next
            curr.next = temp
            curr = temp.next
        
        curr = head
        
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = dummy
        old = head
        
        while old:
            curr.next = old.next
            curr = curr.next
            old = old.next.next
        return dummy.next
            