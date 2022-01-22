class Except:
    arr = []

    def input(self):

        while True:
            try:
                num = int(input('Enter your number: '))
                self.arr.append(num)
                print(f'Your array:  {self.arr} \n ')
            except:
                Except().error()
                break

    def error(self):
        print(f"\nIt is not a number.")
        question = input(f'type (stop) to stop the program or type to continue :  ')
        if question.lower() == 'stop':
            print('\n')
            print('-' * 100)
            print(f'Program is stopped, your final array is: {self.arr}')
            print('-' * 100)
        else:
            Except().input()

Except().input()
