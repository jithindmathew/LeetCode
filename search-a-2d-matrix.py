class Solution:
    def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        
        l = 0
        r = m - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= t <= matrix[mid][-1]:
                l, r = 0, n
                while l <= r:
                    mid_ = (l + r) // 2
                    if matrix[mid][mid_] == t:
                        return True
                    elif matrix[mid][mid_] < t:
                        l = mid_ + 1
                    else:
                        r = mid_ - 1
            elif matrix[mid][0] < t:
                l = mid + 1
            else:
                r = mid - 1
        return False
        
        print(l)
