def left_triangle(n): 

    for i in range(1,n+1):          
        for j in range(i, n+1):
            print('*', end='')  
        print()
             


n = 5
ans = left_triangle(n)
print(ans) 

