#isomorphic strings 
def is_isomorphic(a, b): 

    a_b = {} 
    b_a = {} 

    for i in range(len(a)): 
        char_a = a[i] 
        char_b = b[i] 

        if char_a in a_b and a_b[char_a] != char_b:
            return False
        if char_b in b_a and b_a[char_b] != char_a:
            return False

        a_b[char_a] = char_b
        b_a[char_b] = char_a 

    print(a_b) 
    print(b_a)
    return True


a = 'badc'
b = 'baba' 
print(is_isomorphic(a, b)) 

