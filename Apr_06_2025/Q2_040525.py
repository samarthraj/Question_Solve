# Amstrong Number
def solve(n):
    ans = 0 
    no_of_digits = len(str(n))
    ori_n = n 

    while n > 0: 
        last_num = n % 10 
        ans += last_num**no_of_digits 
        n = n // 10 

    if ans == ori_n: 
        return True 
    return False


n = 71
ans = solve(n)
print(ans)
