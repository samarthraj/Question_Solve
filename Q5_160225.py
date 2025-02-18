#triangle and ulta triangle
def triangle(n): 
    
    for i in range(n):          
        for j in range(i): 
            print(' ', end = '') 
        #print() 
        for k in range(2*(n-i)-1):
            print('*', end = '')
        print()


n = 4
ans = triangle(n)
print(ans) 