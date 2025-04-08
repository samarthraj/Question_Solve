def running_sum(arr):

    ans = [] 
    sum = 0 

    for i in range(0, len(arr)): 
        sum += arr[i] 
        ans.append(sum) 
    
    return ans

arr = [1,1,1,1,1]
ans = running_sum(arr)
print(ans)
