class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i, val in enumerate(arr):
            start = n - i  # number of arrays starting at index i
            end = i + 1
            
            ans += val*((start*end + 1) // 2)
        return ans
            
            