def int_to_binary(n):
    binary = ""
    if n == 0:
        return "0"
    while n > 0:
        binary = str(n % 2) + binary  
        n //= 2 
    return binary

num = 25
print(int_to_binary(num)) 
