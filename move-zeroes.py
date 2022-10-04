class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        index = 0

        for i in range(len(nums)):
            curr = nums[i]

            if curr != 0:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
