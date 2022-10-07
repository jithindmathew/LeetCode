from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(
        self,
        n: int,
        headID: int,
        managers: List[int],
        informTime: List[int]
    ) -> int:

        graph = defaultdict(list)

        for employee, manager in enumerate(managers):
            graph[manager].append(employee)

        def dfs(employee, time):
            new_time = time + informTime[employee]

            if not graph[employee]:
                return new_time

            max_time = new_time

            for child_employee in graph[employee]:
                max_time = max(max_time, dfs(child_employee, new_time))

            return max_time

        return dfs(headID, 0)
