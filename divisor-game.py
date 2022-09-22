class Solution:
    def divisorGame(self, n: int) -> bool:
        if n & 1:
            return True
        return False
