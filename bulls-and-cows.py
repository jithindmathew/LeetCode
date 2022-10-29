from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        s = Counter(secret)
        g = Counter(guess)

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
                s[guess[i]] -= 1

        for i in range(len(guess)):
            if guess[i] != secret[i] and \
               guess[i] in s and \
               s[guess[i]] > 0:
                cows += 1
                s[guess[i]] -= 1

        return str(bulls) + "A" + str(cows) + "B"
