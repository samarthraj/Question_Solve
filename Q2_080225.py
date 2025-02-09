#palindrome 
#we will reverse this digit, 
#to reverse I wil
def palindrome(numb): 
    tmp = numb 
    rev = 0
    while numb > 0: 
        rev = rev * 10 + numb % 10
        numb = numb / 10 
        
      



numb = 756 
#7 * 100 + 5 * 10 + 6 
ans = palindrome(numb) 
print(ans) 


