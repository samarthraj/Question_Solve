# #sieve of erasthothenes 
# #Find the Prime Numbers till n 

# def prime_nos_till_n(n): 
#     #all nos are prime assumption 
#     vector = [True] * (n+1) 

#     for i in range(2, int(n**0.5)+1): 
#         if vector[i]: 
#             for j in range(i*i, n+1, i): 
#                 vector[j] = False 
    
#     for i in range(2, len(vector)): 
#         if vector[i]: 
#             print(i, end = ' ')


# n = 100 
# ans = prime_nos_till_n(n)
# print(ans) 


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def rotated_sorted(arr):

#     #check for drops, if its sorted after rotation it will have only one drop 
#     drop = 0 

#     for i in range(0, len(arr)-1): 
#         if arr[i+1] < arr[i]: 
#             drop += 1
        
#     if arr[-1] > arr[0]: 
#         drop += 1
    
#     if drop > 1: 
#         return False
#     else:
#         return True

# arr = [2,3,4,5,1,-9,2,4,57] 
# ans = rotated_sorted(arr)
# print(ans)


