class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_lst = list(pattern)
        s_lst = s.split(" ")
        dictt = {}
        if len(p_lst) != len(s_lst):
            return False
        for i in range(len(pattern)):
            if p_lst[i] in dictt:
                if dictt[p_lst[i]] != s_lst[i]:
                    return False
            else:
                if s_lst[i] in dictt.values():
                    return False
                else:
                    dictt[p_lst[i]] = s_lst[i]
        return True
