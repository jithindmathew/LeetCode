# 246

def isStrobogrammatic(num: str) -> bool:

    if not num:
        return False
    
    num_map = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}
    l = 0
    r = len(num) - 1

    while l <= r:

        if num[l] in num_map and num_map[num[l]] == num[r]:
            r -= 1
            l += 1

        else:
            return False

    return True

print(isStrobogrammatic("008"))
