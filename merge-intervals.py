import numpy as np
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        n = max(intervals, key=lambda x: x[1])[1]

        temp = np.zeros(n + 1, np.uint8)

        for l, r in intervals:
            if l < r:
                if (temp[l] == 0 or temp[l] == 3) and (temp[r] == 0 or temp[r] == 3):
                    temp[l] = 2
                    temp[r] = 2

                    temp[l + 1: r] = 1

                elif temp[l] == 2 and temp[r] == 2:
                    if np.count_nonzero(temp[:l + 1] == 2) & 1:
                        temp[l] = 2
                    else:
                        temp[l] = 1

                    if np.count_nonzero(temp[r:] == 2) & 1:
                        temp[r] = 2
                    else:
                        temp[r] = 1

                    temp[l + 1: r] = 1

                elif temp[l] == 2 and temp[r] == 1:
                    if np.count_nonzero(temp[:l + 1] == 2) & 1:
                        temp[l] = 2
                    else:
                        temp[l] = 1

                    temp[l + 1: r] = 1

                elif temp[l] == 2 and (temp[r] == 0 or temp[r] == 3):
                    temp[r] = 2
                    if np.count_nonzero(temp[: l + 1] == 2) & 1:
                        temp[l] = 2
                    else:
                        temp[l] = 1

                    temp[l + 1: r] = 1

                elif (temp[l] == 0 or temp[l] == 3) and temp[r] == 2:
                    temp[l] = 2
                    if np.count_nonzero(temp[r: n + 1] == 2) & 1:
                        temp[r] = 2
                    else:
                        temp[r] = 1
                    temp[l + 1: r] = 1

                elif temp[l] == 1 and temp[r] == 2:
                    if np.count_nonzero(temp[r: n + 1] == 2) & 1:
                        temp[r] = 2
                    else:
                        temp[r] = 1

                    temp[l + 1: r] = 1

                elif temp[l] == 1 and (temp[r] == 0 or temp[r] == 3):
                    temp[r] = 2
                    temp[l + 1: r] = 1

                elif temp[l] == 1 and temp[r] == 1:
                    temp[l + 1: r] = 1

                elif (temp[l] == 0 or temp[l] == 3) and temp[r] == 1:
                    temp[l] = 2
                    temp[l + 1: r] = 1

            else:  # l == r
                if temp[l] == 0:
                    temp[r] = 3

        i = 0

        flag_left = False
        num_left = None

        ans = []

        while i < n + 1:
            if temp[i] == 2 and not flag_left:
                flag_left = True
                num_left = i

            elif temp[i] == 2 and flag_left:
                ans.append([num_left, i])
                flag_left = False
                num_left = None

            elif temp[i] == 3:
                ans.append([i, i])

            i += 1

        return ans
        """
        intervals.sort(key=lambda i: i[0])

        ans = [intervals[0]]

        for left, right in intervals[1:]:
            lastend = ans[-1][1]

            if left <= lastend:
                ans[-1][1] = max(lastend, right)
            else:
                ans.append([left, right])

        return ans
