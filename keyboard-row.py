class Solution:
    def findWords(self, words: List[str]) -> List[str]:                    
        
        first = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        second = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        third = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        
        ans = []
        
        for i in words:
            word_set = set(i.lower())
            if word_set&first == word_set:
                ans.append(i)
                continue
            
            if word_set&second == word_set:
                ans.append(i)
                continue
                
            if word_set&third == word_set:
                ans.append(i)
        return ans
                
            
                
                