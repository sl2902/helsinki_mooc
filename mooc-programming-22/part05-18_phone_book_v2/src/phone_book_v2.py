# Write your solution here
phone_dir = {}
while 1:
    is_found = False
    c = int(input('command (1 search, 2 add, 3 quit): '))
    if c == 1:
        name = input('name: ')
        if name in phone_dir:
            # print(f'{name}')
            for num in phone_dir[name]:
                print(num)
        else:
            print('no number')
    elif c == 2:
        name = input('name: ')
        number = input('number: ')
        print('ok!')
        if name not in phone_dir:
            phone_dir[name] = []
        phone_dir[name].append(number)
    elif c == 3:
        print('quitting...')
        break