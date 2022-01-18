class Cells:
    def __init__(self, num_of_cellules):
        self.num_of_cellules = num_of_cellules

    def __add__(self, other):
        sum = int(self.num_of_cellules) + int(other.num_of_cellules)
        return Cells(sum)

    def __sub__(self, other):
        sub = int(self.num_of_cellules) - int(other.num_of_cellules)
        if sub > 0:

            return Cells(sub)

        else:
            print('Unable to subtract')

    def __mul__(self, other):
        mul = int(self.num_of_cellules) * int(other.num_of_cellules)
        return Cells(mul)

    def __truediv__(self, other):
        div = int(self.num_of_cellules) // int(other.num_of_cellules)
        return Cells(div)

    def __str__(self):
        return (f'your result is: \n{self.make_order()}')

    def make_order(self, num_row=5):
        row = 'Your result is: \n'
        for i in range(self.num_of_cellules // num_row):
            row += num_row * '*' +'\n'
        row += (self.num_of_cellules % num_row) * '*'
        return row


a = Cells(int(input('Enter number of cells 1:   ')))
b = Cells(int(input('Enter number of cells 2:   ')))
c = a + b
d = a - b
e = a * b
f = a / b
print(c.make_order(12))
print(d.make_order(3))
print(e.make_order(10))
print(f.make_order())