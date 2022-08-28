# 1474


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNodes(head: ListNode, m: int, n: int) -> ListNode:

    p = head
    q = head
    
    if not p.next:
        return head
    
    while p:
        
        i = 0           
        while p.next and i < m - 1:
            p = p.next
            i += 1
        q = p
        j = 0
        
        while q and i < m + n :
            q = q.next
            i += 1
        p.next = q
        p = q
        
    return head


a, m, n = [1,2,3,4,5,6,7,8,9,10,11,12,13], 2, 3
#a, m, n = [1,2,3,4,5,6,7,8,9,10,11], 1, 3
#a, m, n = [1,2,3,4,5,6,7,8,9,10,11], 3, 1
#a, m, n = [9,3,7,7,9,10,8,2], 1, 2


for i in range(len(a)): 
    a[i] = ListNode(a[i])

for i in range(0, len(a) - 1):
    a[i].next = a[i + 1]
    
ans = deleteNodes(a[0], m, n)
print(ans)

while ans:
    print(ans.val)
    ans = ans.next
