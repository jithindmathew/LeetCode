# 17

"""
Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""

class Solution:
    def comb(self, lst1: str, lst2: str):
        ans = []
        
        for i in lst1:
            for j in lst2:
                ans.append(i + j)
                
        return ans
    
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        if digits == "":
            return []
        
        result = mapping[digits[0]]
        
        for i in range(1, len(digits)):
            result = self.comb(result, mapping[digits[i]])
            
        return result
