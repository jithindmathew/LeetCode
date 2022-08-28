class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        l = arr
        ans = 0
        for i in range(len(l)-2):
            for j in range(i+1, len(l)-1):
                for k in range(j+1, len(l)):
                    if (abs(l[i] - l[j]) <= a and abs(l[j] - l[k]) <= b and abs(l[i] - l[k]) <= c):
                        ans += 1
                    else:
                        continue
        return ans
