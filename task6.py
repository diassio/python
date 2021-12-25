def int_func(str):
    return (str.capitalize())
def capitalize(sentence):
    sentence_arr = sentence.split()
    sentence = ''
    for i in sentence_arr:
        sentence += str(int_func(i)) + ' '
    return sentence
a = capitalize(input('enter your words '))
print(a)