#given an array of binary of 0s and 1s 
def max_ones(nums):
    count = 0 
    max_count = 0
    for i in range(0, len(nums)): 
        if nums[i] == 1: 
            count+= 1
            max_count = max(max_count, count) 
        else: 
            count = 0
    
    return max_count

nums = [1,1,1,2,0,1,1,1]
ans = max_ones(nums)
print(ans) 
