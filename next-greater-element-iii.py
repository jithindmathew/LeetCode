MAX_INT = 2**31 - 1


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))

        index = -1

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                index = i - 1
                for j in range(len(nums) - 1, 0, -1):
                    if nums[j] > nums[index]:
                        nums[j], nums[index] = nums[index], nums[j]
                        break
                l, r = index + 1, len(nums) - 1

                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                break
        else:
            return -1

        ans = int(''.join(nums))

        return ans if ans <= MAX_INT else -1
