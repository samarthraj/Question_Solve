# max cons ones
def solve(arr):
    ct = 0
    max_ct = 0
    for i in range(0, len(arr)):
        if arr[i] != 1:
            ct = 0
        else:
            ct += 1
        max_ct = max(max_ct, ct)

    return max_ct


arr = [1, 0, 1, 1, 0, 1]
ans = solve(arr)
print(ans)
