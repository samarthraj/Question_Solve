#left right sum difference 
def left_right_sum(arr): 

    left_sum = []
    right_sum = [] 
    answer = [0]*len(arr)

    for i in range(0, len(arr)): 
        if i - 1 < 0: 
            left_sum.append(0) 
        else: 
            left_sum.append(arr[i-1] + left_sum[i-1])  
    
    #print(left_sum)
    for j in range(0, len(arr)):
        sum = 0
        for k in range(j, len(arr)-1):
            sum += arr[k+1] 
        right_sum.append(sum) 

    #print(right_sum)

    for i in range(0, len(answer)): 
        answer[i] = abs(left_sum[i] - right_sum[i]) 
    return answer 

arr = [10,4,8,3]
#ans = [15,1,11,22] 
ans = left_right_sum(arr) 
print(ans)  


