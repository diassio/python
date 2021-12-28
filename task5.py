import functools

arr = [i for i in range(100, 1001, 1) if i % 2 == 0]
print(functools.reduce(lambda a, b: a * b, arr))
