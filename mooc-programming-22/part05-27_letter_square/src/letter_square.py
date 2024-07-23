# Write your solution here
import string
n = int(input('Layers: '))
height = 2*n - 1
l = [string.ascii_uppercase[:n]]
if n == 1:
    print(l[0])
else:
    for i in range(1, n):
        s = l[i-1]
        tmp = ''
        for c in s[:i]:
            tmp += chr(ord(c) + 1)
        l.append(tmp + s[len(tmp):])
    ll = [i[::-1] for i in l]

    ll = [ll[idx] + ele for idx, ele in enumerate([i[-height+n:] for i in l])]
    ll = ll[1:][::-1] + ll[:1] + ll[1:]
    for i in range(height):
        print(ll[i])
