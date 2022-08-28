# 1119

def removeVowels(s: str) -> str:
    mapping = set(('a', 'e', 'i', 'o', 'u'))
    ans = ""

    for i in s:
        if i not in mapping:
            ans += i

    return ans


print(removeVowels("leetcode"))
print(removeVowels("aeiou"))
print(removeVowels("leetcodeisacommunityforcoders"))
