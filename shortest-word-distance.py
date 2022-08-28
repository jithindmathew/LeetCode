# 243

import sys
from typing import List

def shortestDistance(words : List[str], word1: str, word2: str) -> int:

    if not words or not word1 or not word2:
        return -1
    
    idx1 = -1
    idx2 = -1
    ans = sys.maxsize
    
    for i in range(len(words)):

        if words[i] == word1:
            idx1 = i
        
        if words[i] == word2:
            idx2 = i

        if idx1 != -1 and idx2 != -1:
            ans = min(ans, abs(idx1 - idx2))

    print(ans)
    return ans


print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "makes"))
