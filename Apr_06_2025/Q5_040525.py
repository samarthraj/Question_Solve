# shuffle array
def solve(arr):

    x_arr = arr[:len(arr)//2] 
    y_arr = arr[len(arr)//2:] 
    ans_arr = [] 
    i = 0 

    while i < len(x_arr):  
        ans_arr.append(x_arr[i]) 
        ans_arr.append(y_arr[i])  
        i += 1

    return ans_arr

arr = [2, 5, 1, 3, 4, 7]
ans = solve(arr)
print(ans)
