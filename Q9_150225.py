# #divisible by 11 
# n = 76945 
# Given an array every number appears twice 
# but one number appears once 

def func(arr): 
    ans = 0
    for i in range(0, len(arr)): 
        ans = ans ^ arr[i] 
    
    return ans

arr = [2,3,5,4,5,3,4]
ans = func(arr)
print(ans) 

#find the largest prime factor of that number 

