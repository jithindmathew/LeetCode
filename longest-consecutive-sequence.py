import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = nums
        heapq.heapify(a)
        max_len = 1
        countt = 1

        if len(nums) == 0:
            return 0

        first = heapq.heappop(a)

        while len(a) > 0:
            second = heapq.heappop(a)

            if (second - first == 1):
                countt += 1
                max_len = max(max_len, countt)

            elif (second - first > 1):
                countt = 1

            first = second

        return max_len
