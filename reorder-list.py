# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        stack = deque()

        while temp:
            stack.append(temp.val)
            temp = temp.next

        curr = head
        flag = True

        while curr:
            if flag:
                value = stack.popleft()
                flag = False
            else:
                value = stack.pop()
                flag = True
            curr.val = value
            curr = curr.next

        return head
