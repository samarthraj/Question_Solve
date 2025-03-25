# given an array,
# return count of distinct numbers in
# all windows of size k

def solve(arr, k):

    dict = {} 
    start = 0
    for end in range(0, len(arr)):
        #Add the current element to the frequency map
        #When the window reaches size k





arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
ans = solve(arr, k)
print(ans)
