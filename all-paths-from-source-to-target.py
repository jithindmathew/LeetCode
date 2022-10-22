class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def backtrack(index, path):
            if index == len(graph) - 1:
                ans.append(path + [index])
                return

            for i in graph[index]:
                backtrack(i, path + [index])

        backtrack(0, [])

        return ans

