class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = list(s)

        start_val = 0  # (

        for i, char in enumerate(s):
            if char == ')':
                if start_val == 0:
                    ans[i] = ""
                else:
                    start_val -= 1
            elif char == '(':
                start_val += 1

        end_val = 0  # )

        for i in range(len(ans) - 1, -1, -1):
            if ans[i] == '(':
                if end_val == 0:
                    ans[i] = ""
                else:
                    end_val -= 1
            elif ans[i] == ')':
                end_val += 1

        return ''.join(ans)


s = Solution()
print(s.minRemoveToMakeValid("))(("))
