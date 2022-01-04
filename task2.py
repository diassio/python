with open('task2.txt') as text_file:
    count = 0
    word_count = 0
    for line in text_file:
        count+= 1
        word_list = line.split()
        word_count = len(word_list)
        print('there are {0} words on the {1} line'.format(word_count, count))

    print('there are ' + str(count) + ' lines in the file.')