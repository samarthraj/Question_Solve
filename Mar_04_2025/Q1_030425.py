def array_of_sqs(arr): 
    new_arr = [] 

    for i in range(0, len(arr)): 
        new_arr.append(arr[i]**2) 
    
    new_arr.sort()
        
    return new_arr        

arr =  [-4,-1,0,3,10]
ans = array_of_sqs(arr) 
print(ans) 
