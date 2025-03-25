# given a binary string
# count the number of
# substrings that starts and end with 1

def solve(binary_str):
    ct_ones = 0
    for i in range(0, len(binary_str)):
        if binary_str[i] == "1":
            ct_ones += 1

    # no_of_subarrays = n! // r! (n-r)! + n (n is nothing but no of ones), r = 2
    # because we choose two ones from the total no of ones in the string
    no_of_subarrays = (ct_ones*(ct_ones - 1) // 2) + ct_ones
    return no_of_subarrays

binary_str = "00100101"
ans = solve(binary_str)
print(ans)
