def merge_two_arrys(arr1, arr2): 

    i,j = len(arr1)-1,0 

    while i < len(arr1) and j < len(arr2): 
        if arr1[i] < arr2[j]:
            temp = arr1[i] 
            arr1[i] = arr2[j] 
            arr2[j] = temp  
            i -= 1
            j += 1
        elif arr2[j] > arr1[i]:  
            break
    
    while i < len(arr1): 
        arr1[k] = arr1[i] 
        i += 1
        k += 1
    
    while j < len(arr2): 
        arr2[k] = arr2[j] 
        j += 1
        k += 1
    
    print(arr1)
    print(arr2) 

arr1 = [2,4,7,10] 
arr2 = [2,3] 
ans = merge_two_arrys(arr1, arr2) 
print(ans) 
