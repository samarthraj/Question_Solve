def solve(mat):

    mat.sort(key = lambda a: a[1]) 
    last_end = float('-inf')
    count = 0

    for start,end in mat: 
        if start < last_end: 
            count += 1
        else:
            last_end = end

    return count
    

# mat =  [[1,2],
#         [2,3],
#         [3,4],
#         [1,3]] 

mat = [[3,2], 
       [1,2], 
       [1,2], 
       [1,2]] 

#mat =  [[1,2],[1,2],[1,2]]

ans = solve(mat)
print(ans) 
