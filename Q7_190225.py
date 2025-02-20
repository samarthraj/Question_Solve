#485. Max Consecutive Ones 
def findMaxConsecutiveOnes(nums):
    ls = []
    pointer = 0
    for i in range(0, len(nums)): 
        ct = 0
        if nums[i] != 1: 
            ct = len(nums[pointer:i])
            ls.append(ct)
            pointer = i + 1       

    ct = len(nums[pointer:])
    ls.append(ct)

    return max(ls)

nums = [1,0,1,1,0,1]
ans = findMaxConsecutiveOnes(nums) 
print(ans) 