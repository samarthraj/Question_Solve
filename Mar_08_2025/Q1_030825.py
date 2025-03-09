#Strings questions 
#given a string return 
#frequencey of each character 

def freq(string): 
    freq = [0]*52
    
    for char in string: 
        if 'a' <= char <= 'z': 
            freq[ord(char) - ord('a')] += 1
        elif 'A' <= char <= 'Z': 
            freq[ord(char) - ord('A') + 26] += 1

    return freq

string = "aabAbbcacc" 
ans = freq(string) 
print(ans) 


