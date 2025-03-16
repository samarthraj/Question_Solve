#good pairs 
from collections import defaultdict

def good_pairs(arr): 
    ct = 0
    #pairs = []
    for i in range(0, len(arr)): 
        for j in range(i+1, len(arr)):  
            if arr[i] == arr[j]: 
                ct += 1
                #pairs.append((i,j)) 
    
    return ct

    # res = 0
    # count = defaultdict(int)
    # for a in arr:
    #     res += count[a]
    #     count[a] += 1
    # print(count)
    # return res



arr = [1,2,3,1,1,3] 
#arr = [1,1,1,1]
ans = good_pairs(arr) 
print(ans) 