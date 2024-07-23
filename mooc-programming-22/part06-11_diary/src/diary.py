# Write your solution here
while 1:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    function = int(input('Function: '))
    if function == 1:
        entry = input('Diary entry: ')
        f = open('diary.txt', 'a')
        f.write(entry + "\n")
        print('Diary saved')
        f.close()
    elif function == 2:
        print('Entries:')
        with open('diary.txt', 'r') as r:
            for line in r:
                print(line.strip())
    else:
        print('Bye now')
        break