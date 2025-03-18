# 2578. Split With Minimum Sum
def solve(num):
    sorted_ls = sorted(str(num))
    num1 = ''
    num2 = ''

    for i in range(0, len(sorted_ls)):
        if i % 2 == 0:
            num1 += sorted_ls[i]
        else:
            num2 += sorted_ls[i]

    return int(num1) + int(num2)


num = 4325
ans = solve(num)
print(ans)
