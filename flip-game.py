# 293

from typing import List

def generatePossibleNextMoves(s: str) -> List[str]:

    ans = []

    for i in range(0, len(s) - 1):
        ans.append(s[:i] + "--" + s[i + 2:])
    
    return ans

print(generatePossibleNextMoves("++++++++++"))
