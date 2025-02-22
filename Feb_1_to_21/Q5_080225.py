#num n reduce it to 1 by two ways do -1 or divide by two 
#print the minimum number of steps 
# def reduce_to_1(n): 
#     ct = 0
#     while n > 1: 
#         if n % 2 == 0: 
#             n = n // 2
#             ct += 1 
#         else: 
#             n = n - 1
#             ct += 1
#     return ct


def reduce_the_number_to_one(n): 

    #How many steps or cts to reduce the number to one by subtracting 1 or divide by two 
    #when we will divide by two when its an even 
    #when we will -1, when its an odd numb 
    ct = 0
    while n > 1: 
        if n % 2 == 0: 
            n = n // 2
            ct += 1
        elif n % 2 != 0: 
            n = n - 1
            ct += 1
    
    return ct

n = 14
ans = reduce_the_number_to_one(n) 
print(ans) 