class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        arr = sorted(arr)
        
        median = arr[(len(arr) - 1) // 2]
        
        i, j, num, ans = 0, len(arr) - 1, 0, []

        while num < k:
            if median - arr[i] > arr[j] - median:
                ans.append(arr[i])
                i += 1
            else: 
                ans.append(arr[j])
                j -= 1
            num += 1
        return ans
                