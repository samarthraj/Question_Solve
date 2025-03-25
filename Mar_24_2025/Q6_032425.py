# find first repeating character
def solve(string):
    dict = {}

    for i in range(0, len(string)):
        if string[i] not in dict:
            dict[string[i]] = 1
        else:
            dict[string[i]] += 1

        if dict[string[i]] == 2:
            return string[i]


string = "sama"
ans = solve(string)
print(ans)
