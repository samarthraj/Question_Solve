def solve(string): 
    freq = [0] * 26  

    for char in string:
        freq[ord(char) - ord('a')] += 1

    for char in string:
        if freq[ord(char) - ord('a')] == 1:
            return char 

string = "racecar"
ans = solve(string) 
print(ans) 