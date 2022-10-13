# from typing import List
class Solution:
    def checkArithmeticSubarrays(
        self,
        nums: List[int],
        l: List[int],
        r: List[int]
    ) -> List[bool]:

        ans = [True] * len(r)

        for i in range(len(r)):
            ans[i] = self.check(nums[l[i]: r[i] + 1])

        return ans

#     def check(self, arr: List[int]) -> bool:
#         if len(arr) < 2:
#             return False

#         arr.sort()

#         d = arr[1] - arr[0]

#         for i in range(2, len(arr)):
#             if arr[i] - arr[i - 1] != d:
#                 return False

#         return True

    def check(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return False

        mi = min(arr)
        ma = max(arr)

        if (ma - mi) % (len(arr) - 1) != 0:
            return False

        d = (ma - mi) // (len(arr) - 1)

        temp1 = set([mi + (i - 1) * d for i in range(1, len(arr) + 1)])
        temp2 = set(arr)

        if len(temp2) != len(temp1):
            return False

        for i in temp2:
            if i not in temp1:
                return False

        return True
