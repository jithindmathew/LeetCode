class Solution:
    def toHex(self, num: int) -> str:
        mapp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        
        if num < 0:
            num = 2**32 + num
            
        if num == 0:
            return "0"
        
        ans = ""
        
        while num:
            rem = num % 16
            ans = mapp[rem] + ans
            num = num // 16

        return ans
        