# given an array
# every integer occurs twice
def find(nums):
    ans = 0
    for i in range(32):
        sum = 0
        for num in nums:
            if (num >> i) & 1 == 1:
                sum += 1
                sum %= 3
        if sum != 0:
            ans |= sum << i
    return ans


nums = [4, 1, 2, 1, 2, 1, 2]
ans = find(nums)
print(ans)
