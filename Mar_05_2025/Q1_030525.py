#2D array questions - Matrix 
#first get the values from a matrix and then fo to doing transpose 
#Transpose a Matrix which is of size nxn only!!! 

def transpose_matrix(matrix): 
    #BELOW LOGIC WORKS FOR ALL SIZE MATRIX
    # rows = len(matrix) 
    # cols = len(matrix[0]) 
    # new_mat = [[0]*rows for _ in range(cols)]

    # for i in range(0, rows):
    #     for j in range(0, cols): 
    #         new_mat[j][i] = matrix[i][j] 
    
    # return new_mat

    #Now we will learn how to transpose a matrix without using an extra space 
    #works only for nxn 
    rows = len(matrix)
    cols = len(matrix[0]) 

    for i in range(rows): 
        for j in range(i+1, cols): 
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i] 
            matrix[j][i] = temp 

    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
] 

ans = transpose_matrix(matrix)
print(ans) 