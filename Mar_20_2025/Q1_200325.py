# 94. Factorial Trailing Zeroes

def solve(n):

    # the zeros in a factorial are contributed by 2s and 5s
    ct_2 = 0
    ct_5 = 0
    factorial = 1
    for i in range(1, n+1):

        while i % 2 == 0:
            i = i // 2
            ct_2 += 1

        while i % 5 == 0:
            i = i // 5
            ct_5 += 1

        # factorial = (factorial * i) % 10 #just to reduce the actual factorial

    # rem_twos = ct_2 - ct_5

    # print(ct_2)
    # print(ct_5)
    # factorial = (factorial * 2**(rem_twos))% 10
    return ct_5


n = 10
ans = solve(n)
print(ans)
