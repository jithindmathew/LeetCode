class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = ""
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] += shifts[i+1]
        for i in range(len(s)):
            ans += chr((ord(s[i]) - ord('a') + shifts[i]) % 26 + ord('a'))
        return ans
