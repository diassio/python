#task 2
inp = input('enter your time in sec: ')
hours = int(inp) // 3600
minutes = int((int(inp) - (hours * 3600)) // 60)
seconds = int(int(inp) - (hours * 3600) - (minutes * 60))
if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)
print('{0}:{1}:{2}'.format(hours, minutes, seconds))



