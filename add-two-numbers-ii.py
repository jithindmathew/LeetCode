class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def _get_length(node1, node2):
            n1 = 1
            n2 = 1

            while node1.next or node2.next:
                if node1.next:
                    n1 += 1
                    node1 = node1.next

                if node2.next:
                    n2 += 1
                    node2 = node2.next

            return n1, n2

        def _helper(n1, n2, nn1, nn2, depth):

            if n1.next is None and n2.next is None:
                n1.val += n2.val

            elif n1.next is not None or n2.next is not None:
                if depth <= nn1 - nn2:
                    carry = _helper(n1.next, n2, nn1, nn2, depth + 1)

                else:
                    carry = _helper(n1.next, n2.next, nn1, nn2, depth + 1)
                    n1.val += n2.val

                n1.val += carry

            carry = n1.val // 10
            n1.val %= 10

            return carry

        ln1, ln2 = _get_length(l1, l2)

        flag = ln1 > ln2

        carry = (_helper(l1, l2, ln1, ln2, 1) if flag else _helper(l2, l1, ln2, ln1, 1))

        if not carry:
            return (l1 if flag else l2)

        ans = ListNode(val=carry, next=(l1 if flag else l2))

        return ans
