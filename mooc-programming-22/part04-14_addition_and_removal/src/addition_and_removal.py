# Write your solution here
arr = []
i = 0
while 1:
    print(f'The list is now {arr}')
    choice = input('a(d)d, (r)emove or e(x)it: ')
    if choice == 'd':
        i += 1
        arr.append(i)
    elif choice == 'r':
        arr.pop(-1)
        i -= 1
    else:
        print('Bye!')
        break