def sum(args):
    sum = 0
    new_arr = args.split()
    for i in new_arr:

        sum += int(i)

    return (sum)

a = sum(input('enter your numbers: '))
print(a)

