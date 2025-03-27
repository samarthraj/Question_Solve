# circular
def solve(a):
    first_letter = a[0]
    last_letter = a[-1]
    ls = a.split()

    if first_letter == last_letter:
        for i in range(0, len(ls)-1):
            last_letter = ls[i][-1]
            first_letter = ls[i+1][0]
            if last_letter == first_letter:
                continue
            else:
                return False
    else:
        return False

    return True


a = "leetcode exercises soundu delightful"
ans = solve(a)
print(ans)
#