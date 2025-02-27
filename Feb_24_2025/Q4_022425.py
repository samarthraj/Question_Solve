#print all prime numbers from 1 to 100 
#Sieve of Eratosthenes  
def prime_factors_upto_n(n): 
    #Mark all as Prime first
    vector = [True] * (n+1)

    for i in range(2, int(n**0.5)+1): 
        if vector[i]: 
            for j in range(i*i, n+1, i): 
                vector[j] = False
    
    for i in range(2, len(vector)): 
        if vector[i]: 
            print(i, end = ' ') 


n = 20 
ans = prime_factors_upto_n(n) 
print(ans) 

