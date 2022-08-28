class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        min_dist = 888888
        b = -1

        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                if abs(x - points[i][0]) + abs(y - points[i][1]) < min_dist:
                    min_dist = abs(x - points[i][0]) + abs(y - points[i][1])
                    b = i
        return b
