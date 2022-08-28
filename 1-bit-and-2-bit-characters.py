class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        ans = False
        while i < n:
            if bits[i] == 1:
                i += 2

            else:
                if i == n - 1:
                    ans = True
                i += 1
        return ans and bits[-1] == 0


"""
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool
        carry = False
        for b in bits[:-1]:
            carry = not carry and b
        return not carry
"""
