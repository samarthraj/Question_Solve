#sort the string 
def solve(string):

    #ans = ''.join(" ".join(sorted(i) for i in string))
    ans = "".join(''.join(sorted(i)) for i in string)
    return ans

string = "bosscoder is good" 
ans = solve(string)
print(ans) 
