def division(numerator, denumerator):
    try:
        result = (numerator)/(denumerator)
    except ZeroDivisionError:
        result = 'Division by zero is not possible'
    return result
inp = division(int(input('enter numerator ')), int(input('input denumerator ')))
print('your result is: ' + str(inp))