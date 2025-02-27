#find the missing number 
#using xor 
#using not in 
def missing_number(n): 

    # for i in range(0, len(n)): 
    #     if i not in n: 
    #         return i
    xor = len(n)

    for i in range(0, len(n)): 
        xor = xor ^ i ^ n[i] 
    
    return xor


n = [3,0,1] 
#ans  = 8 
ans = missing_number(n)
print(ans) 
