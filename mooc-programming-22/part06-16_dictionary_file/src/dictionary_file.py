# Write your solution here
def make_word_dict(word_list: list) -> dict:
    word_dict = {}
    if len (word_list) > 0:
        for i, w in enumerate(word_list):
            if i%2 == 0:
                k = w
                word_dict[k] = w
            else:
                word_dict[k] = w
    return word_dict

r = open('dictionary.txt', 'r')
word_list = [word.strip() for word in r]
word_dict = {}
w = open('dictionary.txt', 'a')
while 1:
    print('1 - Add word, 2 - Search, 3 - Quit')
    function = input('Function: ')
    if function == "1":
        fin = input('The word in Finnish: ')
        eng = input('The word in English: ')
        print('Dictionary entry added')
        if not fin in word_list:
            w.write(fin + "\n")
            word_list.append(fin)
        if not eng in word_list:
            w.write(eng + "\n")
            word_list.append(eng)
    elif function == "2":
        term = input('Search term: ')
        word_dict = make_word_dict(word_list)
        for k, v in word_dict.items():
            if term in k or term in v:
                print(f'{k} - {v}')
    else:
        print('Bye')
        break
r.close()
w.close()
    

