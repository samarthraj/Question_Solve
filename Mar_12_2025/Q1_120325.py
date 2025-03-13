def solve(indices,n, m):  

    mat = [[0]*n for _ in range(m)]
    #print(mat)
    for ri, ci in indices: 

        for col in range(len(mat[0])): 
            mat[ri][col] += 1 
        
        for row in range(len(mat)):  
            mat[row][ci] += 1 
    
    return mat


n = 3
m = 2
indices = [[0,1],[1,1]]
ans = solve(indices,n, m)
print(ans) 