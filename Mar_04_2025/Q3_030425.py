#flip a zero 
def flip_zero_for_max_ones(arr):

    start = 0
    end = 0
    ct_zeros = 0 
    ct_ones = 0 

    while end < len(arr) and start <= end: 
        if arr[end] == 0:
            ct_zeros += 1
        
        while ct_zeros == 2: 
            if arr[start] == 0: 
                ct_zeros -= 1 
            start += 1 
        
        ct_ones = max(ct_ones, end - start + 1) 
        end += 1
    
    return ct_ones

arr = [1,1,1,0,1,1,0,1,1,1,1]
ans = flip_zero_for_max_ones(arr)
print(ans) 