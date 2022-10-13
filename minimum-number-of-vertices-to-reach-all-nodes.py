class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        temp = set(range(n))

        for start, end in edges:
            if end in temp:
                temp.remove(end)

        return temp
