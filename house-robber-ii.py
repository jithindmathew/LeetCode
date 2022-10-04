
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)

        a = b = c = d = 0

        for i in range(len(nums) - 1):
            a, b = b, max(b, a + nums[i])
            c, d = d, max(d, c + nums[i + 1])

        return max(b, d)

s = Solution()

s.rob([2, 3, 2])

s.rob([1, 2, 3, 1])

s.rob([1, 2, 3])

