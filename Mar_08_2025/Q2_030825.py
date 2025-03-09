#given a binary string 
#count the number of 
#substrings that starts and end with 1 

def substring(string): 
    ct = 0
    for i in string: 
        if i == "1": 
            ct += 1
    
    ans = ct*(ct+1)//2
    return ans
        

string = "00100101"
#ans is 3 
ans = substring(string) 
print(ans) 
