# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        o = odd = ListNode(0)
        e = even = ListNode(0)

        ptr = True

        while head:

            if ptr:
                o.next = head
                o = o.next
            else:
                e.next = head
                e = e.next
            ptr = not ptr
            head = head.next

        e.next = None
        o.next = even.next
        return odd.next
