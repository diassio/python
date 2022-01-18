class Matrix:
    def __init__(self, *arr):
        self.arr = arr

    def __add__(self, other):
        try:
            result = []
            for i in range(len(self.arr)):
                result.append([])
                for j in range(len(self.arr[0])):
                    result[i].append(self.arr[i][j] + other.arr[i][j])
            return Matrix(*result)
        except:
            print('Error, adding matrix impossible')

    def __str__(self):
        str_mtrx = ''
        for line in self.arr:
            str_mtrx += (f'{line}\n')
        return str_mtrx


m1 = Matrix([1, 2, 3], [1, 2, 3], [1, 1, 1])
m2 = Matrix([3, 2, 1], [1, 2, 3], [1, 2, 3])


print(f'first matrix:\n{m1}', end='')
print(f'second matrix:\n{m2}', end='')
print(f'sum of matrix:\n{m1 + m2}', end='')
