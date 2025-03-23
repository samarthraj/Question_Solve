# given an array of integers
# variable target given
# return indices of two numbers
# such that they add upto target

def solve(arr, target):

    dict = {}
    for i in range(0, len(arr)):
        pair = target - arr[i]
        if arr[i] in dict:
            return [dict[arr[i]], i]
        else:
            dict[pair] = i


arr = [2, 7, 11, 15]
target = 9
ans = solve(arr, target)
print(ans)
