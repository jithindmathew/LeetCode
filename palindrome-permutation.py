# 266

def canPermutePalindrome(s: str) -> bool:

    dictt = dict()

    for i in s:

        if i not in dictt:
            dictt[i] = 1
        else:
            dictt[i] += 1
    
    ans = 0

    for i in dictt:
        if dictt[i] % 2 == 1:
            ans += 1

    return ans <= 1

print(canPermutePalindrome("acyya"))
