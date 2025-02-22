# You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation exactly k times in order to maximize your score:
# Select an element m from nums.
# Remove the selected element m from the array.
# Add a new element with a value of m + 1 to the array.
# Increase your score by m.
# Return the maximum score you can achieve after performing the operation exactly k times.

def solve(arr, k): 

    score = 0 
    m = max(arr) 

    while k > 0: 
        score += m 
        m += 1
        k -= 1
    
    return score

arr = [1, 2, 3, 4, 5]
k = 3
ans = solve(arr, k) 
print(ans)
