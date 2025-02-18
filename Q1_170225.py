#Questions for Today
# def reverse_array(arr): 
    

#     pointer = len(arr) - 1

#     for i in range(0, len(arr)): 
#         if pointer > i: 
#             temp = arr[pointer] 
#             arr[pointer] = arr[i]
#             arr[i] = temp 
#             pointer -= 1 
#     #return arr
    

# arr =   [1]
# ans = reverse_array(arr) 
# print(ans) 


# def build(nums):
#     ans = [0]*len(self.nums) 
#     for i in range(0, len(self.nums)): 
#         ans[i] = self.nums[self.nums[i]] 

#     return ans

# nums = [0,2,1,5,3,4]
# #print(nums[nums[i]]) 
# ans = build(nums)
# print(ans) 


# def solve(arr):
#     ans = [0]*2*len(self.arr) 
#     i = 0
#     while i < 2*len(self.arr): 
#         for j in range(0, len(self.arr)): 
#             ans[i] = self.arr[j] 
#             i += 1 
    
#     return ans

# arr = [1,3,2,1]
# ans = solve(arr)
# print(ans) 


# def running_sum(arr): 

#     sum = [0]*len(self.arr) 
#     sum_of_each = 0
#     for i in range(0, len(self.arr)): 
#         sum_of_each += self.arr[i] 
#         sum[i] = sum_of_each 

#     return sum

# arr = [1,2,3,4] 
# ans = running_sum(arr) 
# print(ans) 


def shuffle(arr): 
    i = 0 
    j = len(arr) // 2

    pass
    
arr = [1,2,3,4,4,3,2,1]
ans = shuffle(arr)
print(ans) 

