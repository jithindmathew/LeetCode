from collections import defaultdict


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

#         a = defaultdict(int)

#         for i in nums:
#             a[i] += 1

#         j = 0

#         for i in range(a[0]):
#             nums[j] = 0
#             j += 1
#         for i in range(a[1]):
#             nums[j] = 1
#             j += 1
#         for i in range(a[2]):
#             nums[j] = 2
#             j += 1

        i = 0
        l, r = 0, n - 1

        while i <= r:

            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1

            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                i -= 1
            i += 1
