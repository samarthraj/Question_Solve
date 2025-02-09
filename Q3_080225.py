# factorial of a number
# How zero is introduced we need to think
# then we can remove 2 and 5 since it contributes to zero

def factorial(numb):
    # fact = 1
    # for i in range(1, numb):
    #     fact = fact * i
    # print(fact)

    # while fact > 0:
    #     last_digit = fact % 10
    #     rem_numb = fact // 10
    #     if last_digit != 0:
    #         return fact
    #     else:
    #         rem_numb = rem_numb % 10
    #         return rem_numb
    pass
    # find the non zero digit
numb = 10
ans = factorial(numb)
print(ans)
