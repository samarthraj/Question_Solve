#Rotate an array 
def rotate(nums, k): 
    if k > len(nums): 
        k = len(nums) // k 
    
    for i in range(0, len(nums)): 
        if i == k: 
            arr1 = nums[:k+1] 
            arr2 = nums[k+1:] 
            
    for i in range (0, len(arr1)): 
        

             




#7,6,5,4,3,2,1
#5,6,7,1,2,3,4


nums = [1,2,3,4,5,6,7] 
k = 3 
ans = rotate(nums,k) 
print(ans) 


