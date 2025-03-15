#simple modification on if you are at i, after how many indexes the leader exists
#leader array -> any element that is greater in the right 
def leader_array(arr): 

    #start from right and move left 
    max_element = float('-inf') 
    max_element_index = 0
    index_arr = []
    #index_dict = {}
    for i in range(len(arr)-1, -1, -1): 
        if arr[i] >= max_element: 
            max_element = arr[i] 
            max_element_index = i
            index_arr.append(0)
            #index_dict[i] = 0 
            #index_dict[arr[i]] = 0
        else: 
            index_arr.append(max_element_index - i)
            #index_dict[i] = max_element_index - i 
            #index_dict[arr[i]] =  max_element_index - i 
    index_arr.reverse()
    return index_arr

arr = [16, 17, 4, 3, 5, 2] 
#arr= [61, 61, 17]
#o/p = [17, 5, 2] 
ans = leader_array(arr) 
print(ans) 
