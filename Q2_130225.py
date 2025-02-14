#remove duplicates from the array
def remove_duplicates(nums): 

#    if not nums:
    #     return 0


    # index = 0
    # for i in range(1, len(nums)): 
    #     if nums[index] != nums[i]:
    #         index += 1
    #         nums[index] = nums[i] 
    
    # return index + 1

    index = 0
    for i in range(0, len(nums)): 
        if nums[index] != nums[i]: 
            index += 1
            nums[index] = nums[i] 
    
    return index + 1

nums = [1,2,3,4]  
ans = remove_duplicates(nums)
print(ans)
