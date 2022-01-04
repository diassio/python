with open('task5.txt', 'w') as txt_file:
    txt_file.write('10 20 30 40 50 60 70 80 90')
with open('task5.txt', 'r') as txt_file:
    summation = 0
    line = txt_file.readline()
    arr = line.split(' ')
    for el in arr:
        summation += int(el)

    print(summation)