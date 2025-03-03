#happy number 

def happy_number(n):
    #while n != 1: 
    result = 0
    while n > 0: 
        result = result + (n % 10)**2 
        n = n // 10 

    if result == 1: 
        return True
    happy_number(result)


n = 19 
ans = happy_number(n)
print(ans) 
