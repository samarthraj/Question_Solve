#union arrays 
def findUnion(a,b):
    union = []
    
    for i in range(0, len(a)): 
        if a[i] not in union: 
            union.append(a[i]) 

    for j in range(0, len(b)):
        if b[j] not in union: 
            union.append(b[j])  
    
    union.sort()

    return union

a = [1, 2, 3, 4, 5]
b= [1, 2, 3, 6, 7]
ans = findUnion(a,b) 
print(ans) 
