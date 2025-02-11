#write a function that has to check if a number is a prime or not 
#print all prime nums from 1 to 100
# CONCEPT - 
# def prime_or_not(num): 
#     # ct = 0
#     # for i in range(1,num+1):  O(N) 
#     #     if num % i == 0:
#     #         ct += 1

#     # if ct == 2: 
#     #     return True 
#     # else: 
#     #     return False 
#     pass 

def prime_or_not(num): 
    #basic concept is a number will have atleast one factor < root N 
    
    if num < 2: 
        return "{} Not a Prime".format(num) 
    
    for i in range(2, int(num**(1/2))+1): 
        if num % i == 0: 
            return "{} Not a Prime".format(num) 
    return "{} is a Prime".format(num) 

            
num = 1009
ans = prime_or_not(num)
print(ans)