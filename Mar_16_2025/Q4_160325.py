def solve(arr):

    new_arr = sorted(arr)
    ans_arr = [] 
    end = len(new_arr) - 1
    for start in range(0, len(new_arr)): 
        if new_arr[start]*(-1) == new_arr[end]: 
            if [new_arr[start],new_arr[end]] not in ans_arr: 
                ans_arr.append([new_arr[start],new_arr[end]]) 
        if new_arr[start]*(-1)  new_arr[end]
        start += 1
        end -= 1
    return ans_arr


arr = [6, 1, 8, 0, 4, -9, -1, 10, -6, -5]
ans = solve(arr)
print(ans)
