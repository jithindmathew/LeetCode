# 12

"""
Constraints
1 <= num <= 3999

"""

class Solution:
    def intToRoman(self, num: int) -> str:
        b = ""
        a = {1000: "M",
        500: "D",
        100: "C",
        50: "L",
        10: "X",
        5: "V",
        1: "I"}
        for i in a:
            b += (num // i) * a[i]
            num -= (num // i) * i
        b = b.replace("VIIII", "IX")
        b = b.replace("IIII", "IV")
        b = b.replace("LXXXX", "XC")
        b = b.replace("XXXX", "XL")
        b = b.replace("DCCCC", "CM")
        b = b.replace("CCCC", "CD")
        return b
