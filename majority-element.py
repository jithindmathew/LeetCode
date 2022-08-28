class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        item = nums[0]

        cnt = 1

        for i in range(1, len(nums)):

            if cnt == 0:
                item = nums[i]

            if item == nums[i]:
                cnt += 1

            else:
                cnt -= 1

        return item
