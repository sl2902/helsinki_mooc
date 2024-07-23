# Write your solution here
arr, new_arr = [], []
while 1:
    item = int(input('New item: '))
    if item == 0:
        print('Bye!')
        break
    arr.append(item)
    print(f'The list now: {arr}')
    new_arr.append(item)
    print(f'The list in order: {sorted(new_arr)}')