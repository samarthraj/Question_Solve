#leader array -> any element that is greater in the right 
def leader_array(arr): 

    #start from right and move left 
    max_element = float('-inf') 
    leader_arr = []
    for i in range(len(arr)-1, -1, -1): 
        if arr[i] >= max_element: 
            max_element = arr[i] 
            leader_arr.append(max_element)  
    
    leader_arr.sort(reverse=True)
    return leader_arr


#arr = [16, 17, 4, 3, 5, 2] 
arr= [61, 61, 17]
#o/p = [17, 5, 2] 
ans = leader_array(arr) 
print(ans) 
