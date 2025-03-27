# 44. Check if Numbers Are Ascending in a Sentence

def solve(arr):
    
    ls = arr.split()
    ans = []
    for i in range(0, len(ls)): 
        if not ls[i].isalpha(): 
            ans.append(int(ls[i])) 
    
    for i in range(0, len(ans)-1): 
        if ans[i+1] > ans[i]: 
            continue 
        else: 
            return False 
    return True

arr = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
ans = solve(arr)
print(ans)
