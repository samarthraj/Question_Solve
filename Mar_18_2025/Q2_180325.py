# self dividing numbers
def solve(left, right):
    ans = []
    for i in range(left, right+1):
        original_numb = i
        self_dividing = True
        while i > 0:
            last_numb = i % 10
            if last_numb == 0 or original_numb % last_numb != 0:
                self_dividing = False
                break
            i = i // 10

        if self_dividing:
            ans.append(original_numb)

    return ans


left = 9
right = 22
ans = solve(left, right)
print(ans)
