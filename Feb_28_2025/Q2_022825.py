#Find the max ones such that you can flip at max one 0 to 1 in a binary array 
# Sliding Window Concept 
def max_ones(arr):

    start_pointer = 0
    end_pointer = 0
    ct = 0 
    ct_first_zero = 0 
    max_ct = 0

    while end_pointer < len(arr) and start_pointer <= end_pointer:  
        if arr[end_pointer] != 0: 
            ct += 1
            end_pointer += 1
            max_ct = max(ct, max_ct)
        elif ct_first_zero < 1 and arr[end_pointer] == 0: 
            arr[end_pointer] = 1
            ct_first_zero += 1
            start_pointer = end_pointer 
        else: 
            ct = 0
            end_pointer += 1
            start_pointer = end_pointer
    
    return max_ct


arr = [1,1,1,0,1,0,0,1,1,1] 
ans = max_ones(arr)
print(ans) 