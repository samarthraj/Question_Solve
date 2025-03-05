#sum between 2 indexes 

def sum_between(arr, i, j): 
    sum_j = 0
    sum_i = 0
    for k in range(0, j+1): 
        sum_j += arr[k] 
    
    for s in range(0, i):
        sum_i += arr[s] 

    return sum_j - sum_i

arr = [-2,0,3,-5,2,-1]
i, j = 2,5
ans = sum_between(arr, i, j) 
print(ans) 