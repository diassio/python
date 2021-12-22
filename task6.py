array = []
counter = 1
title = None
price = None
quantity = None
while True:
    if title is None:
        title = input('Enter the title: ')
    if price is None:
        price = input('Enter the price: ')
    if quantity is None:
        quantity = input('enter quantity: ')

    unit = input('enter your units: ')
    array.append((
        counter,
        {
            'title': title,
            'price': price,
            'quantity': quantity,
            'unit': unit
        }
    ))
    title = None
    price = None
    quantity = None
    counter += 1
    quit = input('would you like to break? y/n: ')
    if quit == 'y':

        break
print(array)