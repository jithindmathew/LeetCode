from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_kth_node(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, next=head)
        group_prev = dummy

        while True:
            kth_node = self.get_kth_node(group_prev, k)

            if not kth_node:
                break

            group_next = kth_node.next

            # reverse linked list group
            prev = kth_node.next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next
            group_prev.next = kth_node
            group_prev = temp

        return dummy.next
