# 4 divisors of numbers
def solve(arr):
    final_sum = 0
    for i in range(0, len(arr)):
        ct = 0
        sum = 0
        for j in range(1, arr[i]+1):
            if arr[i] % j == 0:
                ct += 1
                sum += j

        if ct == 4:
            final_sum += sum

    return final_sum


arr = [1,2,3,4,5]
ans = solve(arr)
print(ans)
