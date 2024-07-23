# Write your solution here
arr = []
c = 0
while 1:
    w = input('Word: ')
    if w in arr:
        print(f'You typed in {c} different words')
        break
    arr.append(w)
    c += 1