class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        num = set()

        for i in arr:
            if i % 2 == 1:
                if i*2 in num:
                    return True
                else:
                    num.add(i)
            else:
                if i*2 in num or i//2 in num:
                    return True
                else:
                    num.add(i)
        return False


""" 
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashset = set()
        for i in arr:
            if i*2 in hashset or i%2==0 and i/2 in hashset:
                return True
            hashset.add(i)
        return False
                
"""
