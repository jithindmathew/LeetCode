from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        if len(nums) < 4:
            return []
        ans = set()
        nums.sort()

        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    summ = nums[i] + nums[j] + nums[left] + nums[right]
                    if summ == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1

                    elif summ < target:
                        left += 1
                    else:  # summ > target
                        right -= 1
        return ans
