# Write your solution here
import difflib
text = input('Write text: ')
filename = 'wordlist.txt'
with open(filename, 'r') as f:
    words = [line.strip().lower() for line in f]

new_text = ''
mistakes = []
for word in text.split():
    if not word.lower() in words:
        new_text += "*" + word + "*" + " "
        mistakes.append(word)
    else:
        new_text += word + " "
print(new_text.strip())
print('suggestions:')
for word in mistakes:   
    print(f'{word}: ', end="")
    print(*difflib.get_close_matches(word, words), sep=", ")