# 161


def isOneEditDistance(s: str, t: str) -> bool:
    sn = len(s)
    tn = len(t)
    
    if s == t or abs(sn - tn) > 1: 
        return False
    
    if sn == tn:
        count = 0
        for i in range(sn):
            if s[i] != t[i]:
                count += 1
        return count == 1
    
    elif sn > tn:
        for i in range(tn):
            if t[i] != s[i] and t[i] != s[i + 1]:
                return False
                
    else: # tn > sn
        for i in range(sn):
            if s[i] != t[i] and s[i] != t[i + 1]:
                return False
            
    return True
        
print(isOneEditDistance("ab", "acb"))
print(isOneEditDistance("cab", "ad"))
print(isOneEditDistance("1203", "1213"))

    
