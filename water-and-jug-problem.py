from math import gcd


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        return targetCapacity <= (jug1Capacity + jug2Capacity) and \
            targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0
