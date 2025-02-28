#Find avg of any contiguous subarray of size K 

def find_avg_of_sub_array(arr, k): 

    start = 0 
    sum = 0
    avg_ls = []
    for end in range(0, len(arr)): 
        sum += arr[end] 

        if end - start + 1 == k: 
            avg_ls.append(sum/k)
            sum -= arr[start]
            start += 1
    
    return avg_ls

arr = [1,5,4,2,9,9]
#arr = [-1,-1,-1,-1,-1,-1]
#size of window 
k = 3 
ans = find_avg_of_sub_array(arr, k) 
print(ans) 


