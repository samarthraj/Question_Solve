def all_factors_of_nums(n):
    factor_ls = []
    for i in range(1, int(n**(1/2))+1): #at least one if less than root n 
        if n % i == 0: 
            factor_ls.append(i) 
            factor_ls.append(n//i) 
    
    factor_ls.sort()
    return factor_ls    

n = 10
ans = all_factors_of_nums(n)
print(ans) 
