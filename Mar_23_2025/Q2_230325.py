# find number of subarrys with sum zero
# find the largest subarray with sum zero

def solve(arr):

    dict = {0: 1}
    sum = 0
    ct = 0
    for i in range(0, len(arr)):
        sum += arr[i]

        if sum - k in dict:
            ct += dict[sum-k]


arr = [15, -2, 2, -8, 1, 7, 10, 23]
ans = solve(arr)
print(ans)
