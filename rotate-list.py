# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        curr = head
        n = 1

        while curr.next:
            curr = curr.next
            n += 1

        k %= n

        if n == 1 or k == 0:
            return head

        first = head

        for i in range(n - k - 1):
            first = first.next

        temp = first.next
        ans = first.next

        first.next = None

        while temp.next:
            temp = temp.next

        temp.next = head

        return ans
