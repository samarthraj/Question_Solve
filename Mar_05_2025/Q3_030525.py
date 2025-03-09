#This is not done properly still!!!
def check(mat,target):
    
    rows = len(mat)
    cols = len(mat[0]) 

    for i in range(rows):
        for j in range(i+1, cols): 
            temp = mat[i][j]
            mat[i][j] = mat[j][i] 
            mat[j][i] = temp 
    
    for i in mat: 
       i.reverse()  
    print(mat)
    return mat == target   


mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
ans = check(mat, target) 
print(ans) 