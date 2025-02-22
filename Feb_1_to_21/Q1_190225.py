#Given an integer n, return any array containing n unique integers such that they add up to 0.

def solve(n): 
    arr = [] 
    
    if n % 2 != 0: 
        arr.append(0) 
    
    for i in range(1, n//2 + 1): 
        arr.append(-i)
        arr.append(i)
    
    return arr


n = 5
#ans = [-7,-1,1,3,4] 
ans = solve(n) 
print(ans) 

