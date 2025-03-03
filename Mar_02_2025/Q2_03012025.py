def check_matrix(mat, tar): 

    n = len(mat) 

    for i in range(n): 
        for j in range(i+1, n): 
            temp = mat[j][i]
            mat[j][i] = mat[i][j]
            mat[i][j] = temp 
    
    for row in mat:
        row.reverse()
    print(mat)
    if mat == tar: 
        return True 
    else:
        return False


mat = [[0,0,0],[0,1,0],[1,1,1]]
tar = [[1,1,1],[0,1,0],[0,0,0]]
ans = check_matrix(mat, tar)  
print(ans) 