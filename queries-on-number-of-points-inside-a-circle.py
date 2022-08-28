class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0]*len(queries)
        for i, query in enumerate(queries):
            ans_j = 0
            for j in points:
                if ((query[0] - j[0])**2 + (query[1] - j[1])**2) <= query[2]**2:
                    ans_j += 1
            ans[i] = ans_j
        return ans
