# teams winner
# If the current number of teams is even, 
# each team gets paired with another team. 
# A total of n / 2 matches are played, 
# and n / 2 teams advance to the next round.

# If the current number of teams is odd, 
# one team randomly advances in the tournament, 
# and the rest gets paired. A total of (n - 1) / 2 matches are played, 
# and (n - 1) / 2 + 1 teams advance to the next round.

# Return the number of matches played in the tournament until a winner is decided.

def solve(n):
    ans = 0
    while n > 1: 
        if n % 2 == 0: 
            matches_played = n // 2
            n = n // 2
            
        else: 
            matches_played = (n - 1) // 2 
            n = ((n - 1) // 2) + 1 

        ans += matches_played
            
    return ans

n = 7
ans = solve(n)
print(ans)
