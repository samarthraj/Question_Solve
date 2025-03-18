def solve(arr): 

    dict = {} 
    for i in range(0, len(arr)): 
        if arr[i] not in dict: 
            dict[arr[i]] = 1 
        else:  
            dict[arr[i]] += 1
    
    sorted_keys = sorted(dict, key=lambda x: -dict[x])

    result = []
    for key in sorted_keys:
        result.extend([key] * dict[key]) 
    return result

arr = [3,3,3,10,10,5,5,5,5,5] 
ans = solve(arr)
print(ans) 
