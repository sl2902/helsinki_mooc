# Write your solution here
import datetime
filename = input('Filename: ')
start_date = input('Starting date: ')
start_date = datetime.datetime.strptime(start_date, '%d.%m.%Y').date()
n = int(input('How many days: '))
usage = []
print('Please type in screen time in minutes on each day (TV computer mobile):')
total_time, counter = 0, 0
with open(filename, 'w') as f:
    for i in range(n):
        new_date = datetime.datetime.strftime(start_date + datetime.timedelta(days=i), '%d.%m.%Y')
        inp = input(f'Screen time {new_date}: ')
        usage.append(inp)
        total_time += sum(int(t) for t in inp.split())
        # counter += len(inp)
    print(f'Data stored in file {filename}')
    f.write(f'Time period: {datetime.datetime.strftime(start_date, "%d.%m.%Y")}-{datetime.datetime.strftime(start_date + datetime.timedelta(days=n-1), "%d.%m.%Y")}' + "\n")
    f.write(f'Total minutes: {total_time}' + "\n")
    f.write(f'Average minutes: {total_time/n}' + "\n")
    for i in range(n):
        new_date = datetime.datetime.strftime(start_date + datetime.timedelta(days=i), '%d.%m.%Y')
        f.write(f'{new_date}: {usage[i].replace(" ", "/")}' + "\n")
