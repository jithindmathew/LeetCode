class Solution:
    def convert(self, s: str, num: int) -> str:
        if s == "":
            return s

        if num <= 1:
            return s

        ans = ""

        for i in range(num):
            if i == 0:
                ans += s[:: (num - 1)*2]

            elif i == num - 1:
                ans += s[i:: (num - 1)*2]

            else:
                temp = i
                counter = 0

                spacea = 2*(num - i - 1)
                spaceb = 2*i

                while temp < len(s):
                    ans += s[temp]

                    if counter % 2 == 0:
                        temp += spacea
                    else:
                        temp += spaceb
                    counter += 1

        return ans


"""
"PINALSIGYIRPI"

"PINALSIGYAHRPI"

"""
