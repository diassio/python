class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Starting drawing')


class Pen(Stationery):
    def draw(self):
        print(f'Writing with {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Drawing with {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Signing with {self.title}')


pen = Stationery('Pen')
pen.draw()
pencil = Pencil('pencil')
pencil.draw()
handle = Handle('handle')
handle.draw()
