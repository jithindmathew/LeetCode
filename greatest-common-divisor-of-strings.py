class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        if str2 == str1:
            return str2

        if len(str2) > len(str1):
            return self.gcdOfStrings(str2, str1)

        if str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        return ''
