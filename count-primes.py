class Solution:
    def countPrimes(self, n: int) -> int:

        if n == 0 or n == 1:
            return 0

        prime = [True for _ in range(n + 1)]

        prime[0], prime[1] = False, False

        i = 2

        count = 0

        while i*i <= n:
            if prime[i]:
                for j in range(i*2, n + 1, i):
                    prime[j] = False
            i += 1

        for i in range(n):
            if prime[i]:
                count += 1
        return count
