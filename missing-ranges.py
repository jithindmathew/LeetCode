# 163

def findMissingRanges(nums, lower, upper):
    ans = []
    
    i = 0
    
    st = lower
    end = upper
    
    while i < len(nums):
        if nums[i] > st:
            if nums[i] - st >= 2:
                ans.append("{}->{}".format(st, nums[i] - 1))
            else:
                ans.append("{}".format(st))
            st = nums[i] + 1
        
        elif nums[i] == st:
            st = nums[i] + 1
            continue
        
        i += 1
    if upper - nums[-1] >= 2:
        ans.append("{}->{}".format(nums[-1] + 1, upper))
    elif upper - nums[-1] == 1:
        ans.append("{}".format(upper))
    return ans
    
print(findMissingRanges([0, 3, 8, 20, 97], 0, 999))
