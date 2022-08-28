class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        mapp = [0]*101

        for i in heights:
            mapp[i] += 1

        pntr = 1
        ans = 0

        for i in heights:

            while mapp[pntr] == 0 and pntr < len(mapp):
                pntr += 1

            if i != pntr:
                ans += 1

            mapp[pntr] -= 1

        return ans
