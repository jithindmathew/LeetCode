from typing import *

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        for i in ops:
            if i.isdigit() or i.startswith("-") and i[1:].isdigit():
                ans.append(int(i))
            elif i == "C":
                ans.pop()
            elif i == "D":
                ans.append(ans[-1]*2)
            elif i == "+":
                ans.append(ans[-1] + ans[-2])
        return sum(ans)
