from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def helper(curr):
            for i in range(4):

                digit = str((int(curr[i]) + 1) % 10)
                new_str = curr[:i] + digit + curr[i + 1:]

                if new_str not in seen:
                    stack.append(new_str)
                    seen.add(new_str)

                digit = str((int(curr[i]) + 9) % 10)
                new_str = curr[:i] + digit + curr[i + 1:]

                if new_str not in seen:
                    stack.append(new_str)
                    seen.add(new_str)

        stack = deque()
        seen = set(deadends)

        if "0000" in seen:
            return -1

        stack.append(target)

        depth = 1

        while stack:
            n = len(stack)

            for _ in range(n):
                temp = stack.popleft()

                if temp == "0000":
                    return depth - 1

                helper(temp)

            depth += 1

        return -1
