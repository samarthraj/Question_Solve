#max rectangles 
def solve(mat):

    #first find the max length 
    count = 0 
    ls = []
    for i in range(len(mat)): 
        l = mat[i][0]
        w = mat[i][1]
        to_trim = min(l, w) 
        ls.append(to_trim)

    for i in ls:
        if i == max(ls): 
            count += 1 
    return count

#mat =  [[5,8],[3,9],[5,12],[16,5]] 
mat = [[2,3],[3,7],[4,3],[3,7]]
ans = solve(mat)
print(ans) 