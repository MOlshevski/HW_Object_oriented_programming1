class Math:  # Creating a class

    def __init__(self, a, b):  # Creating a constructor
        self.a = a
        self.b = b

    def addition(self):  # Creating methods
        print(f'{self.a} + {self.b} = {self.a + self.b}')

    def subtraction(self):
        print(f'{self.a} - {self.b} = {self.a + self.b}')

    def multiplication(self):
        print(f'{self.a} * {self.b} = {self.a * self.b}')

    def division(self):
        print(f'{self.a} / {self.b} = {self.a / self.b}')


example_1 = Math(int(input('Number a = ')), int(input('Number b = ')))  # Entering numbers from the keyboard
op = input('Operation(+, -, *, /) - ')  # Entering operation from the keyboard
if op == '+':  # Cycle for the operation with numbers a and b
    example_1.addition()
elif op == '-':
    example_1.subtraction()
elif op == '*':
    example_1.multiplication()
elif op == '/':
    example_1.division()
else:
    print('ERROR')  # In case an incorrect operation is entered