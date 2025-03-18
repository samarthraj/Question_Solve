def selection_sort(arr): 
    #select min element and move it to the first and then keep selecting 
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
    #select adjacent elements

    for i in range(0, len(arr)): #highest is swapped and put at the end thats why i will be subtracted
        swapped = False
        for j in range(0, len(arr)-1-i): #leaves the swapped and last one and up until there the loop occurs
            if arr[j+1] < arr[j]: 
                temp = arr[j]
                arr[j] = arr[j+1] 
                arr[j+1] = temp 
                swapped = True
        
        if swapped != True: 
            break
    
    return arr

def merge_sort(arr): 
    if len(arr) > 1: 
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:] 

        merge_sort(left_arr)
        merge_sort(right_arr) 

        i, j, k = 0, 0, 0 

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

#arr = [0,1,7,0,9,-9,100] 
#arr1 = [0,1,7,0,9,-9,100,-2] 
arr2 = [1,3,5,10,2,6,8,9]
#ans = selection_sort(arr)
#ans1 = bubble_sort(arr1)
ans2 = merge_sort(arr2) 
#print(ans) 
#print(ans1)
print(ans2)

