#find the single number in the list 
def singleNumber(nums):

    xor = 0 
    for i in range(0, len(nums)): 
        xor = xor ^ nums[i] 
    return xor 

nums = [4,1,2,1,2]
ans = singleNumber(nums)
print(ans)
