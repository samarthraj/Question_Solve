#Rotate an array 
def rotate(nums, k): 
    if k > len(nums): 
        if k % 2 == 0: 
            k = len(nums) // 2
        elif k % 2 != 0: 
            k = len(nums)//2 + 1 

# nums = [1,2,3,4,5,6,7]
# k = 3

# nums = [-1,-100,3,99]
# k = 2

nums = [1,2,3] 
k = 4
ans = rotate(nums,k) 
print(ans) 


