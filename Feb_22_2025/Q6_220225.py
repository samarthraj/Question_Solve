
def sum_of_k_sub_arrays(arr, k):
    n = len(arr) 
    sum = 0
    last_pointer = k - 1
    first_pointer = 0 
    ls = []
    for i in range(0, k): 
        sum = sum + arr[i] 
    ls.append(sum)
    
    while last_pointer < n: 
        #last_pointer += 1
        sum += arr[last_pointer]
        sum -= arr[first_pointer] 
        last_pointer += 1
        first_pointer += 1
        ls.append(sum) 

    print(ls)

arr = [15,2,4,8,9,5,10,23]
k = 3
ans = sum_of_k_sub_arrays(arr, k)
print(ans) 
