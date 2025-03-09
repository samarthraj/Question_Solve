#Subsequence 
#all letters should be in a continuous sequence 
#relative order 
def subsequence(s1,s2): 
    k = 0
    for i in range(0, len(s2)): 
        if s2[i] == s1[k]: 
            k += 1

    if k == len(s1):
        return True 
    return False 

s1 = "AXY" 
s2 = "AXXUY" 
ans = subsequence(s1, s2) 
print(ans) 


