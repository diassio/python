dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
modified_list = []
with open('task4.txt', 'r') as txt_file:
    for line in txt_file:
        line = line.split(' ', 1)
        modified_list.append(dictionary[line[0]] + ' ' + line[1])
print('text modified')
with open('task4_modified.txt', 'w') as txt_file:
    txt_file.writelines(modified_list)
