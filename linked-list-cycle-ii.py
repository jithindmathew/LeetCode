# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        def check_cycle(head: ListNode) -> bool:
            slow = fast = head

            while slow and fast and fast.next:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    return fast
            return False

        ans = check_cycle(head)

        if ans == False:
            return None

        s = head

        while True:
            if s == ans:
                break
            s = s.next
            ans = ans.next
        return s
