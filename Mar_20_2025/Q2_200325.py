# 41. Check If Array Pairs Are Divisible by k
from collections import Counter
from collections import defaultdict


def solve(arr, k):
    # makes a dict by counting the remainders
    # this way the sum of remainders pair among themselves
    # Remainder 1 appears 2 times (Numbers: 1, 6)
    # Remainder 2 appears 2 times (Numbers: 2, 7)
    # Remainder 3 appears 2 times (Numbers: 3, 8)
    # Remainder 4 appears 2 times (Numbers: 4, 9)
    # Remainder 0 appears 2 times (Numbers: 5, 10)
    # Counter({1: 2, 2: 2, 3: 2, 4: 2, 0: 2})
    # remainder_count = Counter(num % k for num in arr)
    dict = defaultdict(int)
    for num in arr:
        rem = (num % k)
        dict[rem] += 1

    if (dict[0] % 2) != 0:
        return False

    for remainder, count in dict.items():
        if remainder == 0:  # already checked
            continue

        # check if the remainder has some other remainder such that (rem1 + rem 2) % k == 0
        # (rem1 + rem 2) % k == 0
        # rem2 = (k - rem1) % k
        other_remainder = (k - remainder) % k
        if dict[other_remainder] != dict[remainder]:
            return False

    return True


arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
k = 5
ans = solve(arr, k)
print(ans)
