from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = []

        a = Counter(nums1)

        b = Counter(nums2)

        for i in a:
            if i in b:
                ans += [i]*min(a[i], b[i])
        return ans


# from collections import Counter

# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         def helper(a, b):
#             ans = []
#             mapp = Counter(b)
#             for i in a:
#                 if i in mapp and mapp[i] > 0:
#                     ans.append(i)
#                     mapp[i] -= 1
#             return ans
#         if len(nums1) > len(nums2):
#             return helper(nums1, nums2)
#         else:
#             return helper(nums2, nums1)
#             