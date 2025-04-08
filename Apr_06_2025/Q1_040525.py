def solve(n):

    # do a reverse of this number and check if palindrome
    original_number = n
    rev_number = 0

    while n > 0:
        last_number = n % 10
        rev_number = rev_number * 10 + last_number
        n = n // 10

    if rev_number == original_number:
        return True
    else:
        return False


n = 1771
ans = solve(n)
print(ans)
