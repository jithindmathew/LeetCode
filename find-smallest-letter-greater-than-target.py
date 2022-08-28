class Solution:
    def nextGreatestLetter(self, l: List[str], t: str) -> str:
        if t >= l[-1] or t < l[0]:
            return l[0]
        left = 0
        right = len(l) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if l[mid] > t:
                right = mid - 1
            if t >= l[mid]:
                left = mid + 1
        
        if l[right] <= t:
            return l[right + 1]
        else:
            return l[right]
            