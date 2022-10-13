class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        temp = [0] * n

        for i in range(len(trust)):
            temp[trust[i][0] - 1] -= 1
            temp[trust[i][1] - 1] += 1

        for i in range(len(temp)):
            if temp[i] == n - 1:
                return i + 1

        return -1
