#Q1 - check if array contains a sub arrays with sum K 
#Q1 - longest subarray with sum = k 
#Q2 - Total Number of subarrays with sum = k 

#SLIDING WINDOW
def check_subarray_k(arr, k): 

    #the concept of this is a sliding window 
    start = 0
    sum = 0
    ls = [] 
    for end in range(0, len(arr)): 
        sum += arr[end] 

        while sum > k and start <= end:
            sum = sum - arr[start] 
            start += 1
    
        if sum == k: 
            ls.append(arr[start:end+1]) 
    
    return ls

#arr = [15,2,4,8,9,5,10,23] 
#k = 23
# arr = [1, 2, 3, 7, 5]
# k = 12
# arr = [10, 5, 7, 3, 4]
# k = 7
arr = [10, 5, 2, 7, 1, -10]
k = 15 
ans = check_subarray_k(arr, k)
#print(ans) 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#only positive 
def longest_subarray(arr, k ): 
    
    start = 0
    sum = 0
    max_arr = 0
    for end in range(0, len(arr)): 
        sum += arr[end] 

        while sum > k and start <= end: 
            sum -= arr[start] 
            start += 1
        
        if sum == k: 
            length = len(arr[start:end+1])
            max_arr = max(max_arr, length)
        
    return max_arr


arr = [10, 5, 2, 7, 1, 10]
k = 15
ans = longest_subarray(arr, k) 
#print(ans) 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#if there are negative values in the array it will not work 
def total_subarray_with_sum_k(arr, k): 
    
    start = 0
    sum = 0
    ct = 0
    for end in range(0, len(arr)): 
        sum += arr[end]

        while sum > k and start <= end: 
            sum -= arr[start]
            start += 1
        
        if sum == k: 
            ct += 1
    
    return ct 

# arr = [1,10,4,0,3,5] 
# k = 7
arr = [10, 5, 2, 7, 1, -10]
k = 15
ans = total_subarray_with_sum_k(arr, k)
print(ans) 


