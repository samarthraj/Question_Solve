# arr of integers
# [1,2,2,1,1,3]
# return true if no of occurances
# of each value is unique

def solve(arr):
    
    dict = {} 

    for i in range(0, len(arr)): 
        if arr[i] not in dict: 
            dict[arr[i]] = 1 
        else:
            dict[arr[i]] += 1
    
    frequencies = set(dict.values())

    if len(frequencies) == len(dict):
        return True 
    return False


arr = [1, 2, 2, 1, 1, 3]
ans = solve(arr)
print(ans)
