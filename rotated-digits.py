class Solution:
    def rotatedDigits(self, N: int) -> int:
        # invalid:
        # 1. Contains 3, 4, 7
        # 2. Only contains 0, 1, 8

        count = 0
        for d in range(1, N+1):
            d_l = [ch for ch in str(d)]
            if '3' in d_l or '4' in d_l or '7' in d_l:
                continue
            if set(d_l).issubset({'0', '1', '8'}):
                continue
            count += 1
        return count
