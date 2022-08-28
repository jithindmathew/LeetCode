# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        cur = head
        ans = []

        while cur:
            ans.append(cur.val)
            cur = cur.next

        ans.sort()

        anss = ListNode(0)

        cur = anss

        for i in ans:
            cur.next = ListNode(i)
            cur = cur.next

        return anss.next
