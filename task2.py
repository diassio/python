class Clothes:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    @property
    def coat(self):
        return f'coat needs {round(int(self.width) / 6.5 + 0.5)}m of textile'
    @property
    def suit(self):
        return f'suit needs {round(int(self.height) * 2 + 0.3)}m of textile'


c = Clothes(input('Enter the name of your product: '),
            input('Enter the width of the textile: '),
            input('Enter the width of the textile: ')
            )
print(c.coat)
print(c.suit)
