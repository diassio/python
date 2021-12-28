def salary(work_time, wage_in_hour, prize):
    return ((work_time * wage_in_hour) + prize)


print('Ваша зарплата: ' + str(salary(int(input('Введите выработку в часах: ')), int(input('Введите вашу ставку в час: ')),
             int(input('ВВедите вашу премию: ')))))
