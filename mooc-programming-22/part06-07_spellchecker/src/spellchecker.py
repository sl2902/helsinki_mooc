# write your solution here
text = input('Write text: ')
filename = 'wordlist.txt'
with open(filename, 'r') as f:
    words = [line.strip().lower() for line in f]

new_text = ''
for word in text.split():
    if not word.lower() in words:
        new_text += "*" + word + "*" + " "
    else:
        new_text += word + " "
print(new_text.strip())