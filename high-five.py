# 1086

from typing import List

def five(lst: List[int], value: int):
    
    if lst == []:
        lst.append(value)
        return

    else:
        if value <= lst[0] and len(lst) == 5:  
            return
        
        else:
            for i in range(len(lst)):
                if lst[i] > value:
                    lst.insert(i, value)
                    if len(lst) > 5:
                        lst.pop(0)
                    return
                
            lst.append(value)
            if len(lst) > 5:
                lst.pop(0)
            return
        
def highFive(items: List[List[int]]) -> List[List[int]]:
    
    a = dict()
    
    for i in items:
        if i[0] not in a:
            a[i[0]] = [i[1]]
        else:
            five(a[i[0]], i[1])
    
    ans = []
    
    for i in a:
        ans.append([i, sum(a[i])//5])
        
    return ans
    
print(highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
print(highFive([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]))
