#task 4
num = input('enter your positive integer: ')
arr = []
maximum = 0
for i in num:
    arr.append(i)
print('my \"go to\" solution: ' + max(arr))
# :D
# or

for i in num:
    while int(i) != maximum:
        if int(i) > maximum:
            maximum = int(i)
        break
print('solution number two: ' + str(maximum))