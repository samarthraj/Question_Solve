#solve problems from previous weeks (Sundays) 23rd Feb
#intersection of arrays 
def intersection(arr1, arr2): 
    ls = [] 
    arr1.sort()
    arr2.sort() 
    arr1_p = 0
    arr2_p = 0 

    while arr1_p < len(arr1) and arr2_p < len(arr2): 

        if arr1[arr1_p] == arr2[arr2_p]: 
            ls.append(arr1[arr1_p]) 
            #ans_set.add(arr1[arr1_p])
            arr1_p += 1
            arr2_p += 1
        elif arr1[arr1_p] < arr2[arr2_p]:
            arr1_p += 1
        elif arr1[arr1_p] > arr2[arr2_p]:
            arr2_p += 1
    
    return ls

arr1 = [1,1,2,3,4,6,2] 
# 1,1,2,2,3,4,6
# 1,1,2,5,7,7 
arr2 = [5,7,2,1,1,7] 
ans = intersection(arr1, arr2) 
print(ans) 

