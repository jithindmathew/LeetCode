
from typing import *
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        
        def check(email):
            lst = email.split("@")
            lst[0] = lst[0].replace(".", "")
            if "+" in lst[0]:
                lst[0] = lst[0][0:lst[0].find("+")]
            return "@".join(lst)
        
        for i in emails:
            ans.add(check(i))
        print(ans)
        return len(ans)
        