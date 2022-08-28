# 1165

def calculateTime(keyboard: str, word: str) -> int:
    ans = 0
    prev = 0
    
    for i in word:
        ans += abs(keyboard.index(i) - prev)
        prev = keyboard.index(i)
        
    return ans

print(calculateTime("abcdefghijklmnopqrstuvwxyz", "cba"))
print(calculateTime("pqrstuvwxyzabcdefghijklmno", "leetcode"))
