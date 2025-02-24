# given an array size is n-1 
#contains numbers from 1 to n 
# one missing number 

def find_missing_number(n):

    ans = len(n)

    for i in range(0, len(n)): 
        ans = ans ^ i ^ n[i]
    return ans


n = [9,6,4,2,3,5,7,0,1] 
ans = find_missing_number(n) 
print(ans) 
