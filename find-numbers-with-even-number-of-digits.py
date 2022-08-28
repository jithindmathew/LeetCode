class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        m = 0
        for i in nums:
            if self.digits(i) % 2 == 0:
                m += 1
        return m

    def digits(self, num: int) -> int:
        n = 0
        while num > 0:
            n += 1
            num //= 10
        return n
