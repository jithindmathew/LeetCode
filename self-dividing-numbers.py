class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def self_dividing(x: int) -> bool:
            for i in str(x):
                if i == '0':
                    return False
                if x % int(i) != 0:
                    return False
            return True

        ans = []

        for i in range(left, right + 1):
            if self_dividing(i):
                ans.append(i)
        return ans
