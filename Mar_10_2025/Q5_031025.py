#count negative elements in matrix 


def solve(mat): 

    rows = len(mat) 
    cols = len(mat[0]) 
    count = 0 

    for i in range(rows): 
        for j in range(cols): 
            if mat[i][j] < 0: 
                count += 1
    
    # for i in mat: 
    #     for j in i: 
    #         if j < 0: 
    #             count += 1

    return count 
    


mat = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]] 
ans  = solve(mat) 
print(ans) 
