#26. Remove Duplicates from Sorted Array 
def removeDuplicates(nums): 

    pointer = 0
    for i in range(0, len(nums)): 
        if nums[i] != nums[pointer]: 
            pointer += 1
            nums[pointer] = nums[i]
    
    
    return len(nums[:pointer+1]) 
            
    

nums = [0,0,1,1,1,2,2,3,3,4]
ans = removeDuplicates(nums)
print(ans) 