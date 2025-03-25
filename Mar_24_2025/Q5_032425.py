# def solve(string):

#     ls = string.split()
#     #rev_str = " ".join(''.join(reversed(i)) for i in ls)
#     rev_str = " ".join("".join(reversed(i)) for i in ls)

#     return (rev_str)


# string = "this is a test"
# ans = solve(string)
# print(ans)

# count no of equal pairs

def solve(string):
    pair = []
    for i in range(0, len(string)):
        for j in range(0, len(string)):
            if i != j and string[i] == string[j]:
                pair.append((i, j))

    return len(pair)


string = "aabb"
ans = solve(string)
print(ans)
