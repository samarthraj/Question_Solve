#leader array -> any element that is greater in the right 
def leader_array(arr): 
    # ans_arr = [] 
    # for i in range(0, len(arr)): 
    #     for j in range(i, len(arr)): 
    #         if arr[j] > arr[i]: 
    #             ans_arr.append(arr[j]) 
    
    # #return ans_arr
    ans_arr = [] 
    i = 0
    while i < len(arr)-1: 
        for j in range(0, len(arr)): 
            if arr[j] > arr[i]: 
                ans_arr.append(arr[j]) 
                i = j 
                
        
    
    return ans_arr

arr = [16, 17, 4, 3, 5, 2] 
#o/p = [17, 5, 2] 
ans = leader_array(arr) 
print(ans) 
