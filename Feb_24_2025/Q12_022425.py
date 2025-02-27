#max consecutive ones 

def ones(arr): 
#sol 1 
    ct = 0 
    max_ct = 0
    for i in range(0, len(arr)): 
        if arr[i] != 1: 
            ct = 0 
        elif arr[i] == 1: 
            ct += 1 
            max_ct = max(ct, max_ct) 
    
    return max_ct 
#other sol is using pointers 
arr = [0,1,1,1,0,1,1,0,0,1,1,1,1,0,1]
ans = ones(arr) 
print(ans) 