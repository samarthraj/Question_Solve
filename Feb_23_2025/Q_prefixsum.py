def prefix_sum(arr, start, end): 
    sum_end = 0
    sum_start = 0 
    for i in range(0, end+1): 
        sum_end += arr[i] 
    
    for j in range(0, start):
        sum_start += arr[j]
    
    return sum_end - sum_start

arr = [-2,0,3,-5,2,-1]
start = 2
end = 5
ans = prefix_sum(arr, start, end) 
print(ans) 
