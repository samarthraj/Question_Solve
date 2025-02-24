#two pointer with non fixed k or not fixed numbers of sliding window, finding sum = some number k
def solve(arr, k_sum): 

    start = 0
    last = 0 
    sum = 0 

    while last < len(arr): 
        sum += arr[last] 
        if sum == k_sum: 
            while sum > k







arr = [-5, 8, -14, 2, 4, 12]
k_sum = -5 
ans = solve(arr, k_sum)
print(ans) 