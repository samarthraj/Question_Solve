def right_triangle(n): 

    # for i in range(1,n+1):          
    #     for j in range(n-i): 
    #         print(' ', end = '') 
    #     for k in range(i):
    #         print('*', end = '')
    #     print()  

    for i in range(0,n+1):          
        for j in range(n-i): 
            print('*', end = '') 
        print() 
        for k in range(i,n):
            print(' ', end = '')
        



            

n = 5
ans = right_triangle(n)
print(ans) 