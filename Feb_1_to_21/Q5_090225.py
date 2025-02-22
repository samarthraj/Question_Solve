#given a number ex: a**3 + b**3 = n 
# Given a number n find all a and b such that a**3 + b **3 = n 
# n = 9; 1**3 + 2**3 = 9 --> (a + b)(a^2 - ab + b^2) 

def pairs(n): 
    pairs = []
    #(a + b)(a^2 - ab + b^2) = a^3 + b^3 
    limit = int(abs(n) ** (1/3)) + 1

    for a in range(-limit, limit + 1): #O(N**(1/3))
        for b in range(-limit, limit + 1): #O(N**(1/3))
            if a**3 + b**3 == n: 
                pairs.append((a,b)) 
    
    return pairs

#n = 28 
n = 1729 
ans = pairs(n)
print(ans) 


def cube_pairs(n): 
    limit = int(n ** (1/3)) + 1  # Cube root limit for positive values
    
    for i in range(1, limit):
        a = i ** 3
        diff = n - a
        
        # Check if diff is a perfect cube
        cb = round(diff ** (1/3))
        
        if cb ** 3 == diff:
            print(f"{i}^3 + {cb}^3 = {n}", end = " || ")


#n = 28 
n = 1729 
ans = cube_pairs(n)
print(ans) 