#Largest Prime number in a range 

def largest_prime_number(n): 

    vector = [True]*(n+1) 
    temp = 0
    for i in range(2, int(n**0.5)+1): 
        if vector[i]: 
            for j in range(i*i, n+1, i): 
                vector[j] = False 
    
    for k in range(2, len(vector)): 
        if vector[k]: 
            temp = k 
    
    return temp 

n = 50 
ans = largest_prime_number(n)
print(ans) 

