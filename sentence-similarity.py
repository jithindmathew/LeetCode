# 716

from typing import List

def areSentencesSimilar(sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
    
    if len(sentence1) != len(sentence2):
        return False
    
    a = dict()
    
    for i in similarPairs:
        if i[0] not in a:
            a[i[0]] = i[1]
        if i[1] not in a:
            a[i[1]] = i[0]

    for i, j in zip(sentence1, sentence2):
        if i == j:
            continue
        if j != a[i]:
            return False
    return True

print(areSentencesSimilar(["great","acting","skills"], ["fine","drama","talent"], [["great","fine"],["drama","acting"],["skills","talent"]]))

print(areSentencesSimilar(["great"], ["great"], []))

print(areSentencesSimilar(["great"], ["doubleplus","good"], [["great","doubleplus"]]))
