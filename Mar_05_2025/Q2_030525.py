#rotate matrix 90 degree 

def rotate_mat(arr): 

    rows = len(arr) 
    cols = len(arr[0]) 

    for i in range(rows): 
        for j in range(i+1, cols): 
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp 
    
    for row in arr:
        row.reverse()

    return arr

arr = [
    [1, 2, 3],
    [5, 6, 7],
    [9, 10, 12]
] 
ans = rotate_mat(arr)
print(ans) 
