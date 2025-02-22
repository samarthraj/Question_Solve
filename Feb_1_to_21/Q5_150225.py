# a + (n-1)d

def find_missing_number_ap(n):
    diff = (n[-1] - n[0]) // len(n)
    for i in range(1, len(n)-1): 
        #diff = (n[-1] - n[0]) // len(n)
        if (n[i+1] - n[i]) != diff: 
            ans = n[i+1] - diff

    return ans

n = [2,4,8,10] 
ans = find_missing_number_ap(n) 
print(ans) 

