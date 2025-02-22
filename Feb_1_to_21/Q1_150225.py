#

def remove_duplicates(nums): 

    pointer = 0
    for i in range(0, len(nums)): 
        if nums[pointer] != nums[i]: 
            pointer += 1
            nums[pointer] = nums[i]

    return nums[:pointer+1]
        
nums = [1,2,2,3,3,4,4]  
ans = remove_duplicates(nums)
print(ans)


def removeElement(nums, val):

    index = 0
    for i in range(0, len(nums)): 
        if nums[i] != val: 
            temp = nums[index]
            nums[index] = nums[i] 
            nums[i] = temp 
            index += 1
    
    return nums[:index]

nums = [0,1,2,2,3,0,4,2]
val = 2
ans = removeElement(nums, val)
print(ans)


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
#nums = [0,0,1,2,0,3,12] 
ans = remove_zeros(nums)
print(ans)