class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        i = len(num) - 1
        carry = 0

        while k > 0 or carry > 0:
            if i < 0:
                temp = k % 10 + carry
                carry = temp // 10

                num.insert(0, temp % 10)

                k //= 10

                continue

            temp = num[i] + k % 10 + carry
            num[i] = temp % 10

            carry = temp // 10

            k //= 10
            i -= 1

        if carry:
            num.insert(0, carry)

        return num
