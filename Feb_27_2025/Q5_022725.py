#Given a String and a patternm count how many times the pattern (or any of its anagrams) appears
#as a substring in the given string 
def find_k_cts(s, k): 

    start = 0
    count = 0 
    n = len(k) 

    while start <= len(s) - n: 
        if s[start:start + n] == k: 
            count += 1
            start += n 
        else: 
            start += 1
    return count

s = "jj&****"
k = "**"
ans = find_k_cts(s, k) 
print(ans)


# a = "aaabbb"
# b = "aaa"
# ans = a.replace(b, "")
# print(ans)
