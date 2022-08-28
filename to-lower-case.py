
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = [""]*len(s)
        mapp = {
            "A": "a",
            "B": "b",
            "C": "c",
            "D": "d",
            "E": "e",
            "F": "f",
            "G": "g",
            "H": "h",
            "I": "i",
            "J": "j",
            "K": "k",
            "L": "l",
            "M": "m",
            "N": "n",
            "O": "o",
            "P": "p",
            "Q": "q",
            "R": "r",
            "S": "s",
            "T": "t",
            "U": "u",
            "V": "v",
            "W": "w",
            "X": "x",
            "Y": "y",
            "Z": "z"
        }
        for i in range(len(s)):
            if s[i] in mapp:
                ans[i] = mapp[s[i]]
            else:
                ans[i] = s[i]
        # return "".join(ans)
        return s.lower()
