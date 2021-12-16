#task 6
a = int(input('km in a first day '))
b = int(input('desired result km '))
count = 1
while a // b < 1:
    a = a * 1.1
    count += 1
    if a // b > 1:
        break
print('desired results would be in {0} days'.format(count))