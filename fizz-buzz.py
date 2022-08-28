class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        ans = []

        fizz = buzz = 0

        for i in range(1, n + 1):

            word = ""
            fizz += 1
            buzz += 1

            if fizz == 3:
                word += "Fizz"
                fizz = 0

            if buzz == 5:
                word += "Buzz"
                buzz = 0

            ans.append(word) if word != "" else ans.append(str(i))
        return ans
