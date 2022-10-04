import collections
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        n = len(tokens)
        operators = set(['/', '+', '-', '*'])

        for i in range(n):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())

                if tokens[i] == '+':
                    stack.append(str(temp1 + temp2))
                elif tokens[i] == '*':
                    stack.append(str(temp1 * temp2))
                elif tokens[i] == '/':
                    stack.append(str(int(temp2 / temp1)))
                elif tokens[i] == '-':
                    stack.append(str(temp2 - temp1))

        return stack[0]
