#Given a number n check if its a perfect number or not 
#if its factors sum is == the number itself then its a perfect no without the number n
import math
def perfect_number(n): 
    sum = 0
    for i in range(1, int(n**(1/2))+1): 
        if n % i == 0: 
            sum += i 
            if n//i != n: 
                sum += (n//i)
    
    print(sum)
    return True if n == sum else False 


n = 28
ans = perfect_number(n) 
print(ans) 



