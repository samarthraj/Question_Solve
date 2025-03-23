#arr of integers given 
#return total number of 
#subarrays such that 
#their sum = k 


def solve(arr, k):  
    
    dict = {0:1} 
    sum = 0 
    ct = 0 
    for i in range(0, len(arr)): 
        sum += arr[i]

        if sum - k in dict: 
            ct += dict[sum-k] 
        
        

arr = [1,-1,0,1]
k = 0 
ans = solve(arr, k) 
print(ans) 


