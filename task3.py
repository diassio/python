with open('task3.txt', 'r') as txt_file:
    num_lines = 0
    sum_salaries = 0
    for line in txt_file:
        salary = line.split(',')
        if int(salary[1]) > 20000:
            print(salary[0])
        sum_salaries += int(salary[1])
        num_lines += 1

    average = sum_salaries / num_lines

    print('Average salary is ' + str(average))
