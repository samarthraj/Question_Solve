def removeElement(nums, val):
    index = 0
    for i in range(0, len(nums)): 
        if nums[i] != val: 
            nums[index] = nums[i] 
            index += 1
    
    return nums[:index] 
        
nums = [0,1,2,2,3,0,4,2]
val = 2
ans = removeElement(nums, val)
print(ans)
