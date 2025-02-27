#Q1 - check if array contains a sub arrays with sum K 
#Q1 - longest subarray with sum = k 
#Q2 - Total Number of subarrays with sum = k 

#SLIDING WINDOW
def check_subarray_k(arr, k): 
    sum = 0 
    start = 0
    ls = []
    for end in range(0, len(arr)): 
        sum += arr[end] 

        while sum > k and start <= end: #start <= end is written to make the window valid! 
            sum = sum - arr[start] 
            start += 1 
        
        if sum == k: 
            ls.append(arr[start:end+1]) 

    return ls

#arr = [15,2,4,8,9,5,10,23] 
#k = 23
# arr = [1, 2, 3, 7, 5]
# k = 12
arr = [10, 5, 7, 3, 4]
k = 7
ans = check_subarray_k(arr, k)
print(ans) 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def longest_subarray(arr, k ): 
    pass

arr = [10, 5, 7, 3, 4]
k = 7
ans = longest_subarray(arr, k) 
print(ans) 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def total_subarray_with_sum_k(arr, k): 
    pass

arr = [1,10,4,0,3,5] 
k = 7
ans = total_subarray_with_sum_k(arr, k)
print(ans) 


