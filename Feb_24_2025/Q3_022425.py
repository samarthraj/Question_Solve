#print last non zero digit of a factorial 
def last_nonzero_digit(n): 
    ct2 = 0
    ct5 = 0
    factorial_without_2_5 = 1
    for i in range(1, n+1): 

        while i % 2 == 0: 
            i = i // 2 
            ct2 += 1
        
        while i % 5 == 0: 
            i = i // 5
            ct5 += 1
        
        factorial_without_2_5 = (factorial_without_2_5*i) % 10 
    
    extra_twos_ct = ct2 - ct5 
    ans = (factorial_without_2_5*(2**extra_twos_ct))%10

    return ans


n = 10 
ans = last_nonzero_digit(n) 
print(ans) 