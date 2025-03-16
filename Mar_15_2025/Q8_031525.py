#selection sort 

def selection_sort(arr): 

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

arr = [3,5,1,6,-3,8] 
ans = selection_sort(arr) 
#print(ans) 


def bubble_sort(arr): 

    #you will swap adjacent elements 
    for i in range(0, len(arr)): 
        swapped = False 
        for j in range(0, len(arr)-i-1): 
            if arr[j+1] < arr[j]: 
                temp = arr[j] 
                arr[j] = arr[j+1] 
                arr[j+1] = temp 
                swapped = True 
        
        if swapped != True: 
            break 
    
    return arr
    
arr = [3,5,1,6,-3,8,-8] 
ans = bubble_sort(arr) 
#print(ans)

# def insertion_sort(arr): 

#     for i in range(1, len(arr)):
#         val = arr[i]
#         j = i - 1 

#         while j >= 0: 
#             if val < arr[i]:
#                 swap with next elemnt? 

def quick_sort(arr):

    if len(arr) <= 1: 
        return arr

    pivot = arr[len(arr)//2] 
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot] 
    right = [i for i in arr if i > pivot] 

    return quick_sort(left) + middle + quick_sort(right) 

arr = [3,5,1,6,-3,8,-8,-20] 
ans = quick_sort(arr) 
print(ans)


