def selection_sort(arr): 
    #here you select the max number and put it in its position 
    for i in range(0, len(arr)): 
        min_index = i 
        for j in range(i+1, len(arr)): 
            if arr[j] < arr[min_index]: 
                min_index = j 
        
        if min_index != i: 
            temp = arr[i] 
            arr[i] = arr[min_index] 
            arr[min_index] = temp 
        
    return arr


def bubble_sort(arr): 
    #here you compare the adjacent ones and swap 
    for i in range(0, len(arr)): 
        swapped = False
        for j in range(0, len(arr)-1-i): 
            if arr[j+1] < arr[j]: 
                temp = arr[j] 
                arr[j] = arr[j+1] 
                arr[j+1] = temp 
                swapped = True 
        if swapped != True: 
            break 
    return arr


def merge_sort(arr): 
    #you break and merge 
    if len(arr) > 2: 
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:] 

        merge_sort(left_arr)
        merge_sort(right_arr) 

        i,j,k = 0, 0, 0

        while i < len(left_arr) and j < len(right_arr): 
            if left_arr[i] < right_arr[j]: 
                arr[k] = left_arr[i] 
                i += 1
                k += 1
            else: 
                arr[k] = right_arr[j]
                j += 1
                k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr): 
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
    return arr

arr = [0,1,7,0,9,-9,100] 
arr1 = [0,1,7,0,9,-9,100]
arr2 = [0,1,7,0,9,-9,100]
ans = selection_sort(arr)
ans1 = bubble_sort(arr1)
ans2 = merge_sort(arr2) 
print(ans) 
print(ans1)
print(ans2)

