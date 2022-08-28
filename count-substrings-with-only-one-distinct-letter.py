# 1180

def countLetters(S: str) -> int:  # TODO 

    if S == "":
        return 0

    ans = 0
    count = 1

    for i in range(0, len(S) - 1):

        if S[i] != S[i + 1]:
            ans += (count * (count + 1)) // 2
            count = 1
        else:
            count += 1

    ans += (count * (count + 1)) // 2

    return ans


print(countLetters("aaaba"))
print(countLetters("aaaaaaaaaa"))
