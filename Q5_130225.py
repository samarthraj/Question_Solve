def sortColors(nums):
    #use three pointers is what it says 
    low = 0 
    high = len(nums) - 1
    mid = (low + high) // 2

    for i in range(0, len(nums)): 
        if nums[i] != 0: 
            low += 1 
        elif nums[i] == 0: 
            temp = nums[low]
            nums[low] = nums[i] 
            nums[i] = temp 



       











nums = [2,0,2,1,1,0]
ans = sortColors(nums) 
print(ans)