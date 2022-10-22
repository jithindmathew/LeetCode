class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_skip = 0
        t_skip = 0

        s_end = len(s) - 1
        t_end = len(t) - 1

        while s_end >= 0 or t_end >= 0:
            while s_end >= 0:
                if s[s_end] == '#':
                    s_skip += 1
                    s_end -= 1

                elif s_skip > 0:
                    s_skip -= 1
                    s_end -= 1
                else:
                    break

            while t_end >= 0:
                if t[t_end] == '#':
                    t_skip += 1
                    t_end -= 1

                elif t_skip > 0:
                    t_skip -= 1
                    t_end -= 1
                else:
                    break

            if s_end >= 0 and \
               t_end >= 0 and \
               s[s_end] != t[t_end]:
                return False

            if (s_end >= 0) != (t_end >= 0):
                return False

            s_end -= 1
            t_end -= 1

        return True
