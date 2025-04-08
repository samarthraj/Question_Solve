def solve(arr):

    start = 0
    end = len(arr) - 1
    
    while start < len(arr) and start <= end: 
        temp = arr[start] 
        arr[start] = arr[end] 
        arr[end] = temp 
        start += 1
        end -= 1 
    
    return arr
  
arr = [1, 2, 3, 4, 5, 6]
ans = solve(arr)
print(ans)
