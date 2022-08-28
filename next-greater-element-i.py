class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         temp = {i: -1 for i in nums2}
        
#         for i in range(0, len(nums2), 1):
#             if nums2[i] not in temp:
#                 continue
#             for j in range(i + 1, len(nums2), 1):
#                 if nums2[j] > nums2[i]:
#                     next_greater = nums2[j]
#                     temp[nums2[i]] = next_greater
#                     break
                    
#         for i in range(len(nums1)):
#             nums1[i] = temp[nums1[i]]
#         return nums1
        temp = {n:i for i, n in enumerate(nums1)}
        res = [-1]*len(nums1)
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = temp[val]
                res[idx] = cur
            if cur in temp:
                stack.append(cur)
        return res
                