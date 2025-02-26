#Practice all that was pending 

# def getSecondLargest(arr):  

#     first_max = float('-inf') 
#     second_max = float('-inf') 

#     for i in range(0, len(arr)): 
#         if arr[i] > first_max:
#             second_max = first_max
#             first_max = arr[i] 
        
#         if arr[i] > second_max and arr[i] != first_max: 
#             second_max = arr[i] 

#     return second_max
        

# arr = [10, 5, 4, 6, 3, 10]
# arr2 = [10,5,10] 
# arr3 = [10,10,10]
# arr4 = []
# arr5 = [20]
# ans = getSecondLargest(arr2) 
# print(ans) 


def print_prime_factors(n): 
    pass


n = 10 
ans = print_prime_factors(n)
print(ans) 


def print_all_factors(n): 
    
    ls = []
    #concept is atleast one of them is below <= sq root of n 
    for i in range(1, int(n**(1/2))+1): 
        if n % i == 0: 
            ls.append(i) 
            if i != n//i: 
                ls.append(n//i) 

    return len(ls)
   
n = 18
ans = print_all_factors(n)
print(ans) 


