# 1213

from typing import List

"""

def arraysIntersection(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    a = dict()
    
    for i in arr1:
        a[i] = a.get(i, 0) + 1
    
    for i in arr2:
        a[i] = a.get(i, 0) + 1
        
    for i in arr3:
        a[i] = a.get(i, 0) + 1
        
    ans = []
        
    for i in a:
        if a[i] == 3:
            ans.append(i)
    
    return ans
    
"""

def arraysIntersection(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:

    i, j, k = 0, 0, 0
    ni, nj, nk = len(arr1), len(arr2), len(arr3)
    ans = []
    
    while ((i < ni) and (j < nj) and (k < nk)):
        if (arr1[i] == arr2[j]) and (arr2[j] == arr3[k]):
            ans.append(arr2[j])
            i += 1
            j += 1
            k += 1
            continue
            
        if (arr1[i] < arr2[j]):
            i += 1
        
        elif (arr2[j] < arr3[k]):
            j += 1
        
        else:
            k += 1
    return ans
    

print(arraysIntersection([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8]))
print(arraysIntersection([197,418,523,876,1356], [501,880,1593,1710,1870], [521,682,1337,1395,1764]))
