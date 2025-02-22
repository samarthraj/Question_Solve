def print_fibonacci(n):
    a = 0
    b = 1

    for i in range(0, n): 
        print(a, end = " ")
        temp = b 
        b = a + b 
        a = temp  

# 0 1 1 2 3 5 ....
n = 5
ans = print_fibonacci(n) 
print(ans)
