# 1150

def isMajorityElement(nums: List[int], target: int) -> bool:
    a = {}
    
    for i in nums:
        a[i] = a.get(i, 0) + 1
    return target in nums and a[target] > len(nums) // 2

print(isMajorityElement([2,4,5,5,5,5,5,6,6], 5))
print(isMajorityElement([10,100,101,101], 101))
