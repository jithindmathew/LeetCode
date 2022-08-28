# class Solution:
#     def tribonacci(self, n: int) -> int:
# #         def helper(n):
# #             if n == 0:
# #                 return 0
# #             if n == 1 or n == 2:
# #                 return 1
# #             return helper(n - 1) + helper(n - 2) + helper(n - 3)
        
# #         return helper(n)
#         ans = [0]*38
        
#         ans[1] = 1
#         ans[2] = 1
        
#         for i in range(3, 38):
#             ans[i] = ans[i - 1] + ans[i - 2] + ans[i - 3]
#         return ans[n]
import numpy as np

a = np.array([0, 9, 77])

print(a)