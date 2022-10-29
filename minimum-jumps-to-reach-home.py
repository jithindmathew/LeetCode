from collections import deque
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:

        MAX_VAL = 2000 + a + b

        forb = set(forbidden)

        stack = deque()
        seen_1 = set()
        seen_2 = set()

        stack.append((0, 0))
        seen_1.add(0)
        seen_2.add(0)

        pos = 0
        jumps = 1

        while len(stack):

            n = len(stack)
            print(stack)

            for _ in range(n):
                pos, backjump = stack.popleft()

                if pos == x:
                    return jumps - 1

                new_pos_1 = pos + a
                new_pos_2 = pos - b

                if new_pos_1 not in forb and \
                   new_pos_1 not in seen_1 and \
                   new_pos_1 <= MAX_VAL:
                    stack.append((new_pos_1, 0))
                    seen_1.add(new_pos_1)

                if new_pos_2 > 0 and \
                   new_pos_2 not in forb and \
                   new_pos_2 not in seen_2 and \
                   new_pos_2 <= MAX_VAL and \
                   backjump < 1:
                    stack.append((new_pos_2, 1))
                    seen_2.add(new_pos_2)

            jumps += 1

        return -1


s = Solution()
s.minimumJumps(
    [162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54, 154,
        133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98],
    29,
    98,
    80
)
