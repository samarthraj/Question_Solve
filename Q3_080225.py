# factorial of a number
# How zero is introduced we need to think
# then we can remove 2 and 5 since it contributes to zero

# find the last number that is not zero 
# def factorial_of_a_number(numb):

#     #what numbers contribute for zero? 
#     #2 and 5!
#     fact = numb
#     while numb > 1: 
#         numb = numb - 1
#         fact = fact * (numb)

#     ct_of_twos = 0
#     ct_of_fives = 0

#     while fact > 0: 
#         if fact % 2 == 0: 
#             fact = fact // 2 
#             ct_of_twos += 1 
#         elif fact % 5 == 0:
#             fact = fact // 5
#             ct_of_fives += 1 
#         else: 
#             break
#     #print(ct_of_twos, ct_of_fives)

#     extra_twos = ct_of_twos - ct_of_fives
#     fact = fact * (2**extra_twos) 

#     non_zero_numb = fact % 10 
#     return non_zero_numb

def factorial_of_a_number(numb): 
    product = 1 
    ct_of_twos = 0
    ct_of_fives = 0
    for i in range(1, numb+1): 
        num = i  

        while num % 2 == 0: 
                num = num // 2 
                ct_of_twos += 1 

        while num % 5 == 0:
            num = num // 5
            ct_of_fives += 1 
    
    #multiply or calculating factorial withouts 2s and 5s, and do %10 just to store last digit
        product = (product * num) % 10 
    
    extra_twos = ct_of_twos - ct_of_fives
    product = (product * (2 ** extra_twos) % 10)  

    return product

numb = 10
ans = factorial_of_a_number(numb)
print(ans)
#3,628,800
