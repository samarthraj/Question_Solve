#37. Cells with Odd Values in a Matrix

def solve(indices,m,n):
    mat = [[0]*n for i in range(m)]
    rows = len(mat) 
    cols = len(mat[0]) 
    ct =0
    for r,c in indices: 

        for j in range(cols): 
            mat[r][j] += 1
        
        for i in range(rows): 
            mat[i][c] += 1
    
    for i in range(len(mat)): 
        for j in mat[i]: 
            if j % 2 != 0: 
                ct += 1
    
    return ct

m = 2
n = 3
indices = [[0,1],[1,1]]
#mat = [[0,0,0],[0,0,0]]
ans = solve(indices,m, n)
print(ans) 

