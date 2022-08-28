class Solution:
    def average(self, s: List[int]) -> float:
        # return (sum(s) - min(s) - max(s))/(len(s) - 2)
        
        mini = 1000000
        maxi = 1000
        
        summ = 0
        
        for i in range(len(s)):
            summ += s[i]
            
            if s[i] < mini:
                mini = s[i]
            if s[i] > maxi:
                maxi = s[i]
        return (summ - mini - maxi)/(i - 1)