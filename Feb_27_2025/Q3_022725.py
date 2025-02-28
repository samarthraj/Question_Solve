#Find Minimum sum of any contiguous subarray of size K 

def find_min_sum_of_sub_array(arr, k): 

    start = 0 
    sum = 0
    min_sum = float('inf')
    ls = []
    for end in range(0, len(arr)): 
        sum += arr[end] 

        if end - start + 1 == k: 
            ls.append(sum)
            min_sum = min(min_sum, sum) 
            sum -= arr[start]
            start += 1
    
    print(ls)
    return min_sum

#arr = [1,5,4,2,9,9]
arr = [-1,-1,-1,-1,-1,-1]
#size of window 
k = 3 
ans = find_min_sum_of_sub_array(arr, k) 
print(ans) 


