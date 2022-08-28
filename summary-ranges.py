class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return nums

        ans = []

        first = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if first != nums[i - 1]:
                    ans.append(str(first) + "->" + str(nums[i - 1]))

                else:
                    ans.append(str(first))

                first = nums[i]

        if first == nums[-1]:
            ans.append(str(first))
        else:
            ans.append(str(first) + "->" + str(nums[-1]))

        return ans
