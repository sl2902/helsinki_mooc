# Write your solution here
phone_dir = {'name': [],
'phone': []}
while 1:
    c = int(input('command (1 search, 2 add, 3 quit): '))
    if c == 1:
        name = input('name: ')
        if name in phone_dir['name']:
            print(f'{phone_dir["phone"][phone_dir["name"].index(name)]}')
        else:
            print('no number')
    elif c == 2:
        name = input('name: ')
        number = input('number: ')
        print('ok!')
        if name in phone_dir['name']:
            phone_dir['phone'][phone_dir["name"].index(name)] = number
        else:
            phone_dir['name'].append(name) 
            phone_dir['phone'].append(number)
    elif c == 3:
        print('quitting...')
        break

