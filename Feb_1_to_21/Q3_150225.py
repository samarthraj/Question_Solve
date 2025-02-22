#find sum of its alternate digits 
# 1 2 3 4 5 6 7 8 

def sum_of_alternate(n): 
    count = 0
    even_sum = 0
    odd_sum = 0
    while n > 0: 
        last_numb = n % 10 
        if count % 2 == 0: 
            even_sum += last_numb 
        else: 
            odd_sum += last_numb  

        count += 1
        n = n // 10 

    return even_sum, odd_sum



n = 1224
ans = sum_of_alternate(n) 
print(ans)