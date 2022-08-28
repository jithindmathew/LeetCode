# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = dict()
#         for i in nums:
#             if i not in seen:
#                 seen[i] = 2
#                 continue
#             else:
#                 return True
#         return False

from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return max(Counter(nums).values()) > 1