#find absolute difference between sum of even and odd digits 

# def sum_of_diff(n): 
#     sum_even = 0
#     sum_odd = 0
#     while n > 0: 
#         remainder = n % 10 
#         rest_numb = n // 10
#         if remainder % 2 == 0:
#             sum_even += remainder 
#         elif remainder % 2 != 0:
#             sum_odd += remainder
    
#     print(sum_even, sum_odd) 

def sum_of_diff(n): 

    if n < 0: 
        numb = -n 
    else: 
        numb = n

    #or also use numb = abs(n)

    sum_of_even = 0
    sum_of_odd = 0
    while numb > 0: 
        last_numb = numb % 10 
        numb = numb // 10 

        if last_numb % 2 == 0: 
            sum_of_even += last_numb
        elif last_numb % 2 != 0: 
            sum_of_odd += last_numb 
    
    return abs(sum_of_even - sum_of_odd)

n = -1234
ans = sum_of_diff(n)
print(ans)




