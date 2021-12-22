#task4
x = input('Enter your sentence ')
arr = []
arr.append(x.split())
for i in arr:
    for word_ind in range(len(i)):
        word = i[word_ind]
        print('{0}. {1}'.format(word_ind+1, word[:10]))