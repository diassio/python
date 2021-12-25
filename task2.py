def user(name, surname, year_birth, city_birth, residence, email, phone):
    return('{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(name, surname, year_birth, city_birth, residence, email, phone))

u1 = user(input('enter your name '),input('enter your surname '),input('enter your year of birth '),input('enter your city of birth '),input('enter your residence '),input('enter your email '),input('enter your phone number '))
print(u1)