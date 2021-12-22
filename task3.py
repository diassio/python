#task3
arr = {
    'Winter': (1, 2, 12),
    'Spring': (3, 4, 5),
    'Summer': (6, 7, 8),
    'Autumn': (9, 10, 11)
}
inp = int(input('Enter your months number from 1 to 12:: '))
for key in arr.keys():
    if inp in arr[key]:
        print('{0} months is {1}'.format(inp, key))