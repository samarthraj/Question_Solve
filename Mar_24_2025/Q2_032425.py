# panagram - string that contains all 26 alphabets

def solve(pan):
    
    seen = [False]*26 

    for char in pan: 
        if 'a' <= char.lower() <= 'z': 
            seen[ord(char.lower()) - ord('a')] = True

    if False in seen: 
        return "Not a Panagram"
    else: 
        return "Its a Panagram, Yaaaay"


pan = "The quick brown fox jumps over the lazy dog"
#pan = "Thu"
ans = solve(pan)
print(ans)
