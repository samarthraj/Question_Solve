# 314. Reverse words in a given string

def solve(s):
    ls = s.split() 
    ans = " "
    for i in range(len(ls)-1, -1, -1): 
        ans = ans + " " + ls[i] 
    
    return ans

s = "bosscoder quiz practice code"
ans = solve(s)
print(ans)
