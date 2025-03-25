# given two string if same length
# s1 is rotation of s2
def solve(s1, s2):
    
    # for i in range(0, len(s1)): 
    #     s1 = s1[-1] + s1[:-1] 
    #     if s1 == s2: 
    #         return True
    # return False

    ans = s1 + s1 
    if s2 in ans: 
        return True
    return False

s1 = "abcd"
s2 = "cdab"
ans = solve(s1, s2)
print(ans)
