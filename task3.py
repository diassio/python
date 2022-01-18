class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'


staff = Position('Dias', 'Tashev', 'Data Scientist', 10000000, 9000000)
print(staff.get_full_name())
print(staff.get_full_name())
