# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

def find_max_sum_of_sub_array(arr, k): 

    #sliding window coz of subarrays 
    start = 0 
    sum = 0
    max_sum = float('-inf')
    ls = []
    seen = ()
    for end in range(0, len(arr)): 
            seen.add(arr[end]) 
            sum += arr[end] 

            while end - start + 1 == k and start <= end:
                ls.append(sum)
                max_sum = max(max_sum, sum) 
                sum -= arr[start]
                start += 1
    
    if max_sum == float('-inf'): 
        return 0
    else:
        return max_sum

#arr = [4,4,4]
#arr = [1,5,4,2,9,9,9]
arr = [1,1,1,7,8,9]
#size of window 
k = 3
ans = find_max_sum_of_sub_array(arr, k) 
print(ans) 


