# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(-1, head)

        prev = dummy
        curr = head

        while curr and curr.next:
            temp1 = curr.next.next
            temp2 = curr.next

            curr.next = temp1
            prev.next = temp2
            prev.next.next = curr

            prev = prev.next.next
            curr = prev.next

        return dummy.next
