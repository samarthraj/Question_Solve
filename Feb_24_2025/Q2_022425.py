def fibanochi(n): 

    a = 0
    b = 1 
    for i in range(n): 
        #print (a, end = ' ')
        temp = a
        a = b 
        b = b + temp 
        
    
n = 10 
#1 1 2 3 5 8 13 
ans = fibanochi(n) 
#print(ans) 


def palindrome(n): 
    rev_number = 0
    while n > 0: 
        last_numb = n % 10 
        rev_number = rev_number * 10 + last_numb
        n = n // 10 
    
    print(rev_number)

n = 1232
#make that like 4321 and compare 
ans = palindrome(n)
print(ans) 
