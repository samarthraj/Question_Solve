# given two strings, diff between the, should be o/p
def solve(s, t):
    dict = {}
    ans = ""
    for i in range(0, len(s)):
        if s[i] not in dict:
            dict[s[i]] = 1
        else:
            dict[s[i]] += 1

    for j in range(0, len(t)):
        if t[j] in dict.keys() and dict[t[j]] > 0:
            dict[t[j]] -= 1
        else:
            ans += t[j]

    return ans


s = "a"
t = "aa"
ans = solve(s, t)
print(ans)
