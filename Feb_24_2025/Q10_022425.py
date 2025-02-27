#longest sub array 

def missing_number_in_ap(arr): 

    diff = (arr[-1] - arr[0]) // len(arr) 

    for i in range(0, len(arr)-1): 
        if arr[i+1] - arr[i] != diff: 
            return arr[i+1] - diff 


arr = [1, 6, 11, 16, 21, 31]
#6
ans = missing_number_in_ap(arr) 
print(ans) 


