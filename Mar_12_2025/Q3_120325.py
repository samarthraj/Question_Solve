#wave array 
def sort_into_wave_array(arr): 

    for i in range(1, len(arr)-1, 2):
        if arr[i-1] < arr[i]:
            temp = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] = temp 
        
        if arr[i] > arr[i+1]:
            temp = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = temp  
        
    return arr

    
arr = [20,10,8,6,4,2] 
#[20,8,10,4,6,2]
ans = sort_into_wave_array(arr) 
print(ans) 