# def solve(a):
#     #a = self.a
#     if a == a[::-1]:
#         return True
#     else:
#         return False

# 13. Anagram String

def solve(str1, str2):

    # a = ' '.join(sorted(str1))
    # b = ' '.join(sorted(str2))
    # if a == b:
    #     return True
    # return False

    dict = {}

    for i in range(0, len(str1)):
        if str1[i] not in dict:
            dict[str1[i]] = 1
        else:
            dict[str1[i]] += 1

    for j in range(0, len(str2)):
        if str2[j] not in dict:
            dict[str2[j]] = 1
        else:
            dict[str2[j]] -= 1

    print(dict)

    for i in dict.keys():
        if dict[i] != 0 or len(str2) > len(str1):
            return False
        else:
            continue
    return True


str1 = "a"
str2 = "abb"
ans = solve(str1, str2)
print(ans)
