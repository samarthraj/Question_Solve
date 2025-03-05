#intersection of two arrays 
def intersection(arr1, arr2): 

    pointer1 = 0
    pointer2 = 0 
    ans_arr = []

    arr1.sort()
    arr2.sort() 

    while pointer1 < len(arr1) and pointer2 < len(arr2): 
        
        if arr1[pointer1] == arr2[pointer2]: 
            ans_arr.append(arr1[pointer1]) 
            pointer1 += 1
            pointer2 += 1

        elif arr1[pointer1] < arr2[pointer2]: 
            pointer1 += 1

        elif arr1[pointer1] > arr2[pointer2]: 
            pointer2 += 1
    
    return ans_arr

arr1 = [2,2,0,3,3,3] 
arr2 = [1,1,2,3,3,4,5,5]
ans = intersection(arr1, arr2) 
print(ans) 
