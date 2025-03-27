# 340. Sorting the Sentence

def solve(s):

    ls = s.split()
    ct = 1
    ans = []

    while ct < len(ls)+1:
        for i in range(0, len(ls)):
            if str(ct) in ls[i]:
                replaced_str = ls[i].replace(str(ct), "")
                ans.append(replaced_str)
                ct += 1

    return " ".join(ans)


s = "is2 sentence4 This1 a3"
ans = solve(s)
print(ans)
