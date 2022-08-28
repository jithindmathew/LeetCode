class Solution:
    def kClosest(self, points, k):
        if k >= len(points):
            return points

        return sorted(points, key=lambda i: i[0]**2 + i[1]**2)[:k]
