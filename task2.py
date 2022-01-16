class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def full(self):
        return f'{self._length}m * {self._width}m * 25m * 5cm = {self._width * self._length * 25 * 5}t'


a = Road(20, 5000)
print(a.full())
