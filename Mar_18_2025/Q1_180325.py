#gcd array 
def solve(arr): 

    min_num = min(arr) 
    max_num = max(arr) 
    gcd = 1 

    for i in range(min_num, 0, -1): 
        if min_num % i == 0 and max_num % i == 0: 
            return i
            
    return 1

#nums = [2,5,6,9,10] 
#nums = [12,24,64]
nums = [3,3]
ans = solve(nums) 
print(ans) 
