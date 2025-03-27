# 63. Count Pairs Of Similar Strings
def solve(words):

    dict = {}
    ct = 0
    for i in range(0, len(words)):
        dict[i] = set(words[i])

    for key in dict.keys():
        pointer = key + 1
        while pointer < len(dict):
            if dict[key] == dict[pointer]:
                ct += 1
            pointer += 1

    return ct


words = ["aba", "aabb", "abcd", "bac", "aabc"]
ans = solve(words)
print(ans)
