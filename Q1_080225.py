# find sum of all digits in a number
# 6 5 7
# last digit % of 10
# remanining number we get it by - remainder of 10
def sum_of_nums(numb):

    # sum = 0
    # while numb > 0:
    #     last_digit = numb % 10
    #     sum += last_digit
    #     numb = numb // 10

    # return sum

    sum = 0
    str_numb = str(numb)
    for i in range(0,len(str_numb)):
       sum += int(str_numb[i])
    return sum


numb = -221
ans = sum_of_nums(numb)
print(ans)
