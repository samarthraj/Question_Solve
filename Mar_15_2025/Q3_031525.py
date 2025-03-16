def solve(n):
        prime_ls = [True] * (n+1) 
        max_prime = 0 

        for i in range(2, int(n**0.5)+1): 
            if prime_ls[i]: 
                for j in range(i*i, n+1, i):
                    prime_ls[j] = False 

        for k in range(2, len(prime_ls)):
            if prime_ls[k] and n % k == 0: 
                max_prime = max(max_prime, k)
        
        return max_prime

n = 6 
ans = solve(n) 
print(ans) 