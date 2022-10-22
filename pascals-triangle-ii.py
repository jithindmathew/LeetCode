class Solution:
    def getRow(self, row: int) -> List[int]:

        if row == 0:
            return [1]
        if row == 1:
            return [1, 1]

        ans = [1]
        sth = self.getRow(row - 1)
        for i in range(row - 1):
            ans.append(sth[i] + sth[i + 1])
        ans.append(1)

        return ans

