def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a >= b and c >= b:
        return a + c
    else:
        return b + c

inp = my_func(int(input('enter a ')), int(input('enter b ')), int(input('enter c ')))
print(inp)