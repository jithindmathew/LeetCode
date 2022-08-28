class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_one = 0
        num_two = 0
        num_zero = 0

        for i in nums:
            if i == 0:
                num_zero += 1
            elif i == 1:
                num_one += 1
            else:
                num_two += 1
        nums[:] = [0]*num_zero + [1]*num_one + [2]*num_two
