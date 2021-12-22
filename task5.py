#task5
my_list = [7, 5, 3, 3, 2]
inp = int(input('enter your number '))
count = my_list.count(inp)
for el in my_list:
    if count > 0:
        my_list.insert(my_list.index(inp)+count, inp)
        break
    else:
        if inp > el:
            my_list.insert(my_list.index(el), inp)
            break
        elif inp < my_list[len(my_list) - 1]:
            my_list.append(inp)
print(my_list)

