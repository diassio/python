class Data:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def date(cls, date):
        my_date = []

        for i in date.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Date is correct'
                else:
                    return f'Error Year'
            else:
                return f'Error Month'
        else:
            return f'Error Day'

    def __str__(self):
        return f'Текущая дата {Data.date(self.date)}'


today = Data('11 - 1 - 2001')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.date('11 - 11 - 2011'))
print(Data.valid(1, 11, 2000))