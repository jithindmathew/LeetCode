# 1065

def indexPairs(text: str, words: List[str]) -> List[List[int]]:
    ans = []
    
    for i in words:
        
        for j in range(len(text)):
            
            if text.startswith(i, j):
                ans.append([j, j + len(i) - 1])
                
    return ans
    
print(indexPairs("thestoryofleetcodeandme", ["story", "fleet", "leetcode"]))
print(indexPairs("ababa", ["aba","ab"]))
