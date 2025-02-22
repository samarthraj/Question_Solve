#1752. Check if Array Is Sorted and Rotated 
#Intuition is to check the drop in the number of counts 
#if an array is rotated originally, its drop will be <= 1 
def check(nums):

    drop = 0 
    n = len(nums) 
    for i in range(0, len(nums)-1): 
        if nums[i+1] < nums[i]: 
            drop += 1 

    if nums[n-1] > nums[0]: 
        drop += 1

    if drop > 1: 
        return False 
    return True

nums = [3,2,1]
ans = check(nums)
print(ans) 
