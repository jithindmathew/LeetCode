# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if head is None:
            return None

        curr = head
        length = 1

        while curr.next:
            length += 1
            curr = curr.next

        k = k % length

        if length == 1 or k == 0:
            return head

        first = head

        for i in range(length - k - 1):
            first = first.next
        temp = first.next
        a = temp
        first.next = None

        for i in range(k - 1):
            temp = temp.next
        temp.next = head
        return a
