def even_factors_sum(num):
   
    sum = 0
    if num % 2 == 0: 
        sum += num 
    for i in range(2, int(num**0.5)+1): 
        if num % i == 0: 
            ans = num // i 
            if ans % 2 == 0: 
                sum += ans
            elif i % 2 == 0:
                sum += i
    
    return sum
        
num = 18 
ans = even_factors_sum(num) 
print(ans) 
