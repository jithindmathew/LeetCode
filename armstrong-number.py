# 1134

def isArmstrong(N: int) -> bool:
    nn = N
    a = []
    
    while N > 9:
        a.append(N % 10)
        N = N // 10
    a.append(N)
    
    length = len(a)
    
    ans = 0
    for i in a:
        ans += i**length
        
    return ans == nn
    
print(isArmstrong(153))
print(isArmstrong(123))
print(isArmstrong(1634))
print(isArmstrong(371))
