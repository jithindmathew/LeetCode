class Solution:
    def secondHighest(self, s: str) -> int:

        largest = second = -2

        for i in s:

            if i.isnumeric():
                if int(i) > largest:
                    second = largest
                    largest = int(i)

                if largest > int(i) > second:
                    second = int(i)

        return second if second >= 0 else -1
