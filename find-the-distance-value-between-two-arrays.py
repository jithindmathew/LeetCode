class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for i in arr1:
            l = 0
            r = len(arr2) - 1
            
            while l <= r:
                mid = (l + r) // 2
                if abs(i - arr2[mid]) <= d:
                    break
                elif arr2[mid] < i:
                    l = mid + 1
                else:
                    r = mid - 1
            ans += l > r
        return ans