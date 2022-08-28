# 244

from typing import *
import sys

class WordDistance:
    
    def __init__(self, words: List[str]):
        self.dictionary = {}
        for index, item in enumerate(words):
            self.dictionary[item] = self.dictionary.get(item, []) + [index]
            
    def shortest(self, word1: str, word2: str):
        lst1, lst2 = self.dictionary.get(word1), self.dictionary.get(word2)
        lst1n, lst2n = len(lst1), len(lst2)
        i, j = 0, 0
        ans = sys.maxsize
        
        while i < lst1n and j < lst2n:
            ans = min(ans, abs(lst1[i] - lst2[j]))
            if lst1[i] < lst2[j]:
                i += 1
            else:
                j += 1
                
        return ans


print(WordDistance(["practice", "makes", "perfect", "coding", "makes"]).shortest("coding", "practice"))
