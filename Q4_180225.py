#
def solve(arr):
    i = 0
    j = 0
    max_index = 0

    for k in range(0, len(arr)): 
        if arr[k] > i: 
            j = i
            i = arr[k]
            max_index = k
        if j <= i and arr[k] > j and max_index != k: 
            j = arr[k]
                
    return (i-1)*(j-1)


nums =  [1,5,4,5]
ans = solve(nums) 
print(ans) 

