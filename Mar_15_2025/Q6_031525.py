#76. Difference Between Element Sum and Digit Sum of an Array
def solve(nums):

    element_sum = 0 
    digit_sum = 0

    for i in range(0, len(nums)): 
        element_sum += nums[i] 
        while nums[i] >= 1: 
            last_digit = nums[i] % 10 
            nums[i] = nums[i] // 10
            digit_sum += last_digit

    return abs(element_sum - digit_sum) 

#nums = [1,15,6,3] 
nums =  [1,2,3,4]
ans = solve(nums) 
print(ans) 
