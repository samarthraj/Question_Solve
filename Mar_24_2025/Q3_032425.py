# check if s1 is a subsequence of s2
def solve(s1, s2):

    j = 0  # s1 pointer
    if len(s1) > 0:
        for i in range(0, len(s2)):
            if j < len(s1) and s2[i] == s1[j]:
                j += 1
            elif j == len(s1):
                return True
        return j == len(s1)
    else:
        return True


s1 = "b"
s2 = "abc"
ans = solve(s1, s2)
print(ans)
