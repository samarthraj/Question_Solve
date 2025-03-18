#pivot interger 
def pivot_interger(n): 
    pivot_x = n // 2
    i = 0 

    if n <= 1: 
        return 1

    while i < n:  
        sum_x_to_n = 0
        sum_to_x = 0

        for j in range(0, pivot_x+1): 
            sum_to_x += j
        
        for k in range(pivot_x, n+1): 
            sum_x_to_n += k 
        
        if sum_to_x == sum_x_to_n: 
            return pivot_x 
        elif sum_to_x < sum_x_to_n:
            pivot_x += 1 
        elif sum_to_x > sum_x_to_n:
            pivot_x -= 1 
        i += 1

    return -1

n = 1 
ans = pivot_interger(n) 
print(ans) 
