#all prime factors 

def prime_factors_str(numb):

    number = int(numb) 
    string = ""

    while number % 2 == 0: 
        number = number // 2 
        string = string + "2 "

    #atleast one factor is less than sqrt of the number 
    for i in range(3, int(number**0.5)+1, 2): 
        while number % i == 0: 
            number = number // i 
            string = string + str(i)  
    
    if number > 1: 
        string = string + str(number)
    return string

nums = "12"
ans = prime_factors_str(nums) 
print(ans) 
