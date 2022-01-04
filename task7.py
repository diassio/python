import json

dict = {}
sum_profit = 0
num_comp = 0
with open('task7.txt', 'r') as txt_file:
    for line in txt_file:
        firm_name, prop, profit, cost = line.split(',')
        dict[firm_name] = int(profit) - int(cost)
        if dict.setdefault(firm_name) >= 0:
            sum_profit += dict.setdefault(firm_name)
            num_comp += 1
    if num_comp > 0:
        avr = sum_profit / num_comp
        print('average = ' + str(avr))
    else:
        print('None')
    prof_avr = {'Average profit': round(avr)}
    dict.update(prof_avr)
    print(dict)
with open('task7.json', 'w') as file_json:
    json.dump(dict, file_json)
    js_str = json.dumps(dict)
