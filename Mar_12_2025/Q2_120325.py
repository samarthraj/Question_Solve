#spiral Traversal of an array 

def spiral_traversal(matrix): 
    #top and bottom are row pointers 
    #left and right are column pointers 

    rows = len(matrix) 
    cols = len(matrix[0]) 
    top = 0 
    bottom = len(matrix) - 1 
    left = 0
    right = len(matrix[0]) - 1 
    result = [] 

    while left <= right and top <= bottom: 

        for i in range(left, right+1): 
            result.append(matrix[top][i]) 
        top += 1

        for j in range(top, bottom+1):
            result.append(matrix[j][right]) 
        right -= 1 

        if top <= bottom: 
            for k in range(right, left-1, -1): 
                result.append(matrix[bottom][k])
            bottom -= 1 

        if left <= right:
            for l in range(bottom, top-1, -1): 
                result.append(matrix[l][left])
            left += 1

    return result

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] 
ans = spiral_traversal(matrix) 
print(ans)


