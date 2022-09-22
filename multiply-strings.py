class Solution:
    def multiply(self, n1: str, n2: str) -> str:
        if n1 == '0' or n2 == '0':
            return '0'
        ans = [0] * (len(n1) + len(n2))

        multiplier = 0

        def add(temp_, multiplier_):
            ans[-1 - multiplier_] += temp_

            # reorganising array

            index = -1 - multiplier_

            while index > -len(ans):
                if ans[index] > 9:
                    carry = ans[index] // 10
                    ans[index - 1] += carry
                    ans[index] = ans[index] % 10

                else:
                    break

                index -= 1

        for i in range(len(n2) - 1, -1, -1):
            for j in range(len(n1) - 1, -1, -1):

                temp = (ord(n2[i]) - ord('0')) * (ord(n1[j]) - ord('0'))  # *(10**multiplier)

                add(temp, multiplier)

                multiplier += 1
            multiplier = len(n2) - i

        return "".join([str(i) for i in ans]).lstrip('0')
