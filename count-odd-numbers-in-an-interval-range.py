class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if not (high - low + 1) & 1:
            return (high - low + 1)//2

        else:
            if high & 1:
                return (high - low) // 2 + 1
            return (high - low) // 2
