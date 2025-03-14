#wave_array - works only for sorted arrays, if unsorted, first sort it and then same logic 
def wave_array(arr): 
    
    for i in range(1, len(arr), 2): 
        if arr[i] > arr[i-1]: 
            temp = arr[i] 
            arr[i] = arr[i-1] 
            arr[i-1] = temp 
        
        # if arr[i+1] < arr[i]: 
        #     temp = arr[i] 
        #     arr[i] = arr[i+1] 
        #     arr[i+1] = temp 
        
    return arr 

arr = [1,2,3,4,5]
#arr = [2, 4, 7, 8, 9, 10]
#[20,8,10,4,6,2]
ans = wave_array(arr) 
print(ans) 