# paranthesis question
# write a code to find if a string is valid or not

# ((()))
# (()))

def solve(string):
    stack = []

    for char in string:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            top = stack.pop()
            if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                return False

    return True


string = "((())"
ans = solve(string)
print(ans)
