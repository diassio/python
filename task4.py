def my_func(x, y):
    counter = 0
    exponentiation = 1
    while counter != y:
        exponentiation *= x
        counter += 1
    return exponentiation

print('result ' + str(my_func(int(input('base ')), int(input('power ')))))
