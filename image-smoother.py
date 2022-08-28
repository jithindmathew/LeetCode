from copy import deepcopy


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = deepcopy(img)
        row = len(img)
        col = len(img[0])

        for i in range(len(img)):
            for j in range(len(img[0])):
                summ = 0
                count = 0

                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= i+x < row and 0 <= j+y < col:
                            count += 1
                            summ += img[x+i][j+y]

                ans[i][j] = summ//count

        return ans
