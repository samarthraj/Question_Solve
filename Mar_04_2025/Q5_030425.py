#Given an array find the subarray with the largest sum 

def subarray_with_largest_sum(arr): 

    ans = arr[0]
    current_sum = 0 

    for i in range(0, len(arr)): 
        current_sum += arr[i] 
        ans = max(ans, current_sum)

        if current_sum < 0: 
            current_sum = 0 
    
    return ans

arr = [-1]
#-3,4,-1,2,1,-5,4] 
ans = subarray_with_largest_sum(arr)
print(ans) 