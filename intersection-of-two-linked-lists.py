# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self,headA: ListNode, headB: ListNode) -> ListNode:
        
        curra = headA
        currb = headB
        
        while curra != currb:
            if curra:
                curra = curra.next
            else:
                curra = headB
                
            if currb:
                currb = currb.next
            else:
                currb = headA
            
        return currb
        