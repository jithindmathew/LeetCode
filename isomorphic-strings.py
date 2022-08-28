class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictt_s_to_t = {}
        # s to t
        for i in range(len(s)):
            if s[i] in dictt_s_to_t:
                if dictt_s_to_t[s[i]] != t[i]:
                    return False
            else:
                if t[i] in dictt_s_to_t.values():
                    return False
                else:
                    dictt_s_to_t[s[i]] = t[i]

        return True


"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in mapping.values():
                    return False
                else:
                    mapping[s[i]] = t[i]
        
        return True
"""
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         d1 = {}
#         d2 = {}
        
#         for i, j in zip(s, t):
#             if (i in d1 and d1[i] != j) or (j in d2 and d2[j] != i):
#                 return False
#             d1[i] = j
#             d2[j] = i
#         return True