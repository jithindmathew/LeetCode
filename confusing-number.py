# 1056

def confusingNumber(n: int) -> bool:
    mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    
    ans = ""
    string = str(n)
    
    for i in string[::-1]:
        if i not in mapping:
            return False
        else:
            ans += mapping[i]
    return ans != string

print(confusingNumber(25))
print(confusingNumber(89))
print(confusingNumber(6))
print(confusingNumber(11))
