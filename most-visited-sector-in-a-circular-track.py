class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        if rounds[0] > rounds[-1]:
            return [i for i in range(1, rounds[-1] + 1)] + [j for j in range(rounds[0], n+1)]
        return [i for i in range(rounds[0], rounds[-1] + 1)]
            