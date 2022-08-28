class Node:
    def __init__(self, val =  None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        
        if index < 0 or index >= self.getlength():
            return -1
        
        current = self.head
        
        for i in range(index):
            current = current.next
        return current.val
        
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val, self.head, None)
        
        if self.head is None:
            self.head = node
        else:
            self.head.prev = node
            self.head = node
        return
        
        


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is None:
            self.head = Node(val, None, None)
            return
        
        iter = self.head
        
        while iter.next:
            iter = iter.next
        iter.next = Node(val, None, iter)
        
    def getlength(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.getlength():
            raise Exception("Invalide index")
        
        if index == 0:
            self.addAtHead(val)
            return
        count = 0
        
        curr = self.head
        
        while curr:
            if count == index - 1:
                node = Node(val, curr.next, curr)
                if curr.next:
                    curr.next.prev = node
                curr.next = node
                break
            count += 1
            curr = curr.next
        return

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        if index < 0 or index >= self.getlength():
            print("INVALID")
            return
            
        if index == 0 and self.getlength() == 1:
            return None
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return None
        
        
        curr = self.head
        count = 0
        
        while curr:
            if count == index:
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                break
            count += 1
            curr = curr.next
        return
        
        