# 422

from typing import List

def validWordSquare(words: List[str]):
    
    for i in range(len(words)):
        
        for j in range(len(words[i])):
            
            if words[i][j] != words[j][i]:
                
                return False
            
    return True

print(validWordSquare(["abcd","bnrt","crmy","dtye"]))
print(validWordSquare(["abcd","bnrt","crm","dt"]))
print(validWordSquare(["ball","area","read","lady"]))
