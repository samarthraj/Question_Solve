# aeiou
# from collections import defaultdict
# def solve(word):

#     right = 0
#     left = 0
#     ans_dict = defaultdict(int)
#     ct_answer = 0
#     while right < len(word):
#         if word[right] not in "aeiou":
#             left = right + 1
#             ans_dict.clear()
#         else:
#             ans_dict[word[right]] += 1

#             while all(ans_dict[v] > 0 for v in "aeiou"):
#                 ct_answer += (right - left + 1)
#                 ans_dict[word[left]] -= 1
#                 left += 1

#         right += 1

#     return ct_answer

from collections import defaultdict


def solve(word):
    right = 0
    left = 0
    ans_dict = defaultdict(int)
    ct_answer = 0

    for right in range(len(word)):
        if word[right] not in "aeiou":
            # Reset the window if we encounter a non-vowel
            left = right + 1
            ans_dict.clear()  # Clear the vowel counts
        else:
            ans_dict[word[right]] += 1

            # Once we have all vowels, count valid substrings
            while all(ans_dict[v] > 0 for v in "aeiou"):
                ct_answer += (len(word) - right)  # Count this substring
                ans_dict[word[left]] -= 1
                left += 1  # Shrink the window from the left side

    return ct_answer


word = "cuaieuouac"
ans = solve(word)
print(ans)
