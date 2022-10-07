from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        curr_sum = 0

        dictt = {
            0: 1
        }

        for i in nums:
            curr_sum += i

            diff = curr_sum - k

            ans += dictt.get(diff, 0)

            dictt[curr_sum] = 1 + dictt.get(curr_sum, 0)

        return ans
