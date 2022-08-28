# 186

def reversefromitoj(s, i, j):
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return
      
def reverseWords(s : List[str]) -> None:
    
    reversefromitoj(s, 0, len(s) - 1)
    start = 0
    
    for i in range(len(s)):
        if s[i] == ' ':
            reversefromitoj(s, start, i - 1)
            start = i + 1
        if i == len(s) - 1:
            reversefromitoj(s, start, i)
            
            
        
a = ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']
b = ['r', 'e', 'v', 'e', 'r', 's', 'e', ' ', 'w', 'o', 'r', 'd', 's', ' ', 'i', 'n', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']
print(reverseWords(a))
print(reverseWords(b))
print(a)
print(b)
