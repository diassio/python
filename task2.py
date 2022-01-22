def dev_zero(n, m):
    try:
        result = n / m
        return result
    except ZeroDivisionError:
        return ('Division by zero is impossible')


print(dev_zero(4, 2))
print(dev_zero(4, 0))
