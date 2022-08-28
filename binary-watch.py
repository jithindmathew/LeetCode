from typing import *


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """ans = set()
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count("1") == turnedOn:
                    ans.add("%d:%02d"%(h, m))
        return ans"""

        return [
            "%d:%02d" % (h, m) for h in range(12) for m in range(60) if (bin(h) + bin(m)).count("1") == turnedOn
        ]
