#given 2 strings 
#s1, s2 
#check if s2 is a rotation of s1 
def solve(s1,s2):
    ans = s1+s1
    if s2 in ans:
        return True 
    return False

s1 = "abcd" 
s2 = "cdab" 
ans = solve(s1,s2)
print(ans) 

