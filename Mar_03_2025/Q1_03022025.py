#Given an array [20,10,8,6,4,2] 
#output [20,8,10,4,6,2] 
#Wave array 
#one element is greater and one is less 
#first try for sorted array 
#then try for unsorted array 
# arr[i-1] >= arr[i] <= arr[i+1] condition 
#  

def wave_array(arr):

    for i in range(1, len(arr)-1, 2): 
        if arr[i-1] < arr[i]: 
            temp = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] = temp 
        
        if arr[i] > arr[i+1]: 
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp 
        
    return arr

arr = [20,10,8,6,4,2]
ans = wave_array(arr)
print(ans) 
