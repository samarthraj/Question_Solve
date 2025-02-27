#Q2_180225 
#Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.
#Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

# def sum_of_all_int_357(n): 
#     sum = 0
#     for i in range(0, n+1): 
#         if i % 3 == 0 or i % 5 == 0 or i % 7 == 0: 
#             sum += i 
    
#     return sum 

# n = 30
# ans = sum_of_all_int_357(n) 
# print(ans) 

#remove duplicates

def remove_duplicates(arr):
    pointer = 0 
    for i in range(0, len(arr)): 
        if arr[i] != arr[pointer]: 
            pointer += 1 
            arr[pointer] = arr[i]
            
    return arr[:pointer+1]

arr = [1,1,1,2,2,2,3,3]
ans = remove_duplicates(arr)
print(ans) 



