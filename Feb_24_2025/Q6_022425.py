def largest_prime_factor(n):
    max_prime = -1
    while n % 2 == 0: 
        n = n // 2  
        max_prime = 2
        
    
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0: 
            n = n // i 
            max_prime = max(max_prime, i) 
    
    if n > 1: 
        return n 
    else: 
        return max_prime

n = 5
ans = largest_prime_factor(n) 
print(ans)