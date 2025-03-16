def largest_element(arr, k): 

    arr.sort(reverse=True)
    return arr[k] 


arr = [3,2,1,5,6,4] 
k = 2 
ans = largest_element(arr,k) 
print(ans) 

