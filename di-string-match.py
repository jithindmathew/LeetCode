class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        left = 0
        right = len(s)
        ans = [0]*len(s)
        index = 0
        
        for i in s:
            if i == "I":
                ans[index] = left
                index += 1
                left += 1
            else:
                ans[index] = right
                right -= 1
                index += 1
        ans.append(left)
        return ans
        