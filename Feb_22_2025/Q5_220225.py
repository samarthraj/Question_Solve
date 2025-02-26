#sub all the nos of sub arrays  
#sliding window or two pointers both are same 
def find_max_sub_array(arr,k): 

    # pointer_1 = 0 
    # pointer_2 = 0 

    # for i in range(0, len(arr)): 
    #     if arr[pointer_1] + arr[pointer_2] < k: 
    #         pointer_2 += 1
    #     elif arr[pointer_1] + arr[pointer_2] > k: 
    #         pointer_2 -= 1
            


arr = [1,10,4,0,3,5] 
k = 7
ans = find_max_sub_array(arr,k) 
print(ans) 
