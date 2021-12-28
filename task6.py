import itertools


def array(a, b):
    if a > b:
        return ('Enter correct ending and beginning')
    arr = []
    for i in itertools.count(a, 1):
        arr.append(i)
        if i == b:
            break
    return arr


a = int(input('Enter beginning: '))
b = int(input('Enter ending: '))
arr = array(a, b)
print(arr)


def cycle_arr(arr, cycle_count):
    new_arr = []
    a = itertools.cycle(arr)
    for i in range(cycle_count * len(arr)):
        new_arr.append(next(a))
    return new_arr


print(cycle_arr(arr, int(input('enter number of iterations: '))))
