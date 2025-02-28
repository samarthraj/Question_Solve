#Given an array of integers and a number K, 
#find the maximum sum of any contiguous subarray of size K 

def find_max_sum_of_sub_array(arr, k): 

    #sliding window coz of subarrays 
    start = 0 
    sum = 0
    max_sum = float('-inf')
    #ls = []
    for end in range(0, len(arr)): 
        sum += arr[end] 

        #len(arr[start:end+1]) == k --> inefficient 
        #use end - start + 1 

        #use while loop only when we compare < or > but when == comparison using an if makes sense
        #while end - start + 1 == k and start <= end: 
        if end - start + 1 == k: 
            max_sum = max(max_sum, sum) 
            sum -= arr[start]
            start += 1
    
    return max_sum

arr = [1,5,4,2,9,9]
#size of window 
k = 3 
ans = find_max_sum_of_sub_array(arr, k) 
print(ans) 


