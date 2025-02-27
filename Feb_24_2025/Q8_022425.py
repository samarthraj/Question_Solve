#Check if Array Is Sorted and Rotated 
#Intuition is to check the drop in the number of counts 
#if an array is rotated originally, its drop will be <= 1 

def check(nums): 
    
    #check for a dip and count if the dip is more than one then its False 
    #check edge cases 
    ct_dips = 0 
    pointer = 0
    for i in range(0, len(nums)-1): 
        if nums[i+1] < nums[i]: 
            ct_dips += 1 
    
    if nums[-1] > nums[0]: 
        ct_dips += 1
    
    if ct_dips > 1: 
        return False 
    else: 
        return True 


nums = [2,1,3,4]
ans = check(nums) 
print(ans) 
