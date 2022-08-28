class Solution:
    """
    def isPalindrome(self, s: str) -> bool:
        # 65, 122
        count = 0
        for i in s:
            if 65 <= ord(i) <= 90:
                s = s.replace(i, chr(ord(i) + 32))
                count += 1
                continue

            if 0 <= ord(i) <= 47 or 58 <= ord(i) <= 64 or ord(i) > 122 or 91 <= ord(i) <= 96:
                s = s.replace(i, "")
            else:
                count += 1

        for i in range(count):
            if s[i] != s[count - 1 - i]:
                return False
        return True
    """

    def isPalindrome(self, s: str) -> bool:
        # deleting punctuations and converting to lowercase
        l = [x.lower() for x in s if x.isalnum()]
        return l == l[::-1]
