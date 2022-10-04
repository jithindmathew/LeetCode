class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 1

        ans = 0
        temp = [0] * 26

        mapp = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6,
            "H": 7,
            "I": 8,
            "J": 9,
            "K": 10,
            "L": 11,
            "M": 12,
            "N": 13,
            "O": 14,
            "P": 15,
            "Q": 16,
            "R": 17,
            "S": 18,
            "T": 19,
            "U": 20,
            "V": 21,
            "W": 22,
            "X": 23,
            "Y": 24,
            "Z": 25
        }

        temp[mapp[s[left]]] += 1
        temp[mapp[s[right]]] += 1

        while right < len(s) and left <= right:
            maxx = max(temp)
            summ = sum(temp)

            if right == len(s) - 1:

                if summ - maxx <= k:
                    ans = max(ans, summ)

                temp[mapp[s[left]]] -= 1
                left += 1

                continue

            if summ - maxx > k:
                temp[mapp[s[left]]] -= 1
                left += 1
                continue

            ans = max(ans, summ)

            right += 1
            temp[mapp[s[right]]] += 1

        return ans
