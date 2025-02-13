#GCD of a number 
#greatest common devisor of two numbers 
# GCD X LCM = a X b 

def gcd(a,b): 
    gcd = 0
    for i in range(1, min(a,b)):
        if a % i == 0 and b % i == 0: 
            gcd = i  
    return gcd

def lcm(a,b): 
    lcm = (a * b) // gcd(a,b) 
    return lcm

a = 48
b = 18 
ans_gcd = gcd(a,b)
ans_lcm = lcm(a,b)
print(ans_gcd)
print(ans_lcm) 

