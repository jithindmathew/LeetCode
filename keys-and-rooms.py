from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        distinct_rooms = {0}
        temp = 0
        stack = []

        for i in rooms[0]:
            if i not in distinct_rooms:
                distinct_rooms.add(i)
                stack.append(i)
                temp += 1

        while stack:
            temp2 = stack.pop()

            for i in rooms[temp2]:
                if i not in distinct_rooms and i:
                    distinct_rooms.add(i)
                    stack.append(i)
                    temp += 1

        return temp == n - 1
