# 293. Rectangle Overlap
def solve(rec1, rec2):
    
    #when they do not over lap 
    #left 
    # x4 <= x1; 

    #top 
    #y3 >= y2; 

    #right 
    #x3 >= x2 
    
    #bottom 
    #y4 <= y1

    #extracting the coordinates 
    x1, y1, x2, y2 = rec1
    x3, y3, x4, y4 = rec2

    if x4 <= x1 or y3 >= y2 or x3 >= x2 or y4 <= y1: 
        return False 
    else: 
        return True


rec1 = [0, 0, 2, 2]
rec2 = [1, 1, 3, 3]
ans = solve(rec1, rec2)
print(ans)
