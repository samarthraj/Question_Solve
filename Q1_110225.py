# def sum_of_nums(numb): 

#     #take the last number 
#     sum_nums = 0
#     while numb > 0: 
#         last_number = numb % 10 
#         numb = numb // 10 
#         sum_nums += last_number 
    
#     return sum_nums

# numb = 123
# ans = sum_of_nums(numb)
# print(ans)

# def getSecondLargest(arr): 
#     #concept is that if some number becomes first, first number becomes second 
#     max_number = float('-inf') 
#     second_max_numb = float('-inf')  

#     if len(arr) < 2:
#         return -1

#     for i in range(0, len(arr)): 
#         if arr[i] > max_number: 
#             second_max_numb = max_number 
#             max_number = arr[i] 
        
#         elif arr[i] != max_number and arr[i] > second_max_numb: 
#             second_max_numb = arr[i] 
    
#     if second_max_numb == float('-inf'):
#         return -1 

#     return second_max_numb



# arr = [10, 5, 4, 9, 3, 10]
# arr2 = [10,5,10] 
# arr3 = [10,10,10]
# arr4 = []
# arr5 = [20]
# ans = getSecondLargest(arr)
# print(ans)


# def prime_factors(n): 
    
#     #in order to do prime factors of a number we can use seive of erastosthenes 
#     #basic concept is for any number atleast one factor is less than root N 
#     #here you need to find prime factors of which 2 is the only even prime no 
#     #so lets find how many 2s are there 
#     prime_factors_ls = []
#     while n % 2 == 0: #O(log N) 
#         n = n // 2
#         prime_factors_ls.append(2) 
    
#     #for the rest 

#     for i in range(3, int(n**0.5)+1, 2): #O(root N)
#         while n % i == 0: #O(log N)
#             n = n // i 
#             prime_factors_ls.append(i) 
    
#     #if n still remains and is a prime itself 
#     if n > 1: 
#         prime_factors_ls.append(n) 

#     return prime_factors_ls

# n = 45
# ans = prime_factors(n)
# print(ans)

# def palindrome(numb):  
#     #to check if a number is palindrome or not 
#     original_numb = numb 
#     rev_numb = 0
#     while numb > 0: 
#         last_numb = numb % 10 
#         rev_numb = rev_numb * 10 + last_numb
#         numb = numb // 10 

#     if original_numb == rev_numb:
#         return True 
#     else: 
#         return False

# numb = 756 
# numb1 = 1221 
# #7 * 100 + 5 * 10 + 6 
# ans = palindrome(numb1) 
# print(ans) 


# def prime_or_not(num): 
#     ct = 0 
#     for i in range(1, int(num**0.5)+1): 
#         if num % i == 0: 
#             ct += 1
    
#     if ct == 1: 
#         return True 
#     else: 
#         return False

# num = 12
# ans = prime_or_not(num)
# print(ans)



def print_fibonacci(n):
    pass 


n = 5
ans = print_fibonacci(n) 
print(ans)


def all_factors_of_nums(n): 

    pass 

n = 10
ans = all_factors_of_nums(n)
print(ans) 


def reduce_the_number_to_one(n): 
    pass 

n = 14
ans = reduce_the_number_to_one(n) 
print(ans) 


def factorial_of_a_number(numb): 

    #given a number find the number next to the zero in its factorial 
    #nos that contribute for its factorial are 2 and 5 
    ct_of_2s = 0
    ct_of_5s = 0
    product = 1
    for i in range(1, numb+1): 
        while i % 2 == 0: 
            i = i // 2
            ct_of_2s += 1
        
        while i % 5 == 0: 
            i = i // 5
            ct_of_5s += 1

        product = (product * i) % 10 
    

    rem_2s = (ct_of_2s - ct_of_5s)
    ans = (product*(2**rem_2s))%10 

    return ans 


numb = 10
ans = factorial_of_a_number(numb)
print(ans)
#3,628,800




