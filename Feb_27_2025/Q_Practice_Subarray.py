#For subarrays concept we can use a sliding window 
#sub arrays with positive arrays or arr[i] > 0 

#longest subarray with sum = k 
def longest_sub_array(arr,k): 
    
    #end pointer dont need since we are using a loop 
    #we can just use a starting pointer 
    start = 0 
    sum = 0 
    ls = []
    for end in range(0, len(arr)): 
        sum += arr[end] 

        while sum > k and start <= end:
            sum -= arr[start] 
            start += 1
        
        if sum == k: 
            ls.append(arr[start:end+1]) 
    
    return ls

arr = [15,2,4,8,9,5,10,23] 
k = 23 
ans = longest_sub_array(arr, k) 
print(ans)