#find first repeating character 

def solve(string): 
    freq = [0]*26 

    for char in string: 
        freq[ord(char) - ord('a')] += 1
        for i in freq: 
            if i == 2: 
                print(char) 
                break

string = "sama"
ans = solve(string) 
print(ans) 
