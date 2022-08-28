class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(-1, -len(digits)-1, -1):
            if digits[i] + 1 > 9:
                digits[i] = 0
                carry = 1
                continue
            else:
                digits[i] += 1
                return digits
        if carry:
            digits = [1] + digits
        return digits
