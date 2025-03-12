#37. Cells with Odd Values in a Matrix

def solve(indices,mat):

    rows = len(mat) 
    cols = len(mat[0]) 
    
    # for i in range(0, rows): 
    #     for j in range(0, cols): 
    #         for k in indices: 
    #             if k[0] == i and k[1] == j: 
    #                 mat[i][j]

    for k in indices:
        ri = k[0] 
        ci = k[1] 

        pass
        



indices = [[0,1],[1,1]]
mat = [[0,0,0],[0,0,0]]
ans = solve(indices,mat)
print(ans) 

