from typing import *


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        source = image[sr][sc]

        if color == source:
            return image

        def helper(sr, sc):
            if image[sr][sc] == source:
                image[sr][sc] = color
                if sr >= 1:
                    helper(sr - 1, sc)
                if sr < rows - 1:
                    helper(sr + 1, sc)
                if sc >= 1:
                    helper(sr, sc - 1)
                if sc < cols - 1:
                    helper(sr, sc + 1)
        helper(sr, sc)

        return image
