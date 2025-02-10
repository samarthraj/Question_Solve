def getSecondLargest(arr): 
    max_number = float('-inf')
    second_max_number = float('-inf')
    if len(arr) > 1: 
        for i in range(0, len(arr)): 
            if arr[i] > max_number: 
                second_max_number = max_number
                max_number = arr[i] 
            
            if arr[i] > second_max_number and arr[i] != max_number:
                second_max_number = arr[i] 

        if max_number == float('-inf') or second_max_number == float('-inf'): 
            return -1
        else: 
            return second_max_number
    else: 
        return -1
    

arr = [10, 5, 4, 6, 3, 10]
arr2 = [10,5,10] 
arr3 = [10,10,10]
arr4 = []
arr5 = [20]
ans = getSecondLargest(arr5)
print(ans)