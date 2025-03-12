#Diagonal sum of matrix 

def matrix_diagonal(matrix): 
    
    rows = len(matrix)
    cols = len(matrix[0]) 
    sum = 0 
    for i in range(rows): 
        for j in range(cols): 
            if i == j: 
                sum += matrix[i][j]
            elif (i + j) == (rows - 1):
                sum += matrix[i][j] 

    return sum 


    # rows = len(matrix) 
    # sum = 0

    # for i in range(rows): 
    #     sum += matrix[i][i] 

    #     if i != rows - 1 - i:
    #         sum += matrix[i][rows - 1 - i]
    
    # return sum 

#matrix =  [[1,2,3], [4,5,6], [7,8,9]] 
matrix =  [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
ans = matrix_diagonal(matrix) 
print(ans) 
