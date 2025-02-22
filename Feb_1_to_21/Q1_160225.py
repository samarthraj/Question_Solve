#Question 1 for today 
def square_pattern(n): 
    
    for i in range(n):          # Loop for rows
        for j in range(n):      # Loop for columns
            print('*', end='')  # Print star without a newline
        print() 

n = 5
ans = square_pattern(n)
print(ans) 