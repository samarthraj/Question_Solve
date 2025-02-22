class Factorial:
    def __init__(self, n):
        self.n = n  # stores 'n' inside the object

    def solve(self, num):
        if num == 0 or num == 1:
            return 1
        return num * self.solve(num - 1)  # 'num' is passed in the recursion, same self.n value diff numb values numb -1 

factorial = Factorial(5)
print(factorial.solve(5))  # pass 'num' as 5 to solve()
#>>>>>>>>>>>>>>>>>>>>>>>>>
class Factorial:
    def __init__(self, n):
        self.n = n  # stores 'n' inside the object

    def solve(self):
        if self.n == 0 or self.n == 1:
            return 1
        return self.n * Factorial(self.n - 1).solve()  # uses self.n inside the object, created new object every time for different n-1 values 

factorial = Factorial(5)
print(factorial.solve())  # calls solve() without passing anything
