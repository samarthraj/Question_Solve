# given a string, find the longest palindromic substring
# Naive approach / Brute Force
# def solve(a):
#     ans = ""
#     for start in range(0, len(a)):
#         for end in range(start, len(a)):
#             sub_string = a[start:end+1]
#             if sub_string == sub_string[::-1]:
#                 if len(sub_string) > len(ans):
#                     ans = sub_string

#     return ans

def solve(a):

    # consider each index as the center of a string,
    # and start comparing left and right
    # odd and even length of strings
    start = 0
    max_length = 1
    for i in range(0, len(a)):

        for j in range(0, len(a)):

            left = i
            right = i + j

            while left >= 0 and right < len(a) and a[left] == a[right]:
                curr_max = right - left + 1
                if curr_max > max_length:
                    max_length = curr_max
                    start = left
                left -= 1
                right += 1

    return a[start:start+max_length]


a = "cbbd"
ans = solve(a)
print(ans)
