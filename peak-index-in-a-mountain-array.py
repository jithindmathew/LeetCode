class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # for i in range(1, len(arr) - 1):
        #     if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
        #         return i
        
        l = 0
        r = len(arr) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
                return mid
            elif arr[mid - 1] < arr[mid] and arr[mid + 1] > arr[mid]:
                l = mid
            else:
                r = mid
        return l