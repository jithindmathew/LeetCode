# 338

"""
Constraints:

0 <= n <= 100000

"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []
        ans.append(0)
        
        for i in range(1, n + 1):
            if (i & 1) != 0:
                ans.append(ans[i - 1] + 1)
            else:
                ans.append(ans[i >> 1])
                
        return ans
