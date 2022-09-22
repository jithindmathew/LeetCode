from typing import List, int


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:

        def dfs(root):
            ans = root.importance
            for i in root.subordinates:
                ans += dfs(mpp[i])
            return ans

        mpp = dict()
        req = None

        for i in employees:
            mpp[i.id] = i
            if i.id == id:
                req = i
        return dfs(req)
