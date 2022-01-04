with open('task1.txt', 'w') as text_file:
    while True:
        a = text_file.write(input('Enter your string: '))
        text_file.write('\n')
        if not a:
            break

print('=' * 50)

with open('task1.txt', 'r') as text_file:
    print('you have added several lines to your file: \n')
    for line in text_file:
        print(line, end='')