dict = {}
with open('task6.txt', 'r') as txt_file:
    for line in txt_file:
        subj, lect, pract, lab = line.split(',')
        dict[subj] = int(lect) + int(pract) + int(lab)
    print(dict)