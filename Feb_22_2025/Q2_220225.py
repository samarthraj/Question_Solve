def move_zeros(nums):

    pointer = 0

    for i in range(0, len(nums)): 
        if nums[i] != 0: 
            temp = nums[i] 
            nums[i] = nums[pointer] 
            nums[pointer] = temp 
            pointer += 1
        
    return nums

nums = [0,1,0,3,12]
ans = move_zeros(nums) 
print(ans) 
