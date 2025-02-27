#practice all previous 

def largest_prime_factor(n): 

    max_prime = 0 
    while n % 2 == 0: 
        n = n // 2 
        max_prime = 2 
    
    for i in range(3, int(n**0.5)+1, 2): 
        if n % i == 0: 
            n = n // i 
            max_prime = max(max_prime, i) 
    
    if n > 1: 
        max_prime = n 

    return max_prime

n = 26
ans = largest_prime_factor(n)
print(ans) 




