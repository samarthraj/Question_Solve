#flip and invert an image 
#bosscoder slipping an image problem 

def flip_an_image(mat):
    #mat = arr
    rows = len(mat) 
    cols = len(mat[0]) 
    result = [] 

    for i in range(0, rows): 
        result.append(mat[i][::-1])
    
    for i in range(rows): 
        for j in range(cols): 
            if result[i][j] == 1: 
                result[i][j] = 0 
            elif result[i][j] == 0:
                result[i][j] = 1  
    
    return result
mat = [[1,1,0],[1,0,1],[0,0,0]] 
ans = flip_an_image(mat) 
print(ans) 