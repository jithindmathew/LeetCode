# 760

def anagramMappings(A: List[int], B: List[int]) -> List[int]:
    a = dict()
    
    for i in range(len(B)):
        a[B[i]] = i
        
    ans = [0]*len(B)
    
    for i in range(len(B)):
        ans[i] = a[A[i]]
        
    return ans

print(anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]))
