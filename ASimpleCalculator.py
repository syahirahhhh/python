# Classes and Objects Self-Assessment: A Simple Calculator #

class SimpleCalculator:
    num1=None
    num2=None
    oper=None
    def __init__(self,num1,num2,oper):
        self.num1=num1
        self.num2=num2
        self.oper=oper
    def addition(self):
        result=self.num1+self.num2
        print(f"{self.num1} {self.oper} {self.num2} = {result}")
    def subtraction(self):
        result = self.num1 - self.num2
        print(f"{self.num1} {self.oper} {self.num2} = {result}")
    def multiplication(self):
        result = self.num1 * self.num2
        print(f"{self.num1} {self.oper} {self.num2} = {result}")
    def division(self):
        result = self.num1 / self.num2
        print(f"{self.num1} {self.oper} {self.num2} = {result}")

prog=SimpleCalculator(num1,num2,oper)

if operation == "+":
    prog.addition()
elif operation == "-":
    prog.subtraction()
elif operation == "*":
    prog.multiplication()
elif operation == "/":
    prog.division()
else:
    print("Operator invalid, try again")

print("End of program, thank you!")


