# 159



def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    start = 0
    end = 0
    
    ans = 0
    d = dict()
    
    while end < len(s):
        d[s[end]] = end
        if len(d) > 2:
            min_index = min(d.values())
            start = min_index + 1
            del d[s[min_index]]
        ans = max(ans, end - start + 1)
        end += 1
    return ans

print(lengthOfLongestSubstringTwoDistinct("eceba"))
print(lengthOfLongestSubstringTwoDistinct("ccaabbb"))
print(lengthOfLongestSubstringTwoDistinct("bbbbbbbbbbb"))
