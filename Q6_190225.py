#268. Missing Number 
def missingNumber(nums):

    n = len(nums) 

    for i in range(0, n+1): 
        if i not in nums: 
            return i

nums = [3,0,1] 
ans = missingNumber(nums) 
print(ans) 