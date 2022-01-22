class ComplexNumber:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
        print(self.real + self.imag)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.imag * other.real + self.real * other.real)


i = ComplexNumber(2, 10j)
k = ComplexNumber(3, 5j)
print('sum is;')
i + k
print('mult. is;')
i * k
