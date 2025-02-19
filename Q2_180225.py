#Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.
#Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

def solve(n):
    sum = 0
    # for i in range(0, n+1): 
    #     if i % 3 == 0 or i % 5 == 0 or i % 7 == 0: 
    #         sum += 
    # return sum

    while n > 0: 
        if n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
            sum += n 
        n -= 1 

    return sum

n = 10
ans = solve(n)
print(ans) 
