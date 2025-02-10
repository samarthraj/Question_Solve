#palindrome 
#we will reverse this digit, 
#to reverse I wil
# def palindrome(numb): 
#     tmp = numb 
#     rev = 0
#     while numb > 0: 
#         rev = rev * 10 + numb % 10
#         numb = numb / 10 
        
      
def palindrome(numb): 

    reversed_number = 0
    original_numb = numb
    while numb > 0: 
        last_number = numb % 10 
        reversed_number = reversed_number * 10 + last_number
        numb = numb // 10 

    if original_numb == reversed_number: 
        return True
    else: 
        return False


numb = 756 
numb1 = 1221 
#7 * 100 + 5 * 10 + 6 
ans = palindrome(numb1) 
print(ans) 


