# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()

        cur = ans

        carry = 0

        while l1 or l2 or carry:
            val_one = l1.val if l1 else 0
            val_two = l2.val if l2 else 0

            value = val_one + val_two + carry

            carry = value // 10

            value = value % 10

            cur.next = ListNode(value)

            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans.next
