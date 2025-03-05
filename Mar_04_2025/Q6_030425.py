def find_max_sum_of_sub_array(arr, k): 

    start = 0
    sum = 0 
    max_sum = 0

    for end in range(0, len(arr)): 
        sum += arr[end] 

        while end - start + 1 == k: 
            max_sum = max(sum, max_sum)
            sum -= arr[start]
            start += 1
    
    return max_sum

arr = [1,5,4,2,9,9,9,1]
#size of window 
k = 3 
ans = find_max_sum_of_sub_array(arr, k) 
print(ans) 