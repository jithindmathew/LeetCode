# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: "Node") -> "Node":

        if not head:
            return head

        curr_node = head

        while curr_node and not curr_node.child:
            curr_node = curr_node.next

        if not curr_node:
            return head

        child = self.flatten(curr_node.child)

        curr_next = curr_node.next

        curr_node.child.prev = curr_node

        curr_node.child = None

        curr_node.next = child

        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = self.flatten(curr_next)

        if curr_next:
            curr_next.prev = curr_node

        return head

