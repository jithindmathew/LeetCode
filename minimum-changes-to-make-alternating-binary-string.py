class Solution:
    def minOperations(self, s: str) -> int:

        zero, one = 0, 0

        if s[0] == "0":
            one += 1
        else:
            zero += 1

        for i in range(1, len(s)):

            if i % 2 == 1:

                if s[i] == "1":
                    one += 1
                    continue
                else:
                    zero += 1
                    continue
            else:
                if s[i] == "0":
                    one += 1
                    continue
                else:
                    zero += 1
                    continue

        return min(zero, one)
