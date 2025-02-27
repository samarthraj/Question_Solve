def highest_product(arr):  
    
    product = 1 
    max_product = 1
    for i in range(0, len(arr)): 
        for j in range(i+1, len(arr)): 
            product = arr[i] * arr[j] 
            max_product = max(product, max_product)

    return max_product           

arr = [3,4,5,2]
ans = highest_product(arr) 
print(ans) 
