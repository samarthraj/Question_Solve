#190. Maximum 69 Number
def solve(num):
    
    str_num = str(num) 
    max_position = float('+inf') 
    answer = num
    for i in range(0, len(str_num)): 
        if str_num[i] == '6': 
            max_position = min(max_position, i) 
    
    for j in range(0, len(str_num)): 
        if j == max_position: 
            answer = num + ((10**(len(str_num) - j - 1)) * 3)
    return answer
# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
num = 999
ans = solve(num) 
print(ans) 