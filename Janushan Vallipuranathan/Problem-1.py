class Calculator:
    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op
        
    def calculate(self):
        if self.op == '+':
            return self.a + self.b
        elif self.op == '-':
            return self.a - self.b
        elif self.op == '*':
            return self.a * self.b
        elif self.op == '/':
            if self.b != 0:
                return self.a / self.b
            else :
                return "Error: Cannot divide by zero"
        else:
            return "Invalid Operator"
            
    
a = float(input("Enter value for a:"))
b = float(input("Enter value for b:"))
op = input("Enter Operator (+, -, *, /):")
    
calc = Calculator(a,b ,op)
result = calc.calculate()
print(result)