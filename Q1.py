class calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def adder(self):
        return self.input1 + self.input2

    def subtractor(self):
        return self.input1 - self.input2

    def multiplier(self):
        return self.input1 * self.input2

    def divider(self):
        return self.input1 / self.input2

    def clear(self):
        self.input1 = 0
        self.input2 = 0

try:
    input1 = int(input('Enter 1st number: '))
    input2 = int(input('Enter 2nd number: '))

    calc = calculator(input1, input2)

    print('Add: ', calc.adder())
    print('Subtract: ', calc.subtractor())
    print('Multiply: ', calc.multiplier())
    print('Divide: ', calc.divider())
    calc.clear()
except:
    print('Invalid Input')