def square_hollow(n): 
    
    for i in range(n):          
        for j in range(n):
            if i == 0 or i == (n-1):      
                print('*', end='')  
            elif j == 0 or j == (n-1): 
                print('*', end = ' '*(n-2)) 
        print() 

n = 4
ans = square_hollow(n)
print(ans) 