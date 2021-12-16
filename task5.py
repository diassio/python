#task 5
revenue = int(input('input your revenue: '))
cost = int(input('input your costs: '))
profit = revenue - cost
if profit > 0:
    print('Good job, your business is profitable!')
    print('your profit is: {0}$'.format(profit))
    profitability = profit*100 / revenue
    print('your profitability is: {0}%'.format(profitability))
    emp = int(input('how many employees in your business? '))
    emp_prof = profit / emp
    print('average employee profit is: {0}$' .format(emp_prof))
else:
    print('Oh no! your business is in debt :( ')
    print('your debt is: {0}$'.format(profit))



