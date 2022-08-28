class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = dict()
        start = dict()
        end = dict()
        for i, num in enumerate(nums):
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                start[num] = i
            end[num] = i
        max_freq = max(count.values())
        return min(end[num]-start[num]+1 for num, freq in count.items() if freq == max_freq)
