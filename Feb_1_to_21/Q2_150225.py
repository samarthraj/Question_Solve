# def sorted(arr, k): 
#     for i in range(0, len(arr)): 
#         if arr[i] == k: 
#             return True 
#     return False

def findUnion(a,b):

    
    # for i in range(0, len(a)): 
    #     if a[i] not in b:
    #         union.append(a[i])
    #     elif a[i] not in union: 
    #         union.append(a[i]) 
    
    # for j in range(0, len(b)): 
    #     if b[j] not in a: 
    #         union.append(b[j])
    #     elif b[j] not in union: 
    #         union.append(b[j]) 

    # return union

    union = []
    for i in range(0, len(a)): #O(N)
        if a[i] not in union: 
            union.append(a[i]) 
    
    for j in range(0, len(b)): #O(N) 
        if b[j] not in union: 
            union.append(b[j]) 
    
    union.sort()
    return union

#a = [1, 2, 3, 4, 5]
#b = [1, 2, 3, 6, 7]

a = [2, 2, 3, 4, 5]
b = [1, 1, 2, 3, 4]

#a = [1, 1, 1, 1, 1]
#b = [2, 2, 2, 2, 2]
ans = findUnion(a, b) 
print(ans)