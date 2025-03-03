#Transpose of a matrix 
# Rotate a Matrix 

def rotate_matrix(matrix): 
    # rows = len(matrix)
    # cols = len(matrix[0]) 
    # transpose_matrix = [[0] * rows for _ in range(cols)]

    # for i in range(rows): 
    #     for j in range(cols):
    #         transpose_matrix[j][i] = matrix[i][j]  

    # return transpose_matrix  

    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):  
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp 

    for row in matrix:
        row.reverse()

    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = rotate_matrix(matrix) 
print(ans) 
