def matrix_boundary(arr): 
    rows = len(arr)
    cols = len(arr[0]) 

    for i in range(0, cols): 
        print(arr[0][i], end = ' ') 
    
    for j in range(1, rows): 
        print(arr[j][cols-1], end = ' ') 
    
    for k in range(cols-2, -1, -1): 
        print(arr[rows-1][k], end = ' ') 
    
    for l in range(rows-2, 0, -1): 
        print(arr[l][0], end = ' ')

    pass

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = matrix_boundary(matrix) 
print(ans) 