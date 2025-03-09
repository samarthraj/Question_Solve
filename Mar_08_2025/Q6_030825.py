#
def solve(string):
    
    # ls = string.split() 
    # max_str = 0
    # min_str = float('+inf')
    # for i in ls: 
    #     max_str = max(len(i), max_str) 
    #     min_str = min(min_str, len(i)) 
    
    # print(max_str)
    # print(min_str)

    ls = string.split() 
    rev_str = " ".join(''.join(reversed(i)) for i in ls)
    return (rev_str)


string = "this is a test"
ans = solve(string) 
print(ans) 
