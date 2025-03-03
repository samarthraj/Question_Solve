def matrix_boundary(matrix): 
    
    n= len(matrix) 
    m = len(matrix[0]) 

    for i in range(n):
        print(i, end = ' ') 
    
    for i in range(1, m):
        print(matrix[i][m-1]) 
    
    for i in range(m-2, n-1): 
        print()

    for 





matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = matrix_boundary(matrix) 
print(ans) 