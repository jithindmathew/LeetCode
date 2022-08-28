class Solution:
    def countGoodRectangles(_, A): return (
        B := [min(a, b) for a, b in A]).count(max(B))
