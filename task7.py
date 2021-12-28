def fact(n):
    while n > 0:
        yield n
        n -= 1


a = 1
for el in fact(int(input('enter your n to count factorial: '))):
    a *= el
print('result: ' + str(a))
