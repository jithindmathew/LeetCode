class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        increasing = decreasing = 0
        for i in range(len(arr) - 1):
            if decreasing == 0 and arr[i + 1] > arr[i]:
                increasing += 1
            if increasing > 0 and arr[i + 1] < arr[i]:
                decreasing += 1

        return (increasing + decreasing == len(arr) - 1) and increasing > 0 and decreasing > 0
