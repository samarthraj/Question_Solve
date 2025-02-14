#move zeros to the end
def remove_zeros(nums): 
    
    index = 0
    for i in range(0, len(nums)): 
        if nums[i] != 0: 
            temp = nums[index] 
            nums[index] = nums[i] 
            nums[i] = temp
            index += 1
    
    return nums
 
nums = [0]
ans = remove_zeros(nums)
print(ans)