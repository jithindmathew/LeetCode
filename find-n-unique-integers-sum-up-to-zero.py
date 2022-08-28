class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            return list(range(-(n-1), n, 2))
        else:
            return list(range(-(n//2), (n//2) + 1, 1))
