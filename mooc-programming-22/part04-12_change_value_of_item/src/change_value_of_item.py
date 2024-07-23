# Write your solution here
a = [1, 2, 3, 4, 5]
while 1:
    idx = int(input('Index: '))
    if idx == -1:
        break
    value = int(input('New value: '))
    a[idx] = value
    print(a)