# given an array
# of integer all of them are distinct
# find 4 elements such that
# (a,b,c,d)
# a+b = c+d

def solve(arr):

    dict = {}

    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if dict[arr[i]+arr[j]] !=
            dict[arr[i]+arr[j]] = [arr[i], arr[j]]


arr = [3, 4, 7, 1, 2, 9, 8]
ans = solve(arr)
print(ans)
