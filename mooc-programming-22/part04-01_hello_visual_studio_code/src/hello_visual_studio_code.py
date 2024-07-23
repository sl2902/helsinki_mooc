# Write your solution here
while 1:
    s = input('Editor: ')
    s = s.lower()
    if s == 'notepad' or s == 'word':
        print('awful')
    elif s == 'visual studio code':
        print('an excellent choice!')
        break
    else:
        print('not good')