def prime_factors(n): 
    prime_factor_ls = []
    while n % 2 == 0: #O(log N) 
        n = n // 2
        prime_factor_ls.append(2)
        print(2)

    for i in range(3, int(n**(1/2)) + 1, 2): #O(root N)
        while n % i == 0: #O(log N) 
            n = n // i 
            prime_factor_ls.append(i)
            print(i)
    
    if n > 1: 
        prime_factor_ls.append(n) 
        print(n)
        
    return prime_factor_ls
    

n = 10
ans = prime_factors(n)
print(ans)