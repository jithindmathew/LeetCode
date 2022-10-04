from typing import List


class Solution:
    def findRepeatedDnaSequences(
        self,
        s: str
    ) -> List[str]:

        def encrypt(s_):
            mapp = {
                'A': 0,
                'T': 1,
                'G': 2,
                'C': 3
            }

            ans_ = 0

            for i in range(10):
                ans_ = (ans_ << 2) + mapp[s_[i]]

            return ans_

#         def decrypt(val):
#             ans_ = ""
#             ans_index = 9

#             for _ in range(10):
#                 b = val & 1
#                 val >>= 1
#                 a = val & 1
#                 val >>= 1

#                 if a and b:
#                     ans_ = 'C' + ans_
#                 elif a and not b:
#                     ans_ = 'G' + ans_
#                 elif not a and b:
#                     ans_ = 'T' + ans_
#                 else:
#                     ans_ = 'A' + ans_

#                 ans_index -= 1

#             return ans_

        n = len(s)
        sett = set()

        if n < 11:
            return []

        ans = set()

        for i in range(0, n - 9):
            hash_val = encrypt(s[i: i + 10])

            if hash_val not in sett:
                sett.add(hash_val)
            else:
                ans.add(s[i: i + 10])

        # return [decrypt(i) for i in ans]
        return ans
