#249. Number of Steps to Reduce a Number to Zero

def solve(num):
    steps = 0
    while num >= 1: 
        if num % 2 == 0: 
            num = num // 2 
            steps += 1
        else: 
            num = num - 1 
            steps += 1
    
    return steps


num = 14 
ans = solve(num) 
print(ans) 