class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def checkvowel(x: chr) -> bool:
            lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            return x in lst
        count = 0
        for i in range(int(len(s)/2)):
            if checkvowel(s[i]):
                count += 1
            if checkvowel(s[int(len(s)/2) + i]):
                count -= 1
        return count == 0
