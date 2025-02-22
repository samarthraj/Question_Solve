#find length of longest subarray with sum k 
#this logic gives a time out error since there are two loops and time c is O(N**2) 
def longestSubarray(arr, k): 
    # max_numb = 0
    # for i in range(0, len(arr)): 
    #     sum = 0
    #     for j in range(i, len(arr)): 
    #         sum += arr[j] 
    #         if sum == k: 
    #             max_numb = max(max_numb, len(arr[i:j+1]))

    # return max_numb
    sum = 0
    hashmap = {} 
    max_length_subarray = 0 
    for i in range(0, len(arr)): 
        sum += arr[i] 

        if sum == k: 
            max_length_subarray = i + 1 
        
        if sum not in hashmap: 
            hashmap[sum] = i 
        
        if (sum - k) in hashmap: 
            max_length_subarray = max(max_length_subarray, i - hashmap[sum-k])
            
    return max_length_subarray
        
arr = [-5, 8, -14, 2, 4, 12]
k = -5
# arr = [10, 5, 2, 7, 1, -10]
# k = 15
ans = longestSubarray(arr,k) 
print(ans)